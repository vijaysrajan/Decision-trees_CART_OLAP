"""
Utility functions for CART decision tree implementation.

This module contains helper functions for:
- Impurity calculations
- Data validation
- Tree operations
"""

from typing import List, Tuple, Any
import pandas as pd
import numpy as np


def compute_gini_impurity(good_count: int, bad_count: int) -> float:
    """
    Compute Gini impurity from good and bad counts.

    Gini impurity = 1 - (p_good^2 + p_bad^2)

    Args:
        good_count: Number of good class samples
        bad_count: Number of bad class samples

    Returns:
        Gini impurity (0.0 for pure nodes, 0.5 for maximum impurity)
    """
    total = good_count + bad_count
    if total == 0:
        return 0.0

    p_good = good_count / total
    p_bad = bad_count / total

    return 1 - (p_good**2 + p_bad**2)


def compute_weighted_impurity(
    left_good: int,
    left_bad: int,
    right_good: int,
    right_bad: int
) -> float:
    """
    Compute weighted impurity of child nodes after a split.

    Args:
        left_good: Good count in left child
        left_bad: Bad count in left child
        right_good: Good count in right child
        right_bad: Bad count in right child

    Returns:
        Weighted average impurity of child nodes
    """
    left_total = left_good + left_bad
    right_total = right_good + right_bad
    total = left_total + right_total

    if total == 0:
        return 0.0

    left_weight = left_total / total
    right_weight = right_total / total

    left_impurity = compute_gini_impurity(left_good, left_bad)
    right_impurity = compute_gini_impurity(right_good, right_bad)

    return left_weight * left_impurity + right_weight * right_impurity


def information_gain(
    parent_good: int,
    parent_bad: int,
    left_good: int,
    left_bad: int,
    right_good: int,
    right_bad: int
) -> float:
    """
    Compute information gain from a split.

    Information Gain = Parent Impurity - Weighted Child Impurity

    Args:
        parent_good: Good count in parent node
        parent_bad: Bad count in parent node
        left_good: Good count in left child
        left_bad: Bad count in left child
        right_good: Good count in right child
        right_bad: Bad count in right child

    Returns:
        Information gain (higher is better)
    """
    parent_impurity = compute_gini_impurity(parent_good, parent_bad)
    child_impurity = compute_weighted_impurity(left_good, left_bad, right_good, right_bad)

    return parent_impurity - child_impurity


def validate_aggregate_data(
    df: pd.DataFrame,
    feature_cols: List[str],
    good_col: str,
    bad_col: str,
    total_col: str = None
) -> None:
    """
    Validate aggregate data format and contents.

    Args:
        df: Input DataFrame
        feature_cols: List of feature column names
        good_col: Good count column name
        bad_col: Bad count column name
        total_col: Optional total count column for validation

    Raises:
        ValueError: If data format is invalid
    """
    # Check required columns exist
    required_cols = feature_cols + [good_col, bad_col]
    missing_cols = [col for col in required_cols if col not in df.columns]
    if missing_cols:
        raise ValueError(f"Missing required columns: {missing_cols}")

    # Check for non-negative counts
    if (df[good_col] < 0).any():
        raise ValueError(f"Good count column '{good_col}' contains negative values")

    if (df[bad_col] < 0).any():
        raise ValueError(f"Bad count column '{bad_col}' contains negative values")

    # Check for missing values in feature columns
    for col in feature_cols:
        if df[col].isnull().any():
            raise ValueError(f"Feature column '{col}' contains missing values")

    # Validate total count if provided
    if total_col and total_col in df.columns:
        computed_total = df[good_col] + df[bad_col]
        if not np.allclose(df[total_col], computed_total, atol=1e-6):
            mismatches = ~np.isclose(df[total_col], computed_total, atol=1e-6)
            n_mismatches = mismatches.sum()
            raise ValueError(
                f"Total count validation failed for {n_mismatches} rows. "
                f"Expected {total_col} = {good_col} + {bad_col}"
            )

    # Check for empty dataset (check this before missing columns)
    if len(df) == 0:
        if not missing_cols:  # Only if columns would otherwise be valid
            raise ValueError("Dataset is empty")
        else:
            raise ValueError(f"Missing required columns: {missing_cols}")  # Missing cols takes precedence

    # Check for zero total counts
    total_counts = df[good_col] + df[bad_col]
    zero_count_rows = (total_counts == 0).sum()
    if zero_count_rows > 0:
        raise ValueError(f"Found {zero_count_rows} rows with zero total counts")


def sample_to_dict(sample: pd.DataFrame, row_idx: int = 0) -> dict:
    """
    Convert a pandas DataFrame row to a dictionary for prediction.

    Args:
        sample: DataFrame with feature columns
        row_idx: Row index to convert (default: 0)

    Returns:
        Dictionary with feature names as keys and values
    """
    return sample.iloc[row_idx].to_dict()


def print_tree(node, feature_names: List[str] = None, indent: str = "") -> None:
    """
    Print tree structure for debugging.

    Args:
        node: Root node of tree or subtree
        feature_names: List of feature names for display
        indent: Current indentation string
    """
    info = node.get_info()

    if node.is_leaf():
        print(f"{indent}Leaf: prediction={info['prediction']}, "
              f"samples={info['samples']}, "
              f"distribution={info['class_distribution']}, "
              f"impurity={info['impurity']:.3f}")
    else:
        print(f"{indent}Split: {info['feature']} == {info['split_value']}, "
              f"samples={info['samples']}, "
              f"distribution={info['class_distribution']}, "
              f"impurity={info['impurity']:.3f}")

        if node.left:
            print(f"{indent}├── False:")
            print_tree(node.left, feature_names, indent + "│   ")

        if node.right:
            print(f"{indent}└── True:")
            print_tree(node.right, feature_names, indent + "    ")