"""
CART Decision Tree Classifier for Aggregate OLAP Data.

This module implements a sklearn-compatible decision tree classifier that works
directly with pre-aggregated data containing good/bad counts.
"""

from typing import List, Tuple, Optional, Union, Any, Dict
import pandas as pd
import numpy as np
import json

from .tree_nodes import TreeNode, LeafNode
from .utils import (
    compute_gini_impurity,
    compute_impurity,
    information_gain,
    validate_aggregate_data,
    sample_to_dict,
    print_tree
)


class AggregateCART:
    """
    CART Decision Tree Classifier for aggregate data with sklearn-compatible API.

    This classifier builds decision trees directly from aggregate data with
    good/bad counts, without needing access to individual raw records. It supports
    multiple impurity criteria and comprehensive hyperparameter control.

    Parameters:
    -----------
    criterion : {"gini", "entropy", "log_loss"}, default="gini"
        The function to measure the quality of a split.

    max_depth : int, default=None
        Maximum depth of the tree. If None, nodes are expanded until
        all leaves are pure or contain less than min_samples_leaf samples.

    min_samples_split : int, default=2
        Minimum number of samples required to split an internal node.

    min_samples_leaf : int, default=1
        Minimum number of samples required to be at a leaf node.

    min_weight_fraction_leaf : float, default=0.0
        Minimum weighted fraction of the sum total of weights required
        to be at a leaf node (not implemented in aggregate version).

    max_features : int, float, {"sqrt", "log2"}, default=None
        Number of features to consider when looking for the best split:
        - If int, consider max_features features at each split.
        - If float, max_features is a fraction and ceil(max_features * n_features) features are considered.
        - If "sqrt", max_features=sqrt(n_features).
        - If "log2", max_features=log2(n_features).
        - If None, max_features=n_features.

    random_state : int, default=None
        Random seed for reproducible results when max_features is used.

    max_leaf_nodes : int, default=None
        Maximum number of leaf nodes (not fully implemented).

    min_impurity_decrease : float, default=0.0
        Minimum impurity decrease required for a split to happen.

    ccp_alpha : float, default=0.0
        Complexity parameter for minimal cost-complexity pruning (not implemented).

    Attributes:
    -----------
    tree_ : TreeNode or LeafNode
        The root node of the fitted tree.

    feature_names_ : list
        Names of binary features used during fitting.

    original_feature_names_ : list
        Names of original categorical features before one-hot encoding.

    feature_mapping_ : dict
        Mapping from original features to their binary encodings.

    n_features_ : int
        Number of binary features used during fitting.

    classes_ : array
        Class labels (always [0, 1] for binary classification).

    Examples:
    ---------
    >>> import pandas as pd
    >>> from cart_olap import AggregateCART
    >>>
    >>> # Load aggregate data
    >>> df = pd.read_csv('aggregate_data.csv')
    >>>
    >>> # Initialize and fit classifier with entropy criterion
    >>> cart = AggregateCART(
    ...     criterion='entropy',
    ...     max_depth=10,
    ...     min_samples_leaf=5,
    ...     max_features='sqrt',
    ...     random_state=42
    ... )
    >>> feature_cols = ['source', 'city', 'dayType']
    >>> cart.fit(df, feature_cols, 'good_count', 'bad_count')
    >>>
    >>> # Predict on new samples
    >>> new_data = pd.DataFrame({
    ...     'source': ['ios'],
    ...     'city': ['Delhi'],
    ...     'dayType': ['WEEKEND']
    ... })
    >>> predictions = cart.predict(new_data)
    >>> probabilities = cart.predict_proba(new_data)
    """

    def __init__(
        self,
        criterion: str = "gini",
        max_depth: Optional[int] = None,
        min_samples_split: int = 2,
        min_samples_leaf: int = 1,
        min_weight_fraction_leaf: float = 0.0,
        max_features: Optional[Union[int, float, str]] = None,
        random_state: Optional[int] = None,
        max_leaf_nodes: Optional[int] = None,
        min_impurity_decrease: float = 0.0,
        ccp_alpha: float = 0.0
    ):
        # Validate criterion
        if criterion not in ["gini", "entropy", "log_loss"]:
            raise ValueError(f"criterion must be 'gini', 'entropy', or 'log_loss', got {criterion}")

        self.criterion = criterion
        self.max_depth = max_depth
        self.min_samples_split = min_samples_split
        self.min_samples_leaf = min_samples_leaf
        self.min_weight_fraction_leaf = min_weight_fraction_leaf
        self.max_features = max_features
        self.random_state = random_state
        self.max_leaf_nodes = max_leaf_nodes
        self.min_impurity_decrease = min_impurity_decrease
        self.ccp_alpha = ccp_alpha

        # Fitted attributes
        self.tree_ = None
        self.feature_names_ = None
        self.n_features_ = None
        self.classes_ = np.array([0, 1])  # Binary classification

    def fit(
        self,
        X: pd.DataFrame,
        feature_cols: List[str],
        good_col: str,
        bad_col: str,
        total_col: Optional[str] = None
    ) -> 'AggregateCART':
        """
        Build decision tree from aggregate data.

        Parameters:
        -----------
        X : DataFrame
            Input aggregate data with feature columns and count columns.

        feature_cols : list of str
            Names of categorical feature columns to use for splitting.

        good_col : str
            Name of column containing good class counts.

        bad_col : str
            Name of column containing bad class counts.

        total_col : str, optional
            Name of column containing total counts for validation.

        Returns:
        --------
        self : AggregateCART
            Fitted classifier.
        """
        # Validate input data
        validate_aggregate_data(X, feature_cols, good_col, bad_col, total_col)

        # One-hot encode categorical features
        print("Performing one-hot encoding of categorical features...")
        X_encoded, binary_feature_names = self._one_hot_encode_features(X, feature_cols)

        # Store original and encoded feature information
        self.original_feature_names_ = feature_cols.copy()
        self.feature_names_ = binary_feature_names.copy()
        self.n_features_ = len(binary_feature_names)
        self.feature_mapping_ = self._create_feature_mapping(feature_cols, binary_feature_names)

        print(f"Original features: {len(feature_cols)} -> Binary features: {len(binary_feature_names)}")

        # Build the tree on encoded data using boolean mask approach
        # Start with all rows being True (no filtering initially)
        initial_mask = pd.Series([True] * len(X_encoded), index=X_encoded.index)
        self.tree_ = self._build_tree(
            X_encoded, binary_feature_names, good_col, bad_col, initial_mask, depth=0
        )

        return self

    def _one_hot_encode_features(self, X: pd.DataFrame, feature_cols: List[str]) -> Tuple[pd.DataFrame, List[str]]:
        """
        One-hot encode categorical features to create binary variables.

        Parameters:
        -----------
        X : DataFrame
            Input data with categorical features
        feature_cols : List[str]
            Names of categorical feature columns

        Returns:
        --------
        X_encoded : DataFrame
            Data with one-hot encoded binary features
        binary_feature_names : List[str]
            Names of the binary features created
        """
        X_encoded = X.copy()
        binary_feature_names = []

        for feature in feature_cols:
            # Get unique values for this categorical feature
            unique_values = sorted(X[feature].unique())

            # Create binary columns for each unique value
            for value in unique_values:
                binary_col_name = f"{feature}={value}"
                # Create binary column: 1 if feature equals value, 0 otherwise
                X_encoded[binary_col_name] = (X[feature] == value).astype(int)
                binary_feature_names.append(binary_col_name)

        return X_encoded, binary_feature_names

    def _create_feature_mapping(self, original_features: List[str], binary_features: List[str]) -> Dict[str, List[str]]:
        """
        Create mapping from original categorical features to their binary encodings.

        Returns:
        --------
        mapping : Dict[str, List[str]]
            Mapping from original feature name to list of binary feature names
        """
        mapping = {}
        for orig_feature in original_features:
            mapping[orig_feature] = [
                binary_feat for binary_feat in binary_features
                if binary_feat.startswith(f"{orig_feature}=")
            ]
        return mapping

    def _build_tree(
        self,
        data: pd.DataFrame,
        available_features: List[str],
        good_col: str,
        bad_col: str,
        current_mask: pd.Series,
        depth: int = 0
    ) -> Union[TreeNode, LeafNode]:
        """
        Recursively build the decision tree using boolean masks to avoid copying data.

        Parameters:
        -----------
        data : DataFrame
            Original full dataset (never copied, only filtered with masks).
        available_features : list
            Features available for splitting at this node.
        good_col : str
            Good count column name.
        bad_col : str
            Bad count column name.
        current_mask : Series
            Boolean mask indicating which rows belong to this node.
        depth : int
            Current depth in the tree.

        Returns:
        --------
        node : TreeNode or LeafNode
            The root node of the subtree.
        """
        # Calculate node statistics using the current mask
        filtered_data = data[current_mask]
        good_count = filtered_data[good_col].sum()
        bad_count = filtered_data[bad_col].sum()
        total_samples = good_count + bad_count
        node_impurity = compute_impurity(good_count, bad_count, self.criterion)

        # Check stopping criteria
        if self._should_stop_splitting(
            filtered_data, available_features, total_samples, node_impurity, depth
        ):
            return LeafNode(good_count, bad_count, depth)

        # Find best split using the filtered data
        best_feature, best_value, best_gain = self._find_best_split(
            filtered_data, available_features, good_col, bad_col
        )

        # If no good split found, create leaf
        if best_feature is None or best_gain <= self.min_impurity_decrease:
            return LeafNode(good_count, bad_count, depth)

        # Create internal node
        node = TreeNode(
            feature=best_feature,
            split_value=best_value,
            samples=total_samples,
            impurity=node_impurity,
            good_count=good_count,
            bad_count=bad_count,
            depth=depth
        )

        # Create cascading masks for children instead of copying data
        # Left child: current_mask AND feature=False
        # Right child: current_mask AND feature=True
        feature_true_mask = data[best_feature] == 1   # feature=True (present)
        feature_false_mask = data[best_feature] == 0  # feature=False (absent)

        left_mask = current_mask & feature_false_mask   # Cascade: parent filter AND feature=False
        right_mask = current_mask & feature_true_mask   # Cascade: parent filter AND feature=True

        # Check if children would have any samples
        left_samples = data[left_mask][good_col].sum() + data[left_mask][bad_col].sum()
        right_samples = data[right_mask][good_col].sum() + data[right_mask][bad_col].sum()

        # Recursively build children using cascaded masks
        if left_samples > 0:
            node.left = self._build_tree(
                data, available_features, good_col, bad_col, left_mask, depth + 1
            )
        else:
            node.left = LeafNode(0, 0, depth + 1)

        if right_samples > 0:
            node.right = self._build_tree(
                data, available_features, good_col, bad_col, right_mask, depth + 1
            )
        else:
            node.right = LeafNode(0, 0, depth + 1)

        return node

    def _find_best_split(
        self,
        data: pd.DataFrame,
        available_features: List[str],
        good_col: str,
        bad_col: str
    ) -> Tuple[Optional[str], Any, float]:
        """
        Find the best binary feature to split on using the configured criterion.

        For one-hot encoded features, we split on feature=true vs feature=false.
        This follows the same logic as the theta sketches implementation.

        Returns:
        --------
        tuple : (best_feature, split_value, best_gain)
            Best split information, or (None, None, 0) if no valid split.
        """
        parent_good = data[good_col].sum()
        parent_bad = data[bad_col].sum()
        parent_impurity = compute_impurity(parent_good, parent_bad, self.criterion)

        best_feature = None
        best_gain = 0.0
        split_value = True  # Binary split: feature=True vs feature=False

        # Apply max_features limitation by randomly selecting features
        features_to_try = available_features.copy()
        if self.max_features is not None:
            n_features = len(available_features)
            if isinstance(self.max_features, int):
                max_features_to_use = min(self.max_features, n_features)
            elif isinstance(self.max_features, float):
                max_features_to_use = max(1, int(self.max_features * n_features))
            elif self.max_features == "sqrt":
                max_features_to_use = max(1, int(np.sqrt(n_features)))
            elif self.max_features == "log2":
                max_features_to_use = max(1, int(np.log2(n_features)))
            else:
                max_features_to_use = n_features

            if max_features_to_use < n_features:
                if self.random_state is not None:
                    np.random.seed(self.random_state)
                features_to_try = list(np.random.choice(
                    available_features, size=max_features_to_use, replace=False
                ))

        for feature in features_to_try:
            # For binary features, split on feature=True vs feature=False
            mask_true = data[feature] == 1  # feature=True (present)
            mask_false = data[feature] == 0  # feature=False (absent)

            # Calculate counts for True (right) and False (left)
            right_good = data.loc[mask_true, good_col].sum()
            right_bad = data.loc[mask_true, bad_col].sum()
            left_good = data.loc[mask_false, good_col].sum()
            left_bad = data.loc[mask_false, bad_col].sum()

            # Skip if split creates empty child or no actual split
            if (left_good + left_bad == 0) or (right_good + right_bad == 0):
                continue

            # Check minimum samples per leaf constraint
            left_total = left_good + left_bad
            right_total = right_good + right_bad
            if left_total < self.min_samples_leaf or right_total < self.min_samples_leaf:
                continue

            # Verify the split actually separates the data
            total_left_right = left_total + right_total
            if total_left_right != (parent_good + parent_bad):
                continue  # Data doesn't add up correctly

            # Calculate weighted impurity for children
            total_samples = parent_good + parent_bad
            left_weight = left_total / total_samples
            right_weight = right_total / total_samples

            left_impurity = compute_impurity(left_good, left_bad, self.criterion)
            right_impurity = compute_impurity(right_good, right_bad, self.criterion)

            weighted_child_impurity = (left_weight * left_impurity +
                                     right_weight * right_impurity)

            # Calculate information gain
            gain = parent_impurity - weighted_child_impurity

            if gain > best_gain:
                best_gain = gain
                best_feature = feature

        return best_feature, split_value, best_gain

    def _encode_prediction_data(self, X: pd.DataFrame) -> pd.DataFrame:
        """
        One-hot encode prediction data using the same encoding as training.

        Parameters:
        -----------
        X : DataFrame
            Input data with original categorical features

        Returns:
        --------
        X_encoded : DataFrame
            Data with one-hot encoded binary features matching training
        """
        X_encoded = pd.DataFrame()

        # Copy any non-feature columns
        for col in X.columns:
            if col not in self.original_feature_names_:
                X_encoded[col] = X[col]

        # One-hot encode each original categorical feature
        for orig_feature in self.original_feature_names_:
            if orig_feature not in X.columns:
                raise ValueError(f"Missing feature column: {orig_feature}")

            # Get the binary features for this original feature
            binary_features = self.feature_mapping_[orig_feature]

            # Create binary columns for each value seen in training
            for binary_feat in binary_features:
                # Extract the value from binary feature name (e.g., "source_ios" -> "ios")
                value = binary_feat[len(orig_feature) + 1:]  # Remove "feature_" prefix

                # Create binary column: 1 if feature equals value, 0 otherwise
                X_encoded[binary_feat] = (X[orig_feature] == value).astype(int)

        return X_encoded

    def _should_stop_splitting(
        self,
        filtered_data: pd.DataFrame,
        available_features: List[str],
        total_samples: int,
        impurity: float,
        depth: int
    ) -> bool:
        """
        Check if we should stop splitting at this node based on all hyperparameters.

        Note: filtered_data is the subset of data for this node (already filtered by mask)
        """
        # Check depth limit
        if self.max_depth is not None and depth >= self.max_depth:
            return True

        # Check minimum samples to split
        if total_samples < self.min_samples_split:
            return True

        # Check minimum samples per leaf (need at least 2 * min_samples_leaf to split)
        if total_samples < 2 * self.min_samples_leaf:
            return True

        # Check if pure node
        if impurity == 0.0:
            return True

        # Check if no features available or limited by max_features
        available_feature_count = len(available_features)
        if available_feature_count == 0:
            return True

        # Apply max_features limitation
        if self.max_features is not None:
            if isinstance(self.max_features, int):
                max_features_to_use = min(self.max_features, available_feature_count)
            elif isinstance(self.max_features, float):
                max_features_to_use = max(1, int(self.max_features * available_feature_count))
            elif self.max_features == "sqrt":
                max_features_to_use = max(1, int(np.sqrt(available_feature_count)))
            elif self.max_features == "log2":
                max_features_to_use = max(1, int(np.log2(available_feature_count)))
            else:
                max_features_to_use = available_feature_count

            if max_features_to_use <= 0:
                return True

        # Check if only one unique combination of features (or too few rows to split meaningfully)
        if len(filtered_data) <= 1:
            return True

        # Check maximum leaf nodes (approximate - would need more sophisticated tracking)
        # For now, we'll skip this complex constraint

        return False

    def predict(self, X: pd.DataFrame) -> np.ndarray:
        """
        Predict classes for samples in X.

        Parameters:
        -----------
        X : DataFrame
            Input samples with original categorical feature columns.

        Returns:
        --------
        predictions : array of shape (n_samples,)
            Predicted class labels (0 or 1).
        """
        if self.tree_ is None:
            raise ValueError("Model has not been fitted yet.")

        # One-hot encode the input data using the same encoding as training
        X_encoded = self._encode_prediction_data(X)

        predictions = []
        for i in range(len(X_encoded)):
            sample_dict = sample_to_dict(X_encoded, i)
            prediction = self.tree_.predict_sample(sample_dict)
            predictions.append(prediction)

        return np.array(predictions)

    def predict_proba(self, X: pd.DataFrame) -> np.ndarray:
        """
        Predict class probabilities for samples in X.

        Parameters:
        -----------
        X : DataFrame
            Input samples with original categorical feature columns.

        Returns:
        --------
        probabilities : array of shape (n_samples, n_classes)
            Predicted class probabilities. Column 0 is bad class,
            column 1 is good class.
        """
        if self.tree_ is None:
            raise ValueError("Model has not been fitted yet.")

        # One-hot encode the input data using the same encoding as training
        X_encoded = self._encode_prediction_data(X)

        probabilities = []
        for i in range(len(X_encoded)):
            sample_dict = sample_to_dict(X_encoded, i)
            prob_bad, prob_good = self.tree_.predict_proba_sample(sample_dict)
            probabilities.append([prob_bad, prob_good])

        return np.array(probabilities)

    def print_tree(self) -> None:
        """Print the tree structure for debugging."""
        if self.tree_ is None:
            print("Tree has not been fitted yet.")
        else:
            print("Decision Tree Structure:")
            print("=" * 50)
            print_tree(self.tree_, self.feature_names_)

    def get_depth(self) -> int:
        """Get the depth of the tree."""
        if self.tree_ is None:
            return 0
        return self._get_node_depth(self.tree_)

    def _get_node_depth(self, node: Union[TreeNode, LeafNode]) -> int:
        """Recursively calculate tree depth."""
        if node.is_leaf():
            return node.depth

        left_depth = 0 if node.left is None else self._get_node_depth(node.left)
        right_depth = 0 if node.right is None else self._get_node_depth(node.right)

        return max(left_depth, right_depth)

    def get_n_leaves(self) -> int:
        """Get the number of leaves in the tree."""
        if self.tree_ is None:
            return 0
        return self._count_leaves(self.tree_)

    def _count_leaves(self, node: Union[TreeNode, LeafNode]) -> int:
        """Recursively count leaves in the tree."""
        if node.is_leaf():
            return 1

        left_count = 0 if node.left is None else self._count_leaves(node.left)
        right_count = 0 if node.right is None else self._count_leaves(node.right)

        return left_count + right_count

    def to_json(self, indent: int = 2) -> str:
        """
        Export the trained tree to JSON format.

        Parameters:
        -----------
        indent : int, default=2
            JSON indentation for pretty printing.

        Returns:
        --------
        json_str : str
            JSON representation of the tree.
        """
        if self.tree_ is None:
            raise ValueError("Model has not been fitted yet.")

        tree_dict = {
            "model_info": {
                "type": "AggregateCART",
                "criterion": self.criterion,
                "max_depth": self.max_depth,
                "min_samples_split": self.min_samples_split,
                "min_samples_leaf": self.min_samples_leaf,
                "min_weight_fraction_leaf": self.min_weight_fraction_leaf,
                "max_features": self.max_features,
                "random_state": self.random_state,
                "max_leaf_nodes": self.max_leaf_nodes,
                "min_impurity_decrease": self.min_impurity_decrease,
                "ccp_alpha": self.ccp_alpha,
                "n_features": self.n_features_,
                "feature_names": self.feature_names_,
                "original_feature_names": self.original_feature_names_,
                "feature_mapping": self.feature_mapping_,
                "classes": self.classes_.tolist(),
                "tree_depth": self.get_depth(),
                "n_leaves": self.get_n_leaves()
            },
            "tree": self._node_to_dict(self.tree_)
        }

        return json.dumps(tree_dict, indent=indent, ensure_ascii=False)

    def _node_to_dict(self, node: Union[TreeNode, LeafNode]) -> Dict[str, Any]:
        """Convert a tree node to dictionary representation."""
        if node.is_leaf():
            return {
                "type": "leaf",
                "prediction": int(node.prediction),
                "class_probabilities": [float(p) for p in node.class_probabilities],
                "samples": int(node.samples),
                "impurity": float(node.impurity),
                "good_count": int(node.good_count),
                "bad_count": int(node.bad_count),
                "depth": int(node.depth)
            }
        else:
            return {
                "type": "internal",
                "feature": node.feature,
                "split_value": node.split_value,
                "split_condition": f"{node.feature} == 1",
                "left_condition": f"{node.feature} == 0 (FALSE/NOT)",
                "right_condition": f"{node.feature} == 1 (TRUE)",
                "samples": int(node.samples),
                "impurity": float(node.impurity),
                "good_count": int(node.good_count),
                "bad_count": int(node.bad_count),
                "depth": int(node.depth),
                "left": self._node_to_dict(node.left) if node.left else None,
                "right": self._node_to_dict(node.right) if node.right else None
            }

    def save_json(self, filepath: str, indent: int = 2) -> None:
        """
        Save the trained tree to a JSON file.

        Parameters:
        -----------
        filepath : str
            Path to save the JSON file.
        indent : int, default=2
            JSON indentation for pretty printing.
        """
        json_str = self.to_json(indent=indent)
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(json_str)

    @classmethod
    def from_json(cls, json_str: str) -> 'AggregateCART':
        """
        Load a trained tree from JSON string.

        Parameters:
        -----------
        json_str : str
            JSON representation of the tree.

        Returns:
        --------
        cart : AggregateCART
            Loaded classifier.
        """
        data = json.loads(json_str)
        model_info = data["model_info"]

        # Create classifier with original parameters
        cart = cls(
            criterion=model_info.get("criterion", "gini"),
            max_depth=model_info["max_depth"],
            min_samples_split=model_info.get("min_samples_split", 2),
            min_samples_leaf=model_info["min_samples_leaf"],
            min_weight_fraction_leaf=model_info.get("min_weight_fraction_leaf", 0.0),
            max_features=model_info.get("max_features", None),
            random_state=model_info.get("random_state", None),
            max_leaf_nodes=model_info.get("max_leaf_nodes", None),
            min_impurity_decrease=model_info["min_impurity_decrease"],
            ccp_alpha=model_info.get("ccp_alpha", 0.0)
        )

        # Restore fitted attributes
        cart.feature_names_ = model_info["feature_names"]
        cart.original_feature_names_ = model_info["original_feature_names"]
        cart.feature_mapping_ = model_info["feature_mapping"]
        cart.n_features_ = model_info["n_features"]
        cart.classes_ = np.array(model_info["classes"])

        # Rebuild tree from dictionary
        cart.tree_ = cart._dict_to_node(data["tree"])

        return cart

    @classmethod
    def load_json(cls, filepath: str) -> 'AggregateCART':
        """
        Load a trained tree from a JSON file.

        Parameters:
        -----------
        filepath : str
            Path to the JSON file.

        Returns:
        --------
        cart : AggregateCART
            Loaded classifier.
        """
        with open(filepath, 'r', encoding='utf-8') as f:
            json_str = f.read()
        return cls.from_json(json_str)

    def _dict_to_node(self, node_dict: Dict[str, Any]) -> Union[TreeNode, LeafNode]:
        """Convert dictionary representation back to tree node."""
        if node_dict["type"] == "leaf":
            leaf = LeafNode(
                good_count=node_dict["good_count"],
                bad_count=node_dict["bad_count"],
                depth=node_dict["depth"]
            )
            return leaf
        else:
            # Create internal node
            internal = TreeNode(
                feature=node_dict["feature"],
                split_value=node_dict["split_value"],
                samples=node_dict["samples"],
                impurity=node_dict["impurity"],
                good_count=node_dict["good_count"],
                bad_count=node_dict["bad_count"],
                depth=node_dict["depth"]
            )

            # Recursively build children
            if node_dict["left"]:
                internal.left = self._dict_to_node(node_dict["left"])
            if node_dict["right"]:
                internal.right = self._dict_to_node(node_dict["right"])

            return internal