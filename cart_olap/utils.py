"""
Utility functions for CART decision tree implementation.

This module contains helper functions for:
- Impurity calculations
- Data validation
- Tree operations
"""

from typing import List, Tuple, Any, Optional
import pandas as pd
import numpy as np
from scipy.stats import beta, binom, chi2_contingency
import math


def compute_entropy_impurity(good_count: int, bad_count: int) -> float:
    """
    Compute entropy (information) impurity from good and bad counts.

    Entropy = -p_good * log2(p_good) - p_bad * log2(p_bad)

    Args:
        good_count: Number of good class samples
        bad_count: Number of bad class samples

    Returns:
        Entropy impurity (0.0 for pure nodes, 1.0 for maximum impurity)
    """
    total = good_count + bad_count
    if total == 0:
        return 0.0

    p_good = good_count / total
    p_bad = bad_count / total

    entropy = 0.0
    if p_good > 0:
        entropy -= p_good * np.log2(p_good)
    if p_bad > 0:
        entropy -= p_bad * np.log2(p_bad)

    return entropy


def compute_log_loss_impurity(good_count: int, bad_count: int) -> float:
    """
    Compute log loss (cross-entropy) impurity from good and bad counts.

    Log loss = -p_good * ln(p_good) - p_bad * ln(p_bad)

    Args:
        good_count: Number of good class samples
        bad_count: Number of bad class samples

    Returns:
        Log loss impurity (0.0 for pure nodes)
    """
    total = good_count + bad_count
    if total == 0:
        return 0.0

    p_good = good_count / total
    p_bad = bad_count / total

    log_loss = 0.0
    if p_good > 0:
        log_loss -= p_good * np.log(p_good)
    if p_bad > 0:
        log_loss -= p_bad * np.log(p_bad)

    return log_loss


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


def compute_impurity(good_count: int, bad_count: int, criterion: str = "gini") -> float:
    """
    Compute impurity based on specified criterion.

    Args:
        good_count: Number of good class samples
        bad_count: Number of bad class samples
        criterion: Impurity criterion ("gini", "entropy", or "log_loss")

    Returns:
        Impurity value based on criterion
    """
    if criterion == "gini":
        return compute_gini_impurity(good_count, bad_count)
    elif criterion == "entropy":
        return compute_entropy_impurity(good_count, bad_count)
    elif criterion == "log_loss":
        return compute_log_loss_impurity(good_count, bad_count)
    else:
        raise ValueError(f"Unknown criterion: {criterion}")


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
    Compute information gain from a split using Gini impurity.

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


def compute_binomial_confidence_interval(
    good_count: int,
    total_count: int,
    confidence_level: float = 0.95
) -> Tuple[float, float]:
    """
    Compute binomial confidence interval for success probability.

    Uses the beta distribution to compute exact confidence intervals
    for binomial proportions (Clopper-Pearson interval).

    Args:
        good_count: Number of successes (good class samples)
        total_count: Total number of trials
        confidence_level: Confidence level (default: 0.95)

    Returns:
        Tuple of (lower_bound, upper_bound) for success probability
    """
    if total_count == 0:
        return 0.0, 0.0

    if good_count == 0:
        # Special case: no successes
        alpha = 1 - confidence_level
        upper_bound = 1 - (alpha / 2) ** (1 / total_count)
        return 0.0, upper_bound

    if good_count == total_count:
        # Special case: all successes
        alpha = 1 - confidence_level
        lower_bound = (alpha / 2) ** (1 / total_count)
        return lower_bound, 1.0

    # General case: use beta distribution
    alpha = 1 - confidence_level
    lower_bound = beta.ppf(alpha / 2, good_count, total_count - good_count + 1)
    upper_bound = beta.ppf(1 - alpha / 2, good_count + 1, total_count - good_count)

    return lower_bound, upper_bound


def compute_wilson_score_interval(
    good_count: int,
    total_count: int,
    confidence_level: float = 0.95
) -> Tuple[float, float]:
    """
    Compute Wilson score confidence interval for binomial proportion.

    The Wilson score interval is more reliable than the normal approximation
    for small sample sizes or extreme proportions.

    Args:
        good_count: Number of successes
        total_count: Total number of trials
        confidence_level: Confidence level (default: 0.95)

    Returns:
        Tuple of (lower_bound, upper_bound) for success probability
    """
    if total_count == 0:
        return 0.0, 0.0

    # Z-score for the given confidence level
    from scipy.stats import norm
    alpha = 1 - confidence_level
    z = norm.ppf(1 - alpha / 2)

    p = good_count / total_count
    n = total_count

    # Wilson score formula
    center = (p + z**2 / (2*n)) / (1 + z**2 / n)
    margin = z * math.sqrt(p*(1-p)/n + z**2/(4*n**2)) / (1 + z**2 / n)

    lower_bound = max(0.0, center - margin)
    upper_bound = min(1.0, center + margin)

    return lower_bound, upper_bound


def compute_statistical_significance(
    left_good: int,
    left_bad: int,
    right_good: int,
    right_bad: int,
    alpha: float = 0.05
) -> Tuple[bool, float]:
    """
    Test if the difference in success rates between left and right children is statistically significant.

    Uses chi-squared test of independence to test if the split creates
    statistically different distributions.

    Args:
        left_good: Good count in left child
        left_bad: Bad count in left child
        right_good: Good count in right child
        right_bad: Bad count in right child
        alpha: Significance level (default: 0.05)

    Returns:
        Tuple of (is_significant, p_value)
    """
    # Create contingency table
    contingency_table = np.array([
        [left_good, left_bad],
        [right_good, right_bad]
    ])

    # Check if we have enough samples for chi-squared test
    if np.any(contingency_table < 5):
        # Use Fisher's exact test for small samples (approximation)
        from scipy.stats import fisher_exact
        _, p_value = fisher_exact(contingency_table)
        return p_value < alpha, p_value
    else:
        # Use chi-squared test
        _, p_value, _, _ = chi2_contingency(contingency_table)
        return p_value < alpha, p_value


def compute_entropy_reduction(
    parent_good: int,
    parent_bad: int,
    left_good: int,
    left_bad: int,
    right_good: int,
    right_bad: int
) -> float:
    """
    Compute entropy reduction (information gain) with entropy criterion.

    Args:
        parent_good: Good count in parent node
        parent_bad: Bad count in parent node
        left_good: Good count in left child
        left_bad: Bad count in left child
        right_good: Good count in right child
        right_bad: Bad count in right child

    Returns:
        Entropy reduction (information gain)
    """
    total_samples = parent_good + parent_bad
    left_total = left_good + left_bad
    right_total = right_good + right_bad

    if total_samples == 0:
        return 0.0

    # Parent entropy
    parent_entropy = compute_entropy_impurity(parent_good, parent_bad)

    # Weighted child entropy
    left_weight = left_total / total_samples
    right_weight = right_total / total_samples

    left_entropy = compute_entropy_impurity(left_good, left_bad)
    right_entropy = compute_entropy_impurity(right_good, right_bad)

    weighted_child_entropy = left_weight * left_entropy + right_weight * right_entropy

    return parent_entropy - weighted_child_entropy


def compute_split_quality_metrics(
    parent_good: int,
    parent_bad: int,
    left_good: int,
    left_bad: int,
    right_good: int,
    right_bad: int,
    criterion: str = "gini"
) -> dict:
    """
    Compute comprehensive quality metrics for a split.

    Args:
        parent_good: Good count in parent node
        parent_bad: Bad count in parent node
        left_good: Good count in left child
        left_bad: Bad count in left child
        right_good: Good count in right child
        right_bad: Bad count in right child
        criterion: Impurity criterion to use

    Returns:
        Dictionary with various quality metrics
    """
    total_samples = parent_good + parent_bad
    left_total = left_good + left_bad
    right_total = right_good + right_bad

    metrics = {
        'information_gain': 0.0,
        'gini_gain': 0.0,
        'entropy_gain': 0.0,
        'parent_impurity': 0.0,
        'left_impurity': 0.0,
        'right_impurity': 0.0,
        'weighted_child_impurity': 0.0,
        'is_statistically_significant': False,
        'p_value': 1.0,
        'left_confidence_interval': (0.0, 0.0),
        'right_confidence_interval': (0.0, 0.0),
        'split_balance': 0.0  # Measure of how balanced the split is
    }

    if total_samples == 0:
        return metrics

    # Impurity calculations
    metrics['parent_impurity'] = compute_impurity(parent_good, parent_bad, criterion)
    metrics['left_impurity'] = compute_impurity(left_good, left_bad, criterion)
    metrics['right_impurity'] = compute_impurity(right_good, right_bad, criterion)

    # Information gain for different criteria
    metrics['gini_gain'] = information_gain(
        parent_good, parent_bad, left_good, left_bad, right_good, right_bad
    )
    metrics['entropy_gain'] = compute_entropy_reduction(
        parent_good, parent_bad, left_good, left_bad, right_good, right_bad
    )

    # Use the specified criterion for the main gain
    if criterion == "gini":
        metrics['information_gain'] = metrics['gini_gain']
    elif criterion == "entropy":
        metrics['information_gain'] = metrics['entropy_gain']
    elif criterion == "log_loss":
        # For log_loss, use the same calculation as entropy but with natural log
        metrics['information_gain'] = metrics['entropy_gain']  # Approximation

    # Weighted child impurity
    left_weight = left_total / total_samples
    right_weight = right_total / total_samples
    metrics['weighted_child_impurity'] = (
        left_weight * metrics['left_impurity'] +
        right_weight * metrics['right_impurity']
    )

    # Statistical significance
    is_sig, p_val = compute_statistical_significance(
        left_good, left_bad, right_good, right_bad
    )
    metrics['is_statistically_significant'] = is_sig
    metrics['p_value'] = p_val

    # Confidence intervals
    metrics['left_confidence_interval'] = compute_wilson_score_interval(
        left_good, left_total
    )
    metrics['right_confidence_interval'] = compute_wilson_score_interval(
        right_good, right_total
    )

    # Split balance (0.5 = perfectly balanced, 0 = completely unbalanced)
    if total_samples > 0:
        balance = min(left_total, right_total) / total_samples
        metrics['split_balance'] = balance

    return metrics


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