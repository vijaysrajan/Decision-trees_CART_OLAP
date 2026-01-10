#!/usr/bin/env python3
"""
Enhanced Tree Rule Extractor for CART-OLAP
Based on CART_sketch but adapted for enhanced CART-OLAP JSON structure
Extracts human-readable and SQL rules from decision tree JSON models
"""

import json
import argparse
import sys
from pathlib import Path
from typing import Dict, List, Any, Optional, Tuple
import re

class CartOlapRuleExtractor:
    """Extract rules from CART-OLAP decision tree models"""

    def __init__(self, model_path: str):
        self.model_path = model_path
        self.tree_data = self._load_tree()
        self.rules = []
        self.rule_counter = 0

    def _load_tree(self) -> Dict:
        """Load and parse the CART-OLAP tree model"""
        try:
            with open(self.model_path, 'r') as f:
                data = json.load(f)

            # Handle different JSON structures
            if 'tree_structure' in data:
                return data['tree_structure']
            elif 'tree' in data:
                return data['tree']
            else:
                # Assume the entire JSON is the tree structure
                return data

        except Exception as e:
            raise ValueError(f"Failed to load tree from {self.model_path}: {e}")

    def _extract_conditions_from_path(self, path: List[str]) -> List[Tuple[str, bool]]:
        """
        Extract feature conditions from the decision path

        Args:
            path: List of path directions ['left', 'right', ...]

        Returns:
            List of (feature_name, condition_value) tuples
        """
        conditions = []
        current_node = self.tree_data

        for direction in path:
            if 'type' in current_node and current_node['type'] == 'leaf':
                break

            if 'feature' in current_node:
                feature = current_node['feature']
                # Left = False (condition NOT met), Right = True (condition MET)
                condition_value = (direction == 'right')
                conditions.append((feature, condition_value))

                # Move to next node
                if direction == 'left' and 'left' in current_node:
                    current_node = current_node['left']
                elif direction == 'right' and 'right' in current_node:
                    current_node = current_node['right']
                else:
                    break

        return conditions

    def _generate_sql_where_clause(self, conditions: List[Tuple[str, bool]]) -> str:
        """Generate SQL WHERE clause from conditions"""
        if not conditions:
            return "1=1"  # Always true condition

        clauses = []
        for feature, value in conditions:
            # Clean feature name for SQL (remove special characters)
            clean_feature = re.sub(r'[^a-zA-Z0-9_]', '_', feature)

            if value:
                clauses.append(f"[{clean_feature}] = 1")
            else:
                clauses.append(f"([{clean_feature}] = 0 OR [{clean_feature}] IS NULL)")

        return " AND ".join(clauses)

    def _generate_english_rule(self, conditions: List[Tuple[str, bool]]) -> str:
        """Generate human-readable English rule from conditions"""
        if not conditions:
            return "All samples (no conditions)"

        positive_conditions = [feat for feat, val in conditions if val]
        negative_conditions = [feat for feat, val in conditions if not val]

        parts = []

        if positive_conditions:
            if len(positive_conditions) == 1:
                parts.append(f"WHEN {positive_conditions[0]}")
            else:
                parts.append(f"WHEN ALL({', '.join(positive_conditions)})")

        if negative_conditions:
            if len(negative_conditions) == 1:
                parts.append(f"AND NOT {negative_conditions[0]}")
            else:
                parts.append(f"AND NONE({', '.join(negative_conditions)})")

        return " ".join(parts) if parts else "All samples"

    def _traverse_tree_for_rules(self, node: Dict, path: List[str] = None) -> None:
        """Recursively traverse tree to extract all rules"""
        if path is None:
            path = []

        # Check if this is a leaf node
        if node.get('type') == 'leaf':
            # Extract leaf information
            good_count = node.get('good_count', node.get('class_counts', {}).get('good', 0))
            bad_count = node.get('bad_count', node.get('class_counts', {}).get('bad', 0))
            total_samples = good_count + bad_count

            if total_samples == 0:
                return  # Skip empty leaves

            # Determine prediction and confidence
            prediction = 1 if good_count > bad_count else 0
            confidence = max(good_count, bad_count) / total_samples if total_samples > 0 else 0.0

            # Extract conditions from path
            conditions = self._extract_conditions_from_path(path)

            # Create rule
            rule = {
                'rule_id': self.rule_counter,
                'node_path': ' -> '.join(path) if path else 'root',
                'sql_where_clause': self._generate_sql_where_clause(conditions),
                'english_rule': self._generate_english_rule(conditions),
                'prediction': prediction,
                'prediction_label': 'Good_DU' if prediction == 1 else 'Bad_DU',
                'confidence': round(confidence, 4),
                'class_counts': {'good': int(good_count), 'bad': int(bad_count)},
                'n_samples': int(total_samples),
                'class_probabilities': {
                    'good': round(good_count / total_samples, 4) if total_samples > 0 else 0.0,
                    'bad': round(bad_count / total_samples, 4) if total_samples > 0 else 0.0
                },
                'conditions_count': len(conditions),
                'depth': len(path),
                'impurity': node.get('impurity', 0.0),
                'feature_conditions': conditions
            }

            self.rules.append(rule)
            self.rule_counter += 1

        else:
            # Internal node - traverse children
            if 'left' in node and node['left']:
                self._traverse_tree_for_rules(node['left'], path + ['left'])
            if 'right' in node and node['right']:
                self._traverse_tree_for_rules(node['right'], path + ['right'])

    def extract_rules(self) -> List[Dict]:
        """Extract all rules from the tree"""
        self.rules = []
        self.rule_counter = 0
        self._traverse_tree_for_rules(self.tree_data)

        # Sort rules by sample count (descending) for better readability
        self.rules.sort(key=lambda x: x['n_samples'], reverse=True)

        # Reassign rule IDs after sorting
        for i, rule in enumerate(self.rules):
            rule['rule_id'] = i

        return self.rules

    def print_rules_summary(self):
        """Print a human-readable summary of extracted rules"""
        if not self.rules:
            print("No rules extracted!")
            return

        print(f"\n🌳 Decision Tree Rules Summary")
        print(f"📁 Model: {Path(self.model_path).name}")
        print(f"📊 Total Rules: {len(self.rules)}")
        print(f"📈 Total Samples: {sum(rule['n_samples'] for rule in self.rules)}")
        print("=" * 80)

        for rule in self.rules:
            print(f"\n🔹 Rule {rule['rule_id']} [Depth: {rule['depth']}]")
            print(f"   📋 {rule['english_rule']}")
            print(f"   🎯 Prediction: {rule['prediction_label']} (confidence: {rule['confidence']:.3f})")
            print(f"   📊 Samples: {rule['n_samples']} (Good: {rule['class_counts']['good']}, Bad: {rule['class_counts']['bad']})")
            print(f"   ⚙️  Conditions: {rule['conditions_count']}")
            if rule['feature_conditions']:
                print(f"   🔧 Features: {', '.join([f'{feat}={val}' for feat, val in rule['feature_conditions']])}")
            print(f"   🗄️  SQL: {rule['sql_where_clause']}")

    def save_rules_json(self, output_path: str):
        """Save rules to JSON file"""
        output_data = {
            'model_source': self.model_path,
            'total_rules': len(self.rules),
            'total_samples': sum(rule['n_samples'] for rule in self.rules),
            'extraction_metadata': {
                'tree_structure_type': 'CART-OLAP Enhanced',
                'rule_format': 'feature_condition_boolean',
                'left_condition': 'feature == False (condition NOT met)',
                'right_condition': 'feature == True (condition MET)'
            },
            'rules': self.rules
        }

        with open(output_path, 'w') as f:
            json.dump(output_data, f, indent=2)

        print(f"✅ Rules saved to {output_path}")

    def save_sql_queries(self, output_path: str):
        """Save SQL validation queries"""
        with open(output_path, 'w') as f:
            f.write("-- Decision Tree Rules as SQL Queries\n")
            f.write(f"-- Generated from: {self.model_path}\n")
            f.write(f"-- Total rules: {len(self.rules)}\n\n")

            for rule in self.rules:
                f.write(f"-- Rule {rule['rule_id']}: {rule['english_rule']}\n")
                f.write(f"-- Prediction: {rule['prediction_label']} (confidence: {rule['confidence']:.3f})\n")
                f.write(f"-- Samples: {rule['n_samples']}\n")
                f.write(f"SELECT '{rule['prediction_label']}' as prediction, {rule['confidence']:.4f} as confidence\n")
                f.write(f"FROM dataset WHERE {rule['sql_where_clause']};\n\n")

        print(f"✅ SQL queries saved to {output_path}")


def main():
    parser = argparse.ArgumentParser(description='Extract rules from CART-OLAP decision tree models')
    parser.add_argument('model_file', help='Path to JSON model file')
    parser.add_argument('--save_rules', help='Save rules to JSON file')
    parser.add_argument('--save_sql', help='Save SQL queries to file')
    parser.add_argument('--quiet', action='store_true', help='Suppress printed output')

    args = parser.parse_args()

    try:
        # Extract rules
        extractor = CartOlapRuleExtractor(args.model_file)
        rules = extractor.extract_rules()

        if not args.quiet:
            extractor.print_rules_summary()

        # Save outputs if requested
        if args.save_rules:
            extractor.save_rules_json(args.save_rules)

        if args.save_sql:
            extractor.save_sql_queries(args.save_sql)

        print(f"\n✨ Extracted {len(rules)} rules from {Path(args.model_file).name}")

    except Exception as e:
        print(f"❌ Error: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == '__main__':
    main()