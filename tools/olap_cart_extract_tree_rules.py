#!/usr/bin/env python3
"""
Extract decision tree rules from CART-OLAP JSON tree structure for SQL validation.

This tool is adapted from CART_sketch rule extraction to work with CART-OLAP format.
It traverses a decision tree JSON file and generates:
1. SQL WHERE clauses for each leaf node
2. Human-readable English rules
3. Expected predictions and probabilities

Usage:
    python tools/olap_cart_extract_tree_rules.py path/to/tree.json --output_dir output/
"""

import json
import argparse
from pathlib import Path
from typing import List, Dict, Any, Tuple, Optional


class OlapCartRuleExtractor:
    """
    Extracts decision rules from CART-OLAP JSON tree structure for SQL validation.
    """

    def __init__(self, tree_json_path: str):
        """
        Initialize the rule extractor.

        Parameters
        ----------
        tree_json_path : str
            Path to the JSON tree file
        """
        self.tree_json_path = Path(tree_json_path)

        # Load tree structure
        with open(self.tree_json_path, 'r') as f:
            self.tree_data = json.load(f)

        # Extract tree structure - CART-OLAP format uses "tree" key
        if 'tree' in self.tree_data:
            self.tree = self.tree_data['tree']
        else:
            # Fallback to whole structure
            self.tree = self.tree_data

        # Extract feature names
        self.feature_names = self.tree_data.get('model_info', {}).get('feature_names', [])

        # Store extracted rules
        self.rules = []

    def extract_all_rules(self) -> List[Dict[str, Any]]:
        """
        Extract all decision rules from the tree.

        Returns
        -------
        rules : List[Dict]
            List of rule dictionaries with SQL, English, and prediction info
        """
        self.rules = []
        self._traverse_tree(self.tree, [], "root")
        return self.rules

    def _traverse_tree(self, node: Dict[str, Any], path_conditions: List[Tuple[str, bool]], node_path: str):
        """
        Recursively traverse the tree and extract rules.

        Parameters
        ----------
        node : Dict
            Current tree node
        path_conditions : List[Tuple[str, bool]]
            List of (feature_name, is_present) conditions from root to current node
        node_path : str
            Human-readable path description
        """
        if node.get('type') == 'leaf':
            # Leaf node - create rule
            rule = self._create_rule_from_path(path_conditions, node, node_path)
            self.rules.append(rule)
        elif node.get('type') == 'internal':
            # Split node - recurse to children
            feature_name = node.get('feature', 'unknown_feature')

            # Left child: feature absent (= 0/FALSE)
            if 'left' in node:
                left_conditions = path_conditions + [(feature_name, False)]
                left_path = f"{node_path} → {feature_name}=0"
                self._traverse_tree(node['left'], left_conditions, left_path)

            # Right child: feature present (= 1/TRUE)
            if 'right' in node:
                right_conditions = path_conditions + [(feature_name, True)]
                right_path = f"{node_path} → {feature_name}=1"
                self._traverse_tree(node['right'], right_conditions, right_path)

    def _create_rule_from_path(self, path_conditions: List[Tuple[str, bool]],
                              leaf_node: Dict[str, Any], node_path: str) -> Dict[str, Any]:
        """
        Create a complete rule from path conditions and leaf node info.

        Parameters
        ----------
        path_conditions : List[Tuple[str, bool]]
            List of (feature_name, is_present) conditions
        leaf_node : Dict
            Leaf node data
        node_path : str
            Human-readable path

        Returns
        -------
        rule : Dict
            Complete rule with SQL, English, and prediction info
        """
        # Build SQL WHERE clause
        sql_conditions = []
        english_conditions = []

        for feature_name, is_present in path_conditions:
            if is_present:
                sql_conditions.append(f"`{feature_name}` = 1")
                english_conditions.append(f"{feature_name} is TRUE")
            else:
                sql_conditions.append(f"`{feature_name}` = 0")
                english_conditions.append(f"{feature_name} is FALSE")

        sql_where = " AND ".join(sql_conditions) if sql_conditions else "TRUE"
        english_rule = " AND ".join(english_conditions) if english_conditions else "No conditions"

        # Extract prediction info from CART-OLAP format
        prediction = leaf_node.get('prediction', 'unknown')
        good_count = leaf_node.get('good_count', 0)
        bad_count = leaf_node.get('bad_count', 0)
        total_samples = good_count + bad_count

        # Calculate probabilities
        if total_samples > 0:
            positive_prob = good_count / total_samples
            negative_prob = bad_count / total_samples
        else:
            positive_prob = 0.0
            negative_prob = 1.0

        probabilities = [negative_prob, positive_prob]
        confidence = max(probabilities)

        rule = {
            'rule_id': len(self.rules) + 1,
            'node_path': node_path,
            'sql_where_clause': sql_where,
            'english_rule': english_rule,
            'prediction': int(prediction) if prediction != 'unknown' else None,
            'prediction_label': 'Positive' if prediction == 1 else 'Negative' if prediction == 0 else 'Unknown',
            'confidence': round(confidence, 4),
            'class_counts': [bad_count, good_count],
            'n_samples': total_samples,
            'class_probabilities': [round(negative_prob, 4), round(positive_prob, 4)],
            'conditions_count': len(path_conditions),
            'depth': len(path_conditions)
        }

        return rule

    def generate_sql_validation_queries(self, table_name: str = "DU_raw",
                                       target_column: str = "target") -> List[str]:
        """
        Generate SQL queries to validate each rule against the database.

        Parameters
        ----------
        table_name : str
            Name of the database table
        target_column : str
            Name of the target column

        Returns
        -------
        queries : List[str]
            List of SQL validation queries
        """
        queries = []

        for rule in self.rules:
            where_clause = rule['sql_where_clause']
            expected_samples = rule['n_samples']
            expected_prediction = rule['prediction']

            # Count total samples matching the conditions
            count_query = f"""
-- Rule {rule['rule_id']}: {rule['english_rule']}
SELECT
    COUNT(*) as actual_samples,
    {expected_samples} as expected_samples,
    ROUND(AVG(CASE WHEN {target_column} = 1 THEN 1.0 ELSE 0.0 END), 4) as actual_positive_rate,
    {rule['class_probabilities'][1]} as expected_positive_rate,
    '{rule['prediction_label']}' as expected_prediction
FROM {table_name}
WHERE {where_clause};
"""
            queries.append(count_query)

        return queries

    def generate_binomial_analysis(self) -> Dict[str, Any]:
        """
        Generate binomial distribution analysis for rules.

        Returns
        -------
        analysis : Dict
            Binomial analysis with statistical tests
        """
        analysis = {
            'total_rules': len(self.rules),
            'binomial_tests': [],
            'summary': {
                'high_confidence_rules': 0,
                'low_confidence_rules': 0,
                'total_samples': 0
            }
        }

        for rule in self.rules:
            n_samples = rule['n_samples']
            positive_count = rule['class_counts'][1]
            positive_rate = rule['class_probabilities'][1]

            # Binomial test parameters
            expected_prob = 0.5  # Null hypothesis: equal probability

            # Calculate z-score for binomial test
            if n_samples > 0:
                expected_mean = n_samples * expected_prob
                expected_variance = n_samples * expected_prob * (1 - expected_prob)
                z_score = (positive_count - expected_mean) / (expected_variance ** 0.5) if expected_variance > 0 else 0
            else:
                z_score = 0

            binomial_test = {
                'rule_id': rule['rule_id'],
                'samples': n_samples,
                'positive_count': positive_count,
                'positive_rate': positive_rate,
                'z_score': round(z_score, 4),
                'significant': abs(z_score) > 1.96,  # 95% confidence
                'confidence_level': rule['confidence']
            }

            analysis['binomial_tests'].append(binomial_test)

            # Update summary
            analysis['summary']['total_samples'] += n_samples
            if rule['confidence'] > 0.8:
                analysis['summary']['high_confidence_rules'] += 1
            else:
                analysis['summary']['low_confidence_rules'] += 1

        return analysis

    def print_summary_report(self):
        """Print a comprehensive summary of extracted rules."""
        print(f"🌳 CART-OLAP Decision Tree Rule Extraction Report")
        print(f"=" * 60)
        print(f"Tree file: {self.tree_json_path}")
        print(f"Total rules extracted: {len(self.rules)}")
        print(f"Tree depth: {max(rule['depth'] for rule in self.rules) if self.rules else 0}")

        # Summary by prediction
        positive_rules = [r for r in self.rules if r['prediction'] == 1]
        negative_rules = [r for r in self.rules if r['prediction'] == 0]

        print(f"\nPrediction Summary:")
        print(f"  Positive prediction rules: {len(positive_rules)}")
        print(f"  Negative prediction rules: {len(negative_rules)}")

        if positive_rules:
            avg_pos_confidence = sum(r['confidence'] for r in positive_rules) / len(positive_rules)
            print(f"  Average positive confidence: {avg_pos_confidence:.4f}")

        if negative_rules:
            avg_neg_confidence = sum(r['confidence'] for r in negative_rules) / len(negative_rules)
            print(f"  Average negative confidence: {avg_neg_confidence:.4f}")

        print(f"\n" + "="*60)

    def save_rules_to_file(self, output_path: str):
        """
        Save extracted rules to a JSON file.

        Parameters
        ----------
        output_path : str
            Path to save the rules JSON file
        """
        output_data = {
            'metadata': {
                'source_tree': str(self.tree_json_path),
                'total_rules': len(self.rules),
                'extractor_type': 'CART-OLAP',
                'feature_count': len(self.feature_names)
            },
            'rules': self.rules
        }

        with open(output_path, 'w') as f:
            json.dump(output_data, f, indent=2)

        print(f"💾 Rules saved to: {output_path}")

    def save_sql_queries(self, output_path: str, table_name: str = "DU_raw",
                        target_column: str = "target"):
        """
        Save SQL validation queries to a file.

        Parameters
        ----------
        output_path : str
            Path to save the SQL file
        table_name : str
            Database table name
        target_column : str
            Target column name
        """
        queries = self.generate_sql_validation_queries(table_name, target_column)

        with open(output_path, 'w') as f:
            f.write(f"-- CART-OLAP Decision Tree Validation Queries\n")
            f.write(f"-- Generated from: {self.tree_json_path}\n")
            f.write(f"-- Total rules: {len(self.rules)}\n")
            f.write(f"-- Table: {table_name}\n")
            f.write(f"-- Target column: {target_column}\n\n")

            for i, query in enumerate(queries, 1):
                f.write(f"{query}\n")
                if i < len(queries):
                    f.write("\n" + "-"*80 + "\n\n")

        print(f"📝 SQL queries saved to: {output_path}")

    def save_binomial_analysis(self, output_path: str):
        """
        Save binomial distribution analysis to a JSON file.

        Parameters
        ----------
        output_path : str
            Path to save the binomial analysis JSON file
        """
        analysis = self.generate_binomial_analysis()

        with open(output_path, 'w') as f:
            json.dump(analysis, f, indent=2)

        print(f"📊 Binomial analysis saved to: {output_path}")


def main():
    """Main function to run the tree rule extraction."""
    parser = argparse.ArgumentParser(
        description="Extract decision tree rules from CART-OLAP JSON format",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
    # Extract rules from CART-OLAP tree
    python tools/olap_cart_extract_tree_rules.py output/du_model_cli.json

    # Save all outputs to directory
    python tools/olap_cart_extract_tree_rules.py output/du_model_cli.json --output_dir output/du_rules/

    # Custom table settings
    python tools/olap_cart_extract_tree_rules.py output/du_model_cli.json --table DU_raw --target target
        """
    )

    parser.add_argument('tree_json', help='Path to the CART-OLAP JSON tree file')
    parser.add_argument('--output_dir', help='Output directory for all generated files')
    parser.add_argument('--save_rules', help='Save extracted rules to JSON file')
    parser.add_argument('--save_sql', help='Save SQL validation queries to file')
    parser.add_argument('--save_binomial', help='Save binomial analysis to JSON file')
    parser.add_argument('--table', default='DU_raw', help='Database table name for SQL queries')
    parser.add_argument('--target_column', default='target', help='Target column name')
    parser.add_argument('--quiet', '-q', action='store_true', help='Only show summary, no detailed rules')

    args = parser.parse_args()

    # Validate input file
    if not Path(args.tree_json).exists():
        print(f"❌ Error: Tree JSON file not found: {args.tree_json}")
        return 1

    try:
        # Create extractor and extract rules
        extractor = OlapCartRuleExtractor(args.tree_json)
        rules = extractor.extract_all_rules()

        # Print summary
        extractor.print_summary_report()

        # Setup output directory if specified
        if args.output_dir:
            output_dir = Path(args.output_dir)
            output_dir.mkdir(parents=True, exist_ok=True)

            # Generate default filenames based on input
            model_name = Path(args.tree_json).stem
            rules_file = output_dir / f"{model_name}_extracted_rules.json"
            sql_file = output_dir / f"{model_name}_validation_queries.sql"
            binomial_file = output_dir / f"{model_name}_binomial_analysis.json"

        else:
            rules_file = args.save_rules
            sql_file = args.save_sql
            binomial_file = args.save_binomial

        # Save outputs
        if rules_file or args.output_dir:
            file_path = rules_file if rules_file else output_dir / f"{Path(args.tree_json).stem}_extracted_rules.json"
            extractor.save_rules_to_file(str(file_path))

        if sql_file or args.output_dir:
            file_path = sql_file if sql_file else output_dir / f"{Path(args.tree_json).stem}_validation_queries.sql"
            extractor.save_sql_queries(str(file_path), args.table, args.target_column)

        if binomial_file or args.output_dir:
            file_path = binomial_file if binomial_file else output_dir / f"{Path(args.tree_json).stem}_binomial_analysis.json"
            extractor.save_binomial_analysis(str(file_path))

        print(f"\n✅ Rule extraction completed successfully!")
        print(f"   Total rules: {len(rules)}")

        return 0

    except Exception as e:
        print(f"❌ Error during rule extraction: {e}")
        import traceback
        traceback.print_exc()
        return 1


if __name__ == '__main__':
    exit(main())