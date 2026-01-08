"""
CART Decision Tree for Aggregate OLAP Data

A sklearn-compatible decision tree classifier for aggregate data with good/bad counts.
Includes JSON export/import functionality for model persistence.
"""

from .aggregate_cart import AggregateCART
from .tree_nodes import TreeNode, LeafNode

__version__ = "0.1.0"
__author__ = "Vijay Sankar Rajan"
__email__ = "vijay.sankar.rajan@gmail.com"

__all__ = ["AggregateCART", "TreeNode", "LeafNode"]