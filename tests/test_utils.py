"""
Unit tests for utility functions.
"""

import pytest
import pandas as pd
import numpy as np
from cart_olap.utils import (
    compute_gini_impurity,
    compute_weighted_impurity,
    information_gain,
    validate_aggregate_data,
    sample_to_dict
)


class TestGiniImpurity:
    """Test Gini impurity calculations."""

    def test_pure_good_node(self):
        """Test Gini impurity for pure good node."""
        impurity = compute_gini_impurity(100, 0)
        assert impurity == 0.0

    def test_pure_bad_node(self):
        """Test Gini impurity for pure bad node."""
        impurity = compute_gini_impurity(0, 100)
        assert impurity == 0.0

    def test_balanced_node(self):
        """Test Gini impurity for balanced node."""
        impurity = compute_gini_impurity(50, 50)
        assert impurity == 0.5

    def test_empty_node(self):
        """Test Gini impurity for empty node."""
        impurity = compute_gini_impurity(0, 0)
        assert impurity == 0.0

    def test_imbalanced_node(self):
        """Test Gini impurity for imbalanced node."""
        impurity = compute_gini_impurity(80, 20)
        expected = 1 - (0.8**2 + 0.2**2)  # 1 - (0.64 + 0.04) = 0.32
        assert abs(impurity - expected) < 1e-10


class TestWeightedImpurity:
    """Test weighted impurity calculations."""

    def test_balanced_split(self):
        """Test weighted impurity for balanced split."""
        weighted_imp = compute_weighted_impurity(25, 25, 25, 25)
        # Both children have impurity = 0.5, weighted average = 0.5
        assert weighted_imp == 0.5

    def test_pure_children(self):
        """Test weighted impurity with pure children."""
        weighted_imp = compute_weighted_impurity(100, 0, 0, 100)
        # Both children are pure, weighted average = 0
        assert weighted_imp == 0.0

    def test_empty_split(self):
        """Test weighted impurity with empty data."""
        weighted_imp = compute_weighted_impurity(0, 0, 0, 0)
        assert weighted_imp == 0.0


class TestInformationGain:
    """Test information gain calculations."""

    def test_perfect_split(self):
        """Test information gain for perfect split."""
        # Parent: mixed, children: pure
        gain = information_gain(50, 50, 50, 0, 0, 50)
        # Parent impurity = 0.5, child impurity = 0
        assert gain == 0.5

    def test_no_improvement_split(self):
        """Test information gain for useless split."""
        # Parent and children have same distribution
        gain = information_gain(50, 50, 25, 25, 25, 25)
        # All impurities are 0.5
        assert gain == 0.0

    def test_negative_gain_impossible(self):
        """Test that information gain cannot be negative."""
        # Any valid split should have non-negative gain
        gain = information_gain(60, 40, 30, 20, 30, 20)
        assert gain >= 0


class TestDataValidation:
    """Test data validation functions."""

    def setup_method(self):
        """Set up test data."""
        self.valid_data = pd.DataFrame({
            'feature1': ['A', 'A', 'B', 'B'],
            'feature2': ['X', 'Y', 'X', 'Y'],
            'good_count': [100, 80, 60, 40],
            'bad_count': [20, 40, 30, 50],
            'total_count': [120, 120, 90, 90]
        })

    def test_valid_data(self):
        """Test validation with valid data."""
        # Should not raise any exception
        validate_aggregate_data(
            self.valid_data,
            ['feature1', 'feature2'],
            'good_count',
            'bad_count',
            'total_count'
        )

    def test_missing_feature_column(self):
        """Test validation with missing feature column."""
        with pytest.raises(ValueError, match="Missing required columns"):
            validate_aggregate_data(
                self.valid_data,
                ['feature1', 'missing_feature'],
                'good_count',
                'bad_count'
            )

    def test_missing_count_column(self):
        """Test validation with missing count column."""
        with pytest.raises(ValueError, match="Missing required columns"):
            validate_aggregate_data(
                self.valid_data,
                ['feature1'],
                'missing_good',
                'bad_count'
            )

    def test_negative_counts(self):
        """Test validation with negative counts."""
        bad_data = self.valid_data.copy()
        bad_data.loc[0, 'good_count'] = -10

        with pytest.raises(ValueError, match="contains negative values"):
            validate_aggregate_data(
                bad_data,
                ['feature1', 'feature2'],
                'good_count',
                'bad_count'
            )

    def test_null_feature_values(self):
        """Test validation with null feature values."""
        bad_data = self.valid_data.copy()
        bad_data.loc[0, 'feature1'] = None

        with pytest.raises(ValueError, match="contains missing values"):
            validate_aggregate_data(
                bad_data,
                ['feature1', 'feature2'],
                'good_count',
                'bad_count'
            )

    def test_total_count_mismatch(self):
        """Test validation with incorrect total count."""
        bad_data = self.valid_data.copy()
        bad_data.loc[0, 'total_count'] = 999  # Should be 120

        with pytest.raises(ValueError, match="Total count validation failed"):
            validate_aggregate_data(
                bad_data,
                ['feature1', 'feature2'],
                'good_count',
                'bad_count',
                'total_count'
            )

    def test_empty_dataset(self):
        """Test validation with empty dataset."""
        empty_data = pd.DataFrame()

        # Empty dataframe will first fail on missing columns
        with pytest.raises(ValueError, match="Missing required columns"):
            validate_aggregate_data(
                empty_data,
                ['feature1'],
                'good_count',
                'bad_count'
            )

    def test_zero_total_counts(self):
        """Test validation with zero total counts."""
        bad_data = self.valid_data.copy()
        bad_data.loc[0, 'good_count'] = 0
        bad_data.loc[0, 'bad_count'] = 0

        with pytest.raises(ValueError, match="zero total counts"):
            validate_aggregate_data(
                bad_data,
                ['feature1', 'feature2'],
                'good_count',
                'bad_count'
            )


class TestSampleToDict:
    """Test sample conversion utility."""

    def test_sample_conversion(self):
        """Test converting DataFrame row to dictionary."""
        df = pd.DataFrame({
            'feature1': ['A', 'B'],
            'feature2': [1, 2],
            'feature3': ['X', 'Y']
        })

        # Test first row
        result = sample_to_dict(df, 0)
        expected = {'feature1': 'A', 'feature2': 1, 'feature3': 'X'}
        assert result == expected

        # Test second row
        result = sample_to_dict(df, 1)
        expected = {'feature1': 'B', 'feature2': 2, 'feature3': 'Y'}
        assert result == expected

    def test_default_row_index(self):
        """Test default row index (0)."""
        df = pd.DataFrame({
            'feature1': ['A', 'B'],
            'feature2': [1, 2]
        })

        result = sample_to_dict(df)
        expected = {'feature1': 'A', 'feature2': 1}
        assert result == expected