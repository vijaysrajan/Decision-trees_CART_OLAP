#!/usr/bin/env python3
"""
Deep Decision Tree Comparison Tool

Compares CART-OLAP tree with CART_sketch reference tree in detail.
Analyzes features, splits, counts, impurities, and structure at every node.
"""

import json
import requests
from typing import Dict, Any, List, Tuple
from dataclasses import dataclass
from collections import defaultdict


@dataclass
class NodeComparison:
    """Comparison result for a single node"""
    depth: int
    path: str
    olap_feature: str
    sketch_feature: str
    olap_samples: float
    sketch_samples: float
    olap_good: float
    sketch_good: float
    olap_bad: float
    sketch_bad: float
    olap_impurity: float
    sketch_impurity: float
    feature_match: bool
    samples_match: bool
    counts_match: bool
    impurity_match: bool

    def all_match(self) -> bool:
        return self.feature_match and self.samples_match and self.counts_match and self.impurity_match


class TreeComparator:
    """Deep comparison tool for decision trees"""

    def __init__(self, tolerance: float = 1e-3):
        self.tolerance = tolerance
        self.differences: List[NodeComparison] = []
        self.depth_stats: Dict[int, Dict[str, int]] = defaultdict(lambda: {
            'total_nodes': 0, 'matching_nodes': 0, 'feature_matches': 0,
            'count_matches': 0, 'impurity_matches': 0
        })

    def load_cart_sketch_tree(self) -> Dict[str, Any]:
        """Load the CART_sketch reference tree from GitHub"""
        url = "https://raw.githubusercontent.com/vijaysrajan/Decision-trees_CART_sketch/master/DU_output/du_model_lg_k_18/3col_sketches_lg_k_18_model_lg_k_18.json"

        try:
            response = requests.get(url, timeout=30)
            response.raise_for_status()
            return response.json()
        except Exception as e:
            print(f"❌ Error loading CART_sketch tree: {e}")
            return {}

    def load_cart_olap_tree(self, filepath: str) -> Dict[str, Any]:
        """Load the CART-OLAP tree"""
        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                return json.load(f)
        except Exception as e:
            print(f"❌ Error loading CART-OLAP tree: {e}")
            return {}

    def normalize_feature_name(self, feature: str) -> str:
        """Normalize feature names for comparison"""
        if not feature:
            return ""
        # Remove any whitespace and convert to standard format
        return feature.strip()

    def compare_values(self, val1: float, val2: float) -> bool:
        """Compare two values with tolerance"""
        return abs(val1 - val2) <= self.tolerance

    def extract_node_info(self, node: Dict[str, Any], is_sketch: bool = False) -> Tuple[str, float, float, float, float]:
        """Extract node information for comparison"""
        if is_sketch:
            # CART_sketch format
            feature = node.get('feature_name', '')
            samples = float(node.get('n_samples', 0))
            class_counts = node.get('class_counts', [0, 0])
            good_count = float(class_counts[0]) if len(class_counts) > 0 else 0
            bad_count = float(class_counts[1]) if len(class_counts) > 1 else 0
            impurity = float(node.get('impurity', 0))
        else:
            # CART-OLAP format
            feature = node.get('feature', '')
            samples = float(node.get('samples', 0))
            good_count = float(node.get('good_count', 0))
            bad_count = float(node.get('bad_count', 0))
            impurity = float(node.get('impurity', 0))

        return feature, samples, good_count, bad_count, impurity

    def compare_trees_recursive(self, olap_node: Dict[str, Any], sketch_node: Dict[str, Any],
                              path: str = "root", depth: int = 0) -> None:
        """Recursively compare tree nodes"""

        # Extract information from both nodes
        olap_feature, olap_samples, olap_good, olap_bad, olap_impurity = self.extract_node_info(olap_node, False)
        sketch_feature, sketch_samples, sketch_good, sketch_bad, sketch_impurity = self.extract_node_info(sketch_node, True)

        # Normalize features for comparison
        olap_feature_norm = self.normalize_feature_name(olap_feature)
        sketch_feature_norm = self.normalize_feature_name(sketch_feature)

        # Compare values
        feature_match = olap_feature_norm == sketch_feature_norm
        samples_match = self.compare_values(olap_samples, sketch_samples)
        counts_match = (self.compare_values(olap_good, sketch_good) and
                       self.compare_values(olap_bad, sketch_bad))
        impurity_match = self.compare_values(olap_impurity, sketch_impurity)

        # Create comparison record
        comparison = NodeComparison(
            depth=depth,
            path=path,
            olap_feature=olap_feature,
            sketch_feature=sketch_feature,
            olap_samples=olap_samples,
            sketch_samples=sketch_samples,
            olap_good=olap_good,
            sketch_good=sketch_good,
            olap_bad=olap_bad,
            sketch_bad=sketch_bad,
            olap_impurity=olap_impurity,
            sketch_impurity=sketch_impurity,
            feature_match=feature_match,
            samples_match=samples_match,
            counts_match=counts_match,
            impurity_match=impurity_match
        )

        self.differences.append(comparison)

        # Update depth statistics
        stats = self.depth_stats[depth]
        stats['total_nodes'] += 1
        if comparison.all_match():
            stats['matching_nodes'] += 1
        if feature_match:
            stats['feature_matches'] += 1
        if counts_match:
            stats['count_matches'] += 1
        if impurity_match:
            stats['impurity_matches'] += 1

        # Check if both nodes are leaves or internal nodes
        olap_is_leaf = olap_node.get('type') == 'leaf'
        sketch_is_leaf = sketch_node.get('is_leaf', False)

        if olap_is_leaf != sketch_is_leaf:
            print(f"⚠️  Node type mismatch at {path}: OLAP={'leaf' if olap_is_leaf else 'internal'}, "
                  f"Sketch={'leaf' if sketch_is_leaf else 'internal'}")
            return

        # If both are internal nodes, compare children
        if not olap_is_leaf and not sketch_is_leaf:
            olap_left = olap_node.get('left')
            olap_right = olap_node.get('right')
            sketch_left = sketch_node.get('left')
            sketch_right = sketch_node.get('right')

            # Compare left children
            if olap_left and sketch_left:
                self.compare_trees_recursive(olap_left, sketch_left, f"{path}/left", depth + 1)
            elif olap_left or sketch_left:
                print(f"⚠️  Left child mismatch at {path}")

            # Compare right children
            if olap_right and sketch_right:
                self.compare_trees_recursive(olap_right, sketch_right, f"{path}/right", depth + 1)
            elif olap_right or sketch_right:
                print(f"⚠️  Right child mismatch at {path}")

    def analyze_differences(self) -> None:
        """Analyze and report differences"""
        print("\n" + "="*80)
        print("DEEP DECISION TREE COMPARISON RESULTS")
        print("="*80)

        total_nodes = len(self.differences)
        perfect_matches = sum(1 for diff in self.differences if diff.all_match())

        print(f"\n📊 OVERALL SUMMARY:")
        print(f"   Total nodes compared: {total_nodes}")
        print(f"   Perfect matches: {perfect_matches}")
        print(f"   Match percentage: {perfect_matches/total_nodes*100:.1f}%")

        print(f"\n🌳 DEPTH ANALYSIS:")
        for depth in sorted(self.depth_stats.keys()):
            stats = self.depth_stats[depth]
            total = stats['total_nodes']
            if total > 0:
                print(f"   Depth {depth}: {stats['matching_nodes']}/{total} perfect matches "
                      f"({stats['matching_nodes']/total*100:.1f}%)")
                print(f"     Features: {stats['feature_matches']}/{total}, "
                      f"Counts: {stats['count_matches']}/{total}, "
                      f"Impurity: {stats['impurity_matches']}/{total}")

        # Show detailed differences for non-matching nodes
        print(f"\n❌ DETAILED DIFFERENCES:")
        differences_found = False
        for diff in self.differences:
            if not diff.all_match():
                differences_found = True
                print(f"\n   Path: {diff.path} (Depth {diff.depth})")

                if not diff.feature_match:
                    print(f"     🔧 Feature: OLAP='{diff.olap_feature}' vs Sketch='{diff.sketch_feature}'")

                if not diff.samples_match:
                    print(f"     📊 Samples: OLAP={diff.olap_samples} vs Sketch={diff.sketch_samples}")

                if not diff.counts_match:
                    print(f"     📈 Counts: OLAP=({diff.olap_good},{diff.olap_bad}) vs "
                          f"Sketch=({diff.sketch_good},{diff.sketch_bad})")

                if not diff.impurity_match:
                    print(f"     🎯 Impurity: OLAP={diff.olap_impurity:.6f} vs Sketch={diff.sketch_impurity:.6f}")

        if not differences_found:
            print("   🎉 No differences found! Trees are identical.")

    def run_comparison(self, olap_tree_path: str) -> None:
        """Run the complete comparison"""
        print("🔄 Loading decision trees...")

        # Load trees
        sketch_tree = self.load_cart_sketch_tree()
        olap_tree = self.load_cart_olap_tree(olap_tree_path)

        if not sketch_tree or not olap_tree:
            print("❌ Failed to load one or both trees")
            return

        print("✅ Trees loaded successfully")

        # Extract tree structures
        sketch_root = sketch_tree.get('tree_structure', {})
        olap_root = olap_tree.get('tree', {})

        if not sketch_root or not olap_root:
            print("❌ Could not find tree structures in JSON files")
            return

        print("🔍 Starting deep tree comparison...")

        # Run comparison
        self.compare_trees_recursive(olap_root, sketch_root)

        # Analyze and report
        self.analyze_differences()


if __name__ == "__main__":
    comparator = TreeComparator(tolerance=1e-2)  # Allow small floating point differences
    comparator.run_comparison("output/du_model_cli.json")