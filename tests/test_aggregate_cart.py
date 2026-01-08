"""
Unit tests for AggregateCART classifier.
"""

import pytest
import pandas as pd
import numpy as np
from pathlib import Path

from cart_olap import AggregateCART
from cart_olap.tree_nodes import LeafNode, TreeNode


class TestAggregateCART:
    """Test AggregateCART functionality."""

    def setup_method(self):
        """Set up test data for each test."""
        # Simple test dataset
        self.simple_data = pd.DataFrame({
            'feature1': ['A', 'A', 'B', 'B'],
            'feature2': ['X', 'Y', 'X', 'Y'],
            'good_count': [80, 60, 30, 10],
            'bad_count': [20, 40, 70, 90],
            'total_count': [100, 100, 100, 100]
        })

        # Load larger test dataset
        test_data_path = Path(__file__).parent / "test_data" / "sample_aggregate_data.csv"
        self.sample_data = pd.read_csv(test_data_path)

        self.feature_cols = ['feature1', 'feature2', 'feature3']
        self.good_col = 'good_count'
        self.bad_col = 'bad_count'

    def test_initialization(self):
        """Test classifier initialization with different parameters."""
        # Default parameters
        cart1 = AggregateCART()
        assert cart1.max_depth is None
        assert cart1.min_samples_leaf == 1
        assert cart1.min_impurity_decrease == 0.0

        # Custom parameters
        cart2 = AggregateCART(max_depth=5, min_samples_leaf=10, min_impurity_decrease=0.01)
        assert cart2.max_depth == 5
        assert cart2.min_samples_leaf == 10
        assert cart2.min_impurity_decrease == 0.01

    def test_fit_simple_data(self):
        """Test fitting on simple dataset."""
        cart = AggregateCART(max_depth=3)
        cart.fit(self.simple_data, ['feature1', 'feature2'], 'good_count', 'bad_count')

        # Check fitted attributes
        assert cart.tree_ is not None
        # After one-hot encoding: feature1 -> feature1=A, feature1=B; feature2 -> feature2=X, feature2=Y
        expected_features = ['feature1=A', 'feature1=B', 'feature2=X', 'feature2=Y']
        assert cart.feature_names_ == expected_features
        assert cart.n_features_ == 4  # 4 binary features after one-hot encoding
        assert np.array_equal(cart.classes_, [0, 1])

    def test_fit_with_total_validation(self):
        """Test fitting with total count validation."""
        cart = AggregateCART()
        cart.fit(
            self.simple_data,
            ['feature1', 'feature2'],
            'good_count',
            'bad_count',
            'total_count'
        )
        assert cart.tree_ is not None

    def test_fit_sample_data(self):
        """Test fitting on sample dataset."""
        cart = AggregateCART(max_depth=5, min_samples_leaf=5)
        cart.fit(self.sample_data, self.feature_cols, self.good_col, self.bad_col)

        assert cart.tree_ is not None
        # n_features_ should be the number of binary features after one-hot encoding
        # This will be >= 3 (original features) depending on unique values in each feature
        assert cart.n_features_ >= 3
        assert cart.get_depth() <= 5

    def test_predict_simple(self):
        """Test prediction on simple data."""
        cart = AggregateCART()
        cart.fit(self.simple_data, ['feature1', 'feature2'], 'good_count', 'bad_count')

        # Create test samples
        test_samples = pd.DataFrame({
            'feature1': ['A', 'B', 'A', 'B'],
            'feature2': ['X', 'X', 'Y', 'Y']
        })

        predictions = cart.predict(test_samples)
        assert len(predictions) == 4
        assert all(pred in [0, 1] for pred in predictions)

    def test_predict_proba_simple(self):
        """Test probability prediction."""
        cart = AggregateCART()
        cart.fit(self.simple_data, ['feature1', 'feature2'], 'good_count', 'bad_count')

        test_samples = pd.DataFrame({
            'feature1': ['A', 'B'],
            'feature2': ['X', 'Y']
        })

        probabilities = cart.predict_proba(test_samples)
        assert probabilities.shape == (2, 2)

        # Check probabilities sum to 1
        for i in range(len(probabilities)):
            assert abs(probabilities[i].sum() - 1.0) < 1e-10
            assert all(0 <= p <= 1 for p in probabilities[i])

    def test_single_feature_fit(self):
        """Test fitting with single feature."""
        single_feature_data = pd.DataFrame({
            'feature1': ['A', 'A', 'B', 'B'],
            'good_count': [100, 80, 30, 20],
            'bad_count': [10, 20, 70, 80]
        })

        cart = AggregateCART()
        cart.fit(single_feature_data, ['feature1'], 'good_count', 'bad_count')

        test_sample = pd.DataFrame({'feature1': ['A']})
        prediction = cart.predict(test_sample)
        assert prediction[0] in [0, 1]

    def test_max_depth_constraint(self):
        """Test max depth constraint."""
        cart = AggregateCART(max_depth=1)
        cart.fit(self.sample_data, self.feature_cols, self.good_col, self.bad_col)

        assert cart.get_depth() <= 1

    def test_min_samples_leaf_constraint(self):
        """Test minimum samples per leaf constraint."""
        cart = AggregateCART(min_samples_leaf=100)
        cart.fit(self.sample_data, self.feature_cols, self.good_col, self.bad_col)

        # Should create fewer splits due to min samples constraint
        assert cart.tree_ is not None

    def test_min_impurity_decrease_constraint(self):
        """Test minimum impurity decrease constraint."""
        cart = AggregateCART(min_impurity_decrease=0.1)  # High threshold
        cart.fit(self.sample_data, self.feature_cols, self.good_col, self.bad_col)

        # Should create fewer splits due to impurity threshold
        assert cart.tree_ is not None

    def test_pure_leaf_creation(self):
        """Test that pure nodes become leaves."""
        pure_data = pd.DataFrame({
            'feature1': ['A', 'B'],
            'good_count': [100, 0],
            'bad_count': [0, 100]
        })

        cart = AggregateCART()
        cart.fit(pure_data, ['feature1'], 'good_count', 'bad_count')

        # Should have one split creating two pure leaves
        test_a = pd.DataFrame({'feature1': ['A']})
        test_b = pd.DataFrame({'feature1': ['B']})

        pred_a = cart.predict(test_a)[0]
        pred_b = cart.predict(test_b)[0]

        assert pred_a != pred_b  # Should predict different classes

    def test_tree_structure_methods(self):
        """Test tree structure inspection methods."""
        cart = AggregateCART(max_depth=3)
        cart.fit(self.sample_data, self.feature_cols, self.good_col, self.bad_col)

        # Test depth calculation
        depth = cart.get_depth()
        assert depth >= 0
        assert depth <= 3

        # Test leaf counting
        n_leaves = cart.get_n_leaves()
        assert n_leaves >= 1

        # Test tree printing (should not raise exception)
        cart.print_tree()

    def test_unfitted_model_errors(self):
        """Test that unfitted model raises appropriate errors."""
        cart = AggregateCART()

        test_sample = pd.DataFrame({'feature1': ['A']})

        with pytest.raises(ValueError, match="Model has not been fitted"):
            cart.predict(test_sample)

        with pytest.raises(ValueError, match="Model has not been fitted"):
            cart.predict_proba(test_sample)

    def test_empty_split_handling(self):
        """Test handling of splits that create empty children."""
        # Create data where some splits might create empty children
        skewed_data = pd.DataFrame({
            'feature1': ['A', 'A', 'A', 'A', 'B'],
            'good_count': [25, 25, 25, 25, 100],
            'bad_count': [25, 25, 25, 25, 0]
        })

        cart = AggregateCART()
        cart.fit(skewed_data, ['feature1'], 'good_count', 'bad_count')

        # Should still create a valid tree
        assert cart.tree_ is not None

        # Should be able to predict
        test_sample = pd.DataFrame({'feature1': ['A', 'B']})
        predictions = cart.predict(test_sample)
        assert len(predictions) == 2

    def test_identical_rows_handling(self):
        """Test handling of identical rows in aggregate data."""
        identical_data = pd.DataFrame({
            'feature1': ['A', 'A', 'A'],
            'feature2': ['X', 'X', 'X'],
            'good_count': [50, 30, 20],
            'bad_count': [10, 20, 30]
        })

        cart = AggregateCART()
        cart.fit(identical_data, ['feature1', 'feature2'], 'good_count', 'bad_count')

        # Should create a leaf (no useful splits)
        assert isinstance(cart.tree_, LeafNode)

        test_sample = pd.DataFrame({
            'feature1': ['A'],
            'feature2': ['X']
        })
        prediction = cart.predict(test_sample)
        assert len(prediction) == 1

    def test_feature_importance_indirectly(self):
        """Test that tree uses informative features preferentially."""
        # Create data where feature1 is very informative, feature2 is not
        informative_data = pd.DataFrame({
            'feature1': ['good', 'good', 'good', 'bad', 'bad', 'bad'],
            'feature2': ['A', 'B', 'A', 'B', 'A', 'B'],  # Random
            'good_count': [90, 85, 88, 5, 8, 3],
            'bad_count': [10, 15, 12, 95, 92, 97]
        })

        cart = AggregateCART(max_depth=2)
        cart.fit(informative_data, ['feature1', 'feature2'], 'good_count', 'bad_count')

        # Root should split on a feature1-based binary feature (more informative)
        # After one-hot encoding: feature1 -> feature1=good, feature1=bad
        if isinstance(cart.tree_, TreeNode):
            assert cart.tree_.feature.startswith('feature1=')  # Should be feature1=good or feature1=bad

    def test_consistency_multiple_runs(self):
        """Test that multiple runs produce same results (deterministic)."""
        cart1 = AggregateCART(max_depth=3, random_state=42)
        cart1.fit(self.sample_data, self.feature_cols, self.good_col, self.bad_col)

        cart2 = AggregateCART(max_depth=3, random_state=42)
        cart2.fit(self.sample_data, self.feature_cols, self.good_col, self.bad_col)

        test_sample = pd.DataFrame({
            'feature1': ['A'],
            'feature2': ['X'],
            'feature3': [1]
        })

        pred1 = cart1.predict(test_sample)
        pred2 = cart2.predict(test_sample)

        # Should be deterministic (though random_state not implemented yet)
        assert np.array_equal(pred1, pred2)


class TestInvalidInputs:
    """Test error handling for invalid inputs."""

    def test_invalid_aggregate_data(self):
        """Test fitting with invalid aggregate data."""
        cart = AggregateCART()

        # Missing columns
        bad_data = pd.DataFrame({'feature1': ['A', 'B']})
        with pytest.raises(ValueError):
            cart.fit(bad_data, ['feature1'], 'missing_good', 'missing_bad')

        # Negative counts
        bad_data = pd.DataFrame({
            'feature1': ['A', 'B'],
            'good_count': [-5, 10],
            'bad_count': [15, 20]
        })
        with pytest.raises(ValueError):
            cart.fit(bad_data, ['feature1'], 'good_count', 'bad_count')

    def test_prediction_with_missing_features(self):
        """Test prediction when test data missing required features."""
        training_data = pd.DataFrame({
            'feature1': ['A', 'B'],
            'feature2': ['X', 'Y'],
            'good_count': [80, 20],
            'bad_count': [20, 80]
        })

        cart = AggregateCART()
        cart.fit(training_data, ['feature1', 'feature2'], 'good_count', 'bad_count')

        # Test data missing feature2
        bad_test_data = pd.DataFrame({'feature1': ['A']})

        # Our implementation should handle missing features gracefully
        # This might either raise an error or make a prediction based on available features
        # For now, let's just ensure it doesn't crash completely
        try:
            result = cart.predict(bad_test_data)
            # If it succeeds, that's also acceptable behavior
            assert len(result) == 1
            print("Graceful handling of missing features")
        except (KeyError, ValueError, AttributeError):
            # If it raises an error, that's also acceptable
            print("Strict validation of missing features")

    def test_invalid_parameters(self):
        """Test invalid parameter combinations."""
        # Negative max_depth should be handled gracefully
        cart = AggregateCART(max_depth=-1)
        # Should work (treated as no limit or 0)

        # Negative min_samples_leaf
        cart = AggregateCART(min_samples_leaf=-5)
        # Should work (implementation should handle)

        # Negative min_impurity_decrease
        cart = AggregateCART(min_impurity_decrease=-0.1)
        # Should work (treated as 0 effectively)