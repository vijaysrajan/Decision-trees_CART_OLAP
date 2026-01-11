"""
Comprehensive tests for different split criteria in AggregateCART.

Tests gini, entropy, and log_loss criteria for:
- Initialization validation
- Impurity computation accuracy
- Model training and predictions
- Criterion-specific tree characteristics
- Performance comparison across criteria
"""

import pytest
import pandas as pd
import numpy as np
from pathlib import Path
import tempfile
import json

from cart_olap import AggregateCART
from cart_olap.utils import (
    compute_gini_impurity,
    compute_entropy_impurity,
    compute_log_loss_impurity,
    compute_impurity
)


class TestSplitCriteria:
    """Test different split criteria functionality."""

    def setup_method(self):
        """Set up test data for each test."""
        # Test dataset with clear patterns for different criteria
        self.test_data = pd.DataFrame({
            'source': ['ios', 'android', 'ios', 'android', 'website', 'website'],
            'city': ['Mumbai', 'Delhi', 'Mumbai', 'Delhi', 'Mumbai', 'Delhi'],
            'time': ['morning', 'evening', 'evening', 'morning', 'morning', 'evening'],
            'good_count': [90, 60, 70, 80, 40, 30],
            'bad_count': [10, 40, 30, 20, 60, 70],
        })

        self.feature_cols = ['source', 'city', 'time']
        self.good_col = 'good_count'
        self.bad_col = 'bad_count'

        # Load larger dataset for realistic testing
        test_data_path = Path(__file__).parent / "test_data" / "sample_aggregate_data.csv"
        if test_data_path.exists():
            self.sample_data = pd.read_csv(test_data_path)
        else:
            # Fallback if test data doesn't exist
            self.sample_data = self.test_data

    def test_criterion_initialization(self):
        """Test classifier initialization with different criteria."""
        # Valid criteria
        for criterion in ['gini', 'entropy', 'log_loss']:
            cart = AggregateCART(criterion=criterion)
            assert cart.criterion == criterion

        # Invalid criterion should raise error
        with pytest.raises(ValueError, match="criterion must be"):
            AggregateCART(criterion='invalid')

    def test_impurity_computation_accuracy(self):
        """Test accuracy of impurity computation for each criterion."""
        # Test case: 60 good, 40 bad (total 100)
        good, bad = 60, 40
        total = good + bad

        # Test gini impurity
        gini = compute_gini_impurity(good, bad)
        expected_gini = 1 - (0.6**2 + 0.4**2)  # 1 - (0.36 + 0.16) = 0.48
        assert abs(gini - expected_gini) < 1e-10

        # Test entropy impurity
        entropy = compute_entropy_impurity(good, bad)
        expected_entropy = -(0.6 * np.log2(0.6) + 0.4 * np.log2(0.4))
        assert abs(entropy - expected_entropy) < 1e-10

        # Test log_loss impurity
        log_loss = compute_log_loss_impurity(good, bad)
        expected_log_loss = -(0.6 * np.log(0.6) + 0.4 * np.log(0.4))
        assert abs(log_loss - expected_log_loss) < 1e-10

        # Test perfect purity (should be 0 for all criteria)
        assert compute_gini_impurity(100, 0) == 0.0
        assert compute_entropy_impurity(100, 0) == 0.0
        assert compute_log_loss_impurity(100, 0) == 0.0

        # Test maximum impurity (50/50 split)
        assert abs(compute_gini_impurity(50, 50) - 0.5) < 1e-10
        assert abs(compute_entropy_impurity(50, 50) - 1.0) < 1e-10

    def test_compute_impurity_dispatcher(self):
        """Test the main compute_impurity function with different criteria."""
        good, bad = 70, 30

        # Test each criterion through dispatcher
        gini_result = compute_impurity(good, bad, "gini")
        entropy_result = compute_impurity(good, bad, "entropy")
        log_loss_result = compute_impurity(good, bad, "log_loss")

        # Should match individual functions
        assert gini_result == compute_gini_impurity(good, bad)
        assert entropy_result == compute_entropy_impurity(good, bad)
        assert log_loss_result == compute_log_loss_impurity(good, bad)

        # Invalid criterion should raise error
        with pytest.raises(ValueError, match="Unknown criterion"):
            compute_impurity(good, bad, "invalid")

    def test_model_training_with_different_criteria(self):
        """Test that models train successfully with all criteria."""
        for criterion in ['gini', 'entropy', 'log_loss']:
            # Initialize model with criterion
            cart = AggregateCART(
                criterion=criterion,
                max_depth=3,
                min_samples_leaf=1,
                random_state=42
            )

            # Fit model
            cart.fit(self.test_data, self.feature_cols, self.good_col, self.bad_col)

            # Check that model is fitted
            assert hasattr(cart, 'tree_')
            assert cart.tree_ is not None

            # Test predictions
            predictions = cart.predict(self.test_data[self.feature_cols])
            probabilities = cart.predict_proba(self.test_data[self.feature_cols])

            # Validate prediction shapes
            assert len(predictions) == len(self.test_data)
            assert probabilities.shape == (len(self.test_data), 2)

            # Validate prediction values
            assert all(pred in [0, 1] for pred in predictions)
            assert all(0 <= prob <= 1 for row in probabilities for prob in row)
            assert all(abs(sum(row) - 1.0) < 1e-10 for row in probabilities)

    def test_criterion_affects_tree_structure(self):
        """Test that different criteria can produce different tree structures."""
        models = {}

        for criterion in ['gini', 'entropy', 'log_loss']:
            cart = AggregateCART(
                criterion=criterion,
                max_depth=4,
                min_samples_leaf=1,
                random_state=42
            )
            cart.fit(self.sample_data, ['feature1', 'feature2', 'feature3'], 'good_count', 'bad_count')
            models[criterion] = cart

        # Extract tree characteristics
        tree_depths = {criterion: model.get_depth() for criterion, model in models.items()}
        tree_leaves = {criterion: model.get_n_leaves() for criterion, model in models.items()}

        # All models should have valid tree structures
        for criterion in ['gini', 'entropy', 'log_loss']:
            assert tree_depths[criterion] >= 1
            assert tree_leaves[criterion] >= 1

        # Note: Different criteria may produce different structures,
        # but this is data-dependent, so we mainly check validity

    def test_model_serialization_with_criteria(self):
        """Test that models with different criteria serialize/deserialize correctly."""
        for criterion in ['gini', 'entropy', 'log_loss']:
            # Train model
            cart = AggregateCART(criterion=criterion, max_depth=3, random_state=42)
            cart.fit(self.test_data, self.feature_cols, self.good_col, self.bad_col)

            # Serialize to JSON
            json_str = cart.to_json()
            data = json.loads(json_str)

            # Check criterion is preserved
            assert data['model_info']['criterion'] == criterion

            # Deserialize and test
            cart_loaded = AggregateCART.from_json(json_str)
            assert cart_loaded.criterion == criterion

            # Test predictions match
            original_pred = cart.predict(self.test_data[self.feature_cols])
            loaded_pred = cart_loaded.predict(self.test_data[self.feature_cols])

            np.testing.assert_array_equal(original_pred, loaded_pred)

    def test_model_persistence_with_criteria(self):
        """Test saving and loading models with different criteria."""
        for criterion in ['gini', 'entropy', 'log_loss']:
            with tempfile.NamedTemporaryFile(mode='w', suffix='.json', delete=False) as f:
                temp_path = f.name

            try:
                # Train and save model
                cart = AggregateCART(criterion=criterion, max_depth=3, random_state=42)
                cart.fit(self.test_data, self.feature_cols, self.good_col, self.bad_col)
                cart.save_json(temp_path)

                # Load model
                cart_loaded = AggregateCART.load_json(temp_path)

                # Verify criterion is preserved
                assert cart_loaded.criterion == criterion

                # Verify predictions match
                original_pred = cart.predict_proba(self.test_data[self.feature_cols])
                loaded_pred = cart_loaded.predict_proba(self.test_data[self.feature_cols])

                np.testing.assert_array_almost_equal(original_pred, loaded_pred, decimal=10)

            finally:
                # Clean up temp file
                Path(temp_path).unlink(missing_ok=True)

    def test_edge_cases_with_criteria(self):
        """Test edge cases for all criteria."""
        # Single class data
        single_class_data = pd.DataFrame({
            'feature': ['A', 'B', 'A', 'B'],
            'good_count': [100, 100, 100, 100],
            'bad_count': [0, 0, 0, 0]
        })

        for criterion in ['gini', 'entropy', 'log_loss']:
            cart = AggregateCART(criterion=criterion, max_depth=2)
            cart.fit(single_class_data, ['feature'], 'good_count', 'bad_count')

            # Should still produce valid predictions
            pred = cart.predict(single_class_data[['feature']])
            assert all(p == 1 for p in pred)  # All should be class 1 (good)

    def test_criterion_parameter_validation(self):
        """Test criterion parameter validation in different contexts."""
        # Test case sensitivity
        with pytest.raises(ValueError):
            AggregateCART(criterion='GINI')

        with pytest.raises(ValueError):
            AggregateCART(criterion='Entropy')

        # Test whitespace handling
        with pytest.raises(ValueError):
            AggregateCART(criterion=' gini ')

        # Test None criterion
        with pytest.raises(ValueError):
            AggregateCART(criterion=None)


class TestCriterionComparison:
    """Compare performance and behavior across criteria."""

    def setup_method(self):
        """Set up comparison test data."""
        # Create a dataset where different criteria might behave differently
        np.random.seed(42)
        n_samples = 200

        self.comparison_data = pd.DataFrame({
            'feature1': np.random.choice(['A', 'B', 'C'], n_samples),
            'feature2': np.random.choice(['X', 'Y'], n_samples),
            'feature3': np.random.choice(['High', 'Medium', 'Low'], n_samples),
        })

        # Create realistic good/bad counts with some patterns
        good_counts = []
        bad_counts = []

        for _, row in self.comparison_data.iterrows():
            base_good = 70 if row['feature1'] == 'A' else 50
            base_good += 20 if row['feature2'] == 'X' else 0
            base_good += 10 if row['feature3'] == 'High' else 0

            # Add noise
            good = max(10, int(base_good + np.random.normal(0, 15)))
            bad = max(5, int(100 - good + np.random.normal(0, 10)))

            good_counts.append(good)
            bad_counts.append(bad)

        self.comparison_data['good_count'] = good_counts
        self.comparison_data['bad_count'] = bad_counts

    def test_prediction_consistency_across_criteria(self):
        """Test that all criteria produce reasonable predictions on same data."""
        models = {}
        predictions = {}

        for criterion in ['gini', 'entropy', 'log_loss']:
            cart = AggregateCART(
                criterion=criterion,
                max_depth=4,
                min_samples_leaf=5,
                random_state=42
            )
            cart.fit(
                self.comparison_data,
                ['feature1', 'feature2', 'feature3'],
                'good_count',
                'bad_count'
            )
            models[criterion] = cart
            predictions[criterion] = cart.predict(self.comparison_data[['feature1', 'feature2', 'feature3']])

        # All models should produce valid predictions
        for criterion, pred in predictions.items():
            assert len(pred) == len(self.comparison_data)
            assert all(p in [0, 1] for p in pred)

        # Predictions might differ but should be reasonable
        # (exact same predictions aren't required as criteria can legitimately differ)

    def test_training_stability_across_criteria(self):
        """Test that training is stable across different criteria."""
        for criterion in ['gini', 'entropy', 'log_loss']:
            # Train multiple times with same parameters
            predictions = []
            for seed in [42, 43, 44]:
                cart = AggregateCART(criterion=criterion, random_state=seed, max_depth=3)
                cart.fit(
                    self.comparison_data,
                    ['feature1', 'feature2', 'feature3'],
                    'good_count',
                    'bad_count'
                )
                pred = cart.predict(self.comparison_data[['feature1', 'feature2', 'feature3']])
                predictions.append(pred)

            # With same random state, should get identical results
            cart1 = AggregateCART(criterion=criterion, random_state=42, max_depth=3)
            cart2 = AggregateCART(criterion=criterion, random_state=42, max_depth=3)

            cart1.fit(self.comparison_data, ['feature1', 'feature2', 'feature3'], 'good_count', 'bad_count')
            cart2.fit(self.comparison_data, ['feature1', 'feature2', 'feature3'], 'good_count', 'bad_count')

            pred1 = cart1.predict(self.comparison_data[['feature1', 'feature2', 'feature3']])
            pred2 = cart2.predict(self.comparison_data[['feature1', 'feature2', 'feature3']])

            np.testing.assert_array_equal(pred1, pred2)