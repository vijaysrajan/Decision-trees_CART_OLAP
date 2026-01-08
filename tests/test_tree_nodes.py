"""
Unit tests for tree node classes.
"""

import pytest
from cart_olap.tree_nodes import TreeNode, LeafNode


class TestLeafNode:
    """Test LeafNode functionality."""

    def test_pure_good_leaf(self):
        """Test leaf node with only good samples."""
        leaf = LeafNode(good_count=100, bad_count=0, depth=2)

        assert leaf.prediction == 1  # Good class
        assert leaf.class_probabilities == (0.0, 1.0)
        assert leaf.samples == 100
        assert leaf.impurity == 0.0
        assert leaf.depth == 2
        assert leaf.is_leaf() == True

    def test_pure_bad_leaf(self):
        """Test leaf node with only bad samples."""
        leaf = LeafNode(good_count=0, bad_count=50, depth=1)

        assert leaf.prediction == 0  # Bad class
        assert leaf.class_probabilities == (1.0, 0.0)
        assert leaf.samples == 50
        assert leaf.impurity == 0.0
        assert leaf.depth == 1

    def test_mixed_leaf_good_majority(self):
        """Test leaf node with good majority."""
        leaf = LeafNode(good_count=70, bad_count=30, depth=0)

        assert leaf.prediction == 1  # Good class (majority)
        assert leaf.class_probabilities == (0.3, 0.7)
        assert leaf.samples == 100
        expected_impurity = 1 - (0.7**2 + 0.3**2)  # 1 - (0.49 + 0.09) = 0.42
        assert abs(leaf.impurity - expected_impurity) < 1e-10

    def test_mixed_leaf_bad_majority(self):
        """Test leaf node with bad majority."""
        leaf = LeafNode(good_count=20, bad_count=80, depth=3)

        assert leaf.prediction == 0  # Bad class (majority)
        assert leaf.class_probabilities == (0.8, 0.2)
        assert leaf.samples == 100

    def test_tied_leaf(self):
        """Test leaf node with tied counts (good wins by default)."""
        leaf = LeafNode(good_count=50, bad_count=50, depth=1)

        assert leaf.prediction == 1  # Good class (tie goes to good)
        assert leaf.class_probabilities == (0.5, 0.5)
        assert leaf.impurity == 0.5

    def test_empty_leaf(self):
        """Test leaf node with no samples."""
        leaf = LeafNode(good_count=0, bad_count=0, depth=2)

        assert leaf.prediction == 1  # Default to good when tie (0 >= 0)
        assert leaf.class_probabilities == (0.5, 0.5)
        assert leaf.samples == 0

    def test_predict_sample(self):
        """Test prediction for a sample."""
        leaf = LeafNode(good_count=80, bad_count=20, depth=1)
        sample = {'feature1': 'A', 'feature2': 'B'}  # Content doesn't matter for leaf

        prediction = leaf.predict_sample(sample)
        assert prediction == 1

    def test_predict_proba_sample(self):
        """Test probability prediction for a sample."""
        leaf = LeafNode(good_count=60, bad_count=40, depth=2)
        sample = {'feature1': 'X'}

        proba = leaf.predict_proba_sample(sample)
        assert proba == (0.4, 0.6)

    def test_get_info(self):
        """Test node information retrieval."""
        leaf = LeafNode(good_count=75, bad_count=25, depth=2)
        info = leaf.get_info()

        expected_info = {
            'type': 'leaf',
            'prediction': 1,
            'class_probabilities': [0.25, 0.75],
            'samples': 100,
            'impurity': 0.375,  # 1 - (0.75^2 + 0.25^2)
            'good_count': 75,
            'bad_count': 25,
            'depth': 2,
            'class_distribution': [25, 75]
        }

        assert info['type'] == expected_info['type']
        assert info['prediction'] == expected_info['prediction']
        assert info['samples'] == expected_info['samples']
        assert abs(info['impurity'] - expected_info['impurity']) < 1e-10


class TestTreeNode:
    """Test TreeNode functionality."""

    def test_node_creation(self):
        """Test internal node creation."""
        node = TreeNode(
            feature='feature1',
            split_value='A',
            samples=200,
            impurity=0.4,
            good_count=120,
            bad_count=80,
            depth=1
        )

        assert node.feature == 'feature1'
        assert node.split_value == 'A'
        assert node.samples == 200
        assert node.impurity == 0.4
        assert node.good_count == 120
        assert node.bad_count == 80
        assert node.depth == 1
        assert node.left is None
        assert node.right is None
        assert node.is_leaf() == False

    def test_predict_with_children(self):
        """Test prediction traversal through tree."""
        # Create root node using binary feature name (after one-hot encoding)
        # Binary logic: feature=1 (True) goes right, feature=0 (False) goes left
        root = TreeNode(
            feature='feature1=A',  # Binary feature: feature1=A vs feature1!=A
            split_value=None,      # Not used in binary logic
            samples=200,
            impurity=0.5,
            good_count=100,
            bad_count=100,
            depth=0
        )

        # Create children
        left_leaf = LeafNode(good_count=20, bad_count=80, depth=1)   # Predicts 0
        right_leaf = LeafNode(good_count=80, bad_count=20, depth=1)  # Predicts 1

        root.left = left_leaf
        root.right = right_leaf

        # Test prediction routing with binary logic
        # feature1=A is 1 means feature1='A', should go right
        sample_right = {'feature1=A': 1, 'feature2=X': 0}
        prediction = root.predict_sample(sample_right)
        assert prediction == 1  # Should go right and predict good

        # feature1=A is 0 means feature1!='A', should go left
        sample_left = {'feature1=A': 0, 'feature2=Y': 1}
        prediction = root.predict_sample(sample_left)
        assert prediction == 0  # Should go left and predict bad

    def test_predict_proba_with_children(self):
        """Test probability prediction traversal."""
        root = TreeNode(
            feature='city=Delhi',  # Binary feature: city=Delhi vs city!=Delhi
            split_value=None,      # Not used in binary logic
            samples=150,
            impurity=0.48,
            good_count=90,
            bad_count=60,
            depth=0
        )

        left_leaf = LeafNode(good_count=30, bad_count=45, depth=1)   # (0.6, 0.4)
        right_leaf = LeafNode(good_count=60, bad_count=15, depth=1)  # (0.2, 0.8)

        root.left = left_leaf
        root.right = right_leaf

        # Test probability routing with binary logic
        # city=Delhi is 1 means city='Delhi', should go right
        sample_right = {'city=Delhi': 1}
        proba = root.predict_proba_sample(sample_right)
        assert proba == (0.2, 0.8)

        # city=Delhi is 0 means city!='Delhi', should go left
        sample_left = {'city=Delhi': 0, 'city=Mumbai': 1}
        proba = root.predict_proba_sample(sample_left)
        assert proba == (0.6, 0.4)

    def test_get_info(self):
        """Test internal node information retrieval."""
        node = TreeNode(
            feature='source',
            split_value='ios',
            samples=300,
            impurity=0.32,
            good_count=180,
            bad_count=120,
            depth=0
        )

        info = node.get_info()

        expected_info = {
            'type': 'internal',
            'feature': 'source',
            'split_value': 'ios',
            'samples': 300,
            'impurity': 0.32,
            'good_count': 180,
            'bad_count': 120,
            'depth': 0,
            'class_distribution': [120, 180]
        }

        assert info['type'] == expected_info['type']
        assert info['feature'] == expected_info['feature']
        assert info['split_value'] == expected_info['split_value']
        assert info['samples'] == expected_info['samples']
        assert info['good_count'] == expected_info['good_count']
        assert info['bad_count'] == expected_info['bad_count']

    def test_deep_tree_traversal(self):
        """Test prediction in a deeper tree."""
        # Create a 3-level tree using binary features
        root = TreeNode('feature1=A', None, 400, 0.5, 200, 200, 0)

        # Level 1
        left_internal = TreeNode('feature2=X', None, 200, 0.48, 80, 120, 1)
        right_leaf = LeafNode(180, 20, 1)  # Good majority

        # Level 2
        left_left_leaf = LeafNode(20, 80, 2)   # Bad majority
        left_right_leaf = LeafNode(60, 40, 2)  # Good majority

        # Connect the tree
        root.left = left_internal
        root.right = right_leaf
        left_internal.left = left_left_leaf
        left_internal.right = left_right_leaf

        # Test deep traversal with binary logic
        # feature1=A is 1 means feature1='A', goes right to right_leaf
        sample1 = {'feature1=A': 1, 'feature2=Y': 1}
        assert root.predict_sample(sample1) == 1

        # feature1=A is 0 means feature1!='A', goes left to left_internal
        # Then feature2=X is 1 means feature2='X', goes right to left_right_leaf
        sample2 = {'feature1=A': 0, 'feature2=X': 1}
        assert root.predict_sample(sample2) == 1

        # feature1=A is 0 goes left, feature2=X is 0 means feature2!='X', goes left to left_left_leaf
        sample3 = {'feature1=A': 0, 'feature2=X': 0, 'feature2=Z': 1}
        assert root.predict_sample(sample3) == 0