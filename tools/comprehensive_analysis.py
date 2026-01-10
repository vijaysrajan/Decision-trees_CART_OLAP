#!/usr/bin/env python3
"""
Comprehensive Tree Analysis

Complete statistical analysis of both trees including all depths.
"""

import json
import requests
from typing import Dict, Any, List
from collections import defaultdict


def load_trees():
    """Load both trees"""
    url = "https://raw.githubusercontent.com/vijaysrajan/Decision-trees_CART_sketch/master/DU_output/du_model_lg_k_18/3col_sketches_lg_k_18_model_lg_k_18.json"
    response = requests.get(url, timeout=30)
    sketch_tree = response.json()

    with open("output/du_model_cli.json", 'r', encoding='utf-8') as f:
        olap_tree = json.load(f)

    return sketch_tree, olap_tree


def extract_all_nodes(node: Dict[str, Any], is_sketch: bool = False) -> List[Dict[str, Any]]:
    """Extract all nodes from tree recursively"""
    nodes = []

    # Current node
    if is_sketch:
        node_info = {
            'depth': node.get('depth', 0),
            'feature': node.get('feature_name', 'LEAF'),
            'samples': node.get('n_samples', 0),
            'good': node.get('class_counts', [0, 0])[0] if node.get('class_counts') else 0,
            'bad': node.get('class_counts', [0, 0])[1] if len(node.get('class_counts', [])) > 1 else 0,
            'impurity': node.get('impurity', 0),
            'is_leaf': node.get('is_leaf', False)
        }
    else:
        node_info = {
            'depth': node.get('depth', 0),
            'feature': node.get('feature', 'LEAF'),
            'samples': node.get('samples', 0),
            'good': node.get('good_count', 0),
            'bad': node.get('bad_count', 0),
            'impurity': node.get('impurity', 0),
            'is_leaf': node.get('type') == 'leaf'
        }

    nodes.append(node_info)

    # Children
    if not node_info['is_leaf']:
        if node.get('left'):
            nodes.extend(extract_all_nodes(node['left'], is_sketch))
        if node.get('right'):
            nodes.extend(extract_all_nodes(node['right'], is_sketch))

    return nodes


def analyze_trees():
    """Complete tree analysis"""
    print("🔍 COMPREHENSIVE DECISION TREE ANALYSIS")
    print("=" * 80)

    sketch_tree, olap_tree = load_trees()

    # Extract all nodes
    sketch_nodes = extract_all_nodes(sketch_tree['tree_structure'], True)
    olap_nodes = extract_all_nodes(olap_tree['tree'])

    print(f"\n📊 TREE STATISTICS:")
    print(f"   CART_sketch total nodes: {len(sketch_nodes)}")
    print(f"   CART-OLAP total nodes: {len(olap_nodes)}")

    # Group by depth
    sketch_by_depth = defaultdict(list)
    olap_by_depth = defaultdict(list)

    for node in sketch_nodes:
        sketch_by_depth[node['depth']].append(node)

    for node in olap_nodes:
        olap_by_depth[node['depth']].append(node)

    print(f"\n🌳 DEPTH ANALYSIS:")
    all_depths = sorted(set(list(sketch_by_depth.keys()) + list(olap_by_depth.keys())))

    for depth in all_depths:
        sketch_count = len(sketch_by_depth[depth])
        olap_count = len(olap_by_depth[depth])

        sketch_leaves = sum(1 for n in sketch_by_depth[depth] if n['is_leaf'])
        olap_leaves = sum(1 for n in olap_by_depth[depth] if n['is_leaf'])

        print(f"\n   Depth {depth}:")
        print(f"     Nodes: Sketch={sketch_count}, OLAP={olap_count}")

        if sketch_count == olap_count and sketch_count > 0:
            # Compare nodes at this depth
            matches = 0
            feature_matches = 0
            sample_matches = 0
            count_matches = 0
            impurity_matches = 0

            for i in range(sketch_count):
                s_node = sketch_by_depth[depth][i]
                o_node = olap_by_depth[depth][i]

                # Feature match
                if s_node['feature'] == o_node['feature']:
                    feature_matches += 1

                # Sample match
                if abs(s_node['samples'] - o_node['samples']) < 1e-3:
                    sample_matches += 1

                # Count match
                if (abs(s_node['good'] - o_node['good']) < 1e-3 and
                    abs(s_node['bad'] - o_node['bad']) < 1e-3):
                    count_matches += 1

                # Impurity match
                if abs(s_node['impurity'] - o_node['impurity']) < 1e-2:
                    impurity_matches += 1

                # Overall match
                if (s_node['feature'] == o_node['feature'] and
                    abs(s_node['samples'] - o_node['samples']) < 1e-3 and
                    abs(s_node['good'] - o_node['good']) < 1e-3 and
                    abs(s_node['bad'] - o_node['bad']) < 1e-3 and
                    abs(s_node['impurity'] - o_node['impurity']) < 1e-2):
                    matches += 1

            print(f"     Perfect matches: {matches}/{sketch_count} ({matches/sketch_count*100:.1f}%)")
            print(f"     Feature matches: {feature_matches}/{sketch_count}")
            print(f"     Sample matches: {sample_matches}/{sketch_count}")
            print(f"     Count matches: {count_matches}/{sketch_count}")
            print(f"     Impurity matches: {impurity_matches}/{sketch_count}")

    # Feature analysis
    print(f"\n🔧 FEATURE USAGE ANALYSIS:")

    sketch_features = [node['feature'] for node in sketch_nodes if not node['is_leaf']]
    olap_features = [node['feature'] for node in olap_nodes if not node['is_leaf']]

    sketch_feature_counts = defaultdict(int)
    olap_feature_counts = defaultdict(int)

    for feature in sketch_features:
        sketch_feature_counts[feature] += 1

    for feature in olap_features:
        olap_feature_counts[feature] += 1

    print(f"   Features used in splits:")
    all_features = sorted(set(list(sketch_feature_counts.keys()) + list(olap_feature_counts.keys())))

    for feature in all_features[:10]:  # Show top 10
        sketch_count = sketch_feature_counts[feature]
        olap_count = olap_feature_counts[feature]
        print(f"     {feature}: Sketch={sketch_count}, OLAP={olap_count}")

    print(f"\n🎯 FINAL VERIFICATION:")

    # Overall statistics
    total_sketch_samples = sum(node['samples'] for node in sketch_nodes if node['depth'] == 0)
    total_olap_samples = sum(node['samples'] for node in olap_nodes if node['depth'] == 0)

    total_sketch_good = sum(node['good'] for node in sketch_nodes if node['depth'] == 0)
    total_olap_good = sum(node['good'] for node in olap_nodes if node['depth'] == 0)

    total_sketch_bad = sum(node['bad'] for node in sketch_nodes if node['depth'] == 0)
    total_olap_bad = sum(node['bad'] for node in olap_nodes if node['depth'] == 0)

    print(f"   Total samples: Sketch={total_sketch_samples}, OLAP={total_olap_samples}")
    print(f"   Total good: Sketch={total_sketch_good}, OLAP={total_olap_good}")
    print(f"   Total bad: Sketch={total_sketch_bad}, OLAP={total_olap_bad}")

    # Overall match percentage
    total_nodes = len(sketch_nodes)
    if total_nodes == len(olap_nodes):
        perfect_matches = 0
        for i in range(total_nodes):
            s_node = sketch_nodes[i]
            o_node = olap_nodes[i]

            if (s_node['feature'] == o_node['feature'] and
                abs(s_node['samples'] - o_node['samples']) < 1e-3 and
                abs(s_node['good'] - o_node['good']) < 1e-3 and
                abs(s_node['bad'] - o_node['bad']) < 1e-3 and
                abs(s_node['impurity'] - o_node['impurity']) < 1e-2):
                perfect_matches += 1

        print(f"\n🎉 OVERALL RESULT:")
        print(f"   Perfect node matches: {perfect_matches}/{total_nodes} ({perfect_matches/total_nodes*100:.1f}%)")

        if perfect_matches == total_nodes:
            print(f"   ✅ TREES ARE IDENTICAL!")
            print(f"   🎊 The CART-OLAP implementation perfectly reproduces the CART_sketch results!")
        else:
            print(f"   ❌ Trees have differences")
    else:
        print(f"   ❌ Different number of nodes: Sketch={len(sketch_nodes)}, OLAP={len(olap_nodes)}")


if __name__ == "__main__":
    analyze_trees()