"""
Tree node data structures for CART decision tree.

This module defines the node classes used in the decision tree:
- TreeNode: Internal nodes with split conditions
- LeafNode: Terminal nodes with class predictions
"""

from typing import Any, Dict, Optional, Union
import pandas as pd


class TreeNode:
    """
    Internal tree node representing a decision point.

    Attributes:
        feature: Name of the feature to split on
        split_value: Value used for binary split (feature == split_value)
        left: Left child node (when feature != split_value)
        right: Right child node (when feature == split_value)
        samples: Total number of samples (sum of good + bad counts)
        impurity: Gini impurity of this node
        good_count: Total good class samples in this node
        bad_count: Total bad class samples in this node
        depth: Depth of this node in the tree (root = 0)
    """

    def __init__(
        self,
        feature: str,
        split_value: Any,
        samples: int,
        impurity: float,
        good_count: int,
        bad_count: int,
        depth: int = 0
    ):
        self.feature = feature
        self.split_value = split_value
        self.left: Optional[Union['TreeNode', 'LeafNode']] = None
        self.right: Optional[Union['TreeNode', 'LeafNode']] = None
        self.samples = samples
        self.impurity = impurity
        self.good_count = good_count
        self.bad_count = bad_count
        self.depth = depth

    def is_leaf(self) -> bool:
        """Check if this is a leaf node."""
        return False

    def predict_sample(self, sample: Dict[str, Any]) -> int:
        """
        Predict class for a single sample by traversing the tree.

        Args:
            sample: Dictionary with feature names as keys

        Returns:
            Predicted class (0 for bad, 1 for good)
        """
        # Binary split: feature=True (right) vs feature=False (left)
        # This matches the theta sketches approach: column=value vs column!=value
        if sample.get(self.feature, 0) == 1:  # feature=True (present)
            return self.right.predict_sample(sample)
        else:  # feature=False (absent)
            return self.left.predict_sample(sample)

    def predict_proba_sample(self, sample: Dict[str, Any]) -> tuple:
        """
        Predict class probabilities for a single sample.

        Args:
            sample: Dictionary with feature names as keys

        Returns:
            Tuple of (prob_bad, prob_good)
        """
        # Binary split: feature=True (right) vs feature=False (left)
        # This matches the theta sketches approach: column=value vs column!=value
        if sample.get(self.feature, 0) == 1:  # feature=True (present)
            return self.right.predict_proba_sample(sample)
        else:  # feature=False (absent)
            return self.left.predict_proba_sample(sample)

    def get_info(self) -> Dict[str, Any]:
        """Get node information for debugging/visualization."""
        return {
            'type': 'internal',
            'feature': self.feature,
            'split_value': self.split_value,
            'samples': self.samples,
            'impurity': round(self.impurity, 4),
            'good_count': self.good_count,
            'bad_count': self.bad_count,
            'depth': self.depth,
            'class_distribution': [self.bad_count, self.good_count]
        }


class LeafNode:
    """
    Leaf tree node representing a final prediction.

    Attributes:
        prediction: Predicted class (0 for bad, 1 for good)
        class_probabilities: Tuple of (prob_bad, prob_good)
        samples: Total number of samples in this leaf
        impurity: Gini impurity of this leaf (should be 0 for pure leaves)
        good_count: Total good class samples in this leaf
        bad_count: Total bad class samples in this leaf
        depth: Depth of this leaf in the tree
    """

    def __init__(
        self,
        good_count: int,
        bad_count: int,
        depth: int = 0
    ):
        self.good_count = good_count
        self.bad_count = bad_count
        self.samples = good_count + bad_count
        self.depth = depth

        # Determine prediction (majority class)
        if good_count >= bad_count:
            self.prediction = 1  # Good class
        else:
            self.prediction = 0  # Bad class

        # Calculate class probabilities
        if self.samples > 0:
            prob_good = good_count / self.samples
            prob_bad = bad_count / self.samples
        else:
            prob_good = 0.5
            prob_bad = 0.5

        self.class_probabilities = (prob_bad, prob_good)

        # Calculate impurity
        self.impurity = 1 - (prob_good**2 + prob_bad**2)

    def is_leaf(self) -> bool:
        """Check if this is a leaf node."""
        return True

    def predict_sample(self, sample: Dict[str, Any]) -> int:
        """
        Predict class for a single sample.

        Args:
            sample: Dictionary with feature names as keys (unused for leaf)

        Returns:
            Predicted class (0 for bad, 1 for good)
        """
        return self.prediction

    def predict_proba_sample(self, sample: Dict[str, Any]) -> tuple:
        """
        Predict class probabilities for a single sample.

        Args:
            sample: Dictionary with feature names as keys (unused for leaf)

        Returns:
            Tuple of (prob_bad, prob_good)
        """
        return self.class_probabilities

    def get_info(self) -> Dict[str, Any]:
        """Get node information for debugging/visualization."""
        return {
            'type': 'leaf',
            'prediction': self.prediction,
            'class_probabilities': [round(p, 4) for p in self.class_probabilities],
            'samples': self.samples,
            'impurity': round(self.impurity, 4),
            'good_count': self.good_count,
            'bad_count': self.bad_count,
            'depth': self.depth,
            'class_distribution': [self.bad_count, self.good_count]
        }