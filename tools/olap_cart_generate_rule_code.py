#!/usr/bin/env python3
"""
Generate if-then-else rule code from CART-OLAP trained decision tree models.

This tool converts CART-OLAP decision trees into native code (Python, Java, C++) for
cross-platform deployment with maximum performance and zero dependencies.

Usage:
    python tools/olap_cart_generate_rule_code.py --input model.json --languages python,java,cpp --output generated_rules/
"""

import json
import argparse
import os
from pathlib import Path
from typing import Dict, List, Any, Tuple


class OlapCartRuleCodeGenerator:
    """Generates if-then-else rule code from CART-OLAP decision tree JSON"""

    def __init__(self, model_json_path: str, optimize_order: bool = True):
        """Initialize generator with CART-OLAP model JSON"""
        with open(model_json_path, 'r') as f:
            self.model_data = json.load(f)

        # Extract tree structure from CART-OLAP format
        self.tree_structure = self.model_data.get('tree', {})

        # Extract model info
        model_info = self.model_data.get('model_info', {})
        self.feature_names = model_info.get('feature_names', [])
        self.classes = [0, 1]  # Binary classification
        self.model_name = f"CART-OLAP_{Path(model_json_path).stem}"
        self.optimize_order = optimize_order

        # Extract decision rules from tree
        self.rules = self._extract_rules()

        if self.optimize_order:
            self._optimize_rule_order()

    def _extract_rules(self) -> List[Dict[str, Any]]:
        """Extract all decision paths as rules from CART-OLAP format"""
        rules = []

        def traverse(node, conditions=None, path_id=0):
            if conditions is None:
                conditions = []

            if node.get('type') == 'leaf':
                # Extract leaf statistics from CART-OLAP format
                good_count = node.get('good_count', 0)
                bad_count = node.get('bad_count', 0)
                total_samples = good_count + bad_count

                if total_samples > 0:
                    positive_rate = good_count / total_samples
                    prediction = int(node.get('prediction', 1 if positive_rate > 0.5 else 0))
                    confidence = max(positive_rate, 1 - positive_rate)
                else:
                    prediction = 0
                    confidence = 0.5
                    positive_rate = 0.0

                rules.append({
                    'conditions': conditions.copy(),
                    'prediction': prediction,
                    'confidence': confidence,
                    'samples': total_samples,
                    'positive_rate': positive_rate,
                    'good_count': good_count,
                    'bad_count': bad_count,
                    'rule_id': len(rules) + 1,
                    'path_id': path_id
                })
            elif node.get('type') == 'internal':
                # Split node
                feature_name = node.get('feature', f"feature_{path_id}")

                # Left child (feature == 0, absent/false)
                left_conditions = conditions + [(feature_name, 0)]
                if 'left' in node:
                    traverse(node['left'], left_conditions, path_id * 2 + 1)

                # Right child (feature == 1, present/true)
                right_conditions = conditions + [(feature_name, 1)]
                if 'right' in node:
                    traverse(node['right'], right_conditions, path_id * 2 + 2)

        traverse(self.tree_structure)
        return rules

    def _optimize_rule_order(self):
        """Order rules by frequency (most samples first) for better performance"""
        self.rules.sort(key=lambda r: r['samples'], reverse=True)

        # Update rule IDs after sorting
        for i, rule in enumerate(self.rules):
            rule['rule_id'] = i + 1

    def generate_python(self, include_stats: bool = True) -> str:
        """Generate Python if-then-else rules"""

        lines = [
            '#!/usr/bin/env python3',
            '"""',
            'Generated decision rules for classification from CART-OLAP model',
            f'Source: {self.model_name}',
            f'Total rules: {len(self.rules)}',
            f'Feature count: {len(self.feature_names)}',
            '"""',
            '',
            'def predict_sample(features):',
            '    """',
            '    Classify a single sample using decision rules',
            '    ',
            '    Parameters',
            '    ----------',
            '    features : dict',
            '        Feature dictionary with binary values (0/1)',
            '        Keys should match feature names from training',
            '    ',
            '    Returns',
            '    -------',
            '    dict',
            '        Prediction result with confidence and metadata',
            '    """'
        ]

        # Generate rules
        for rule in self.rules:
            lines.append('')

            # Add rule comment
            conf_pct = rule['confidence'] * 100
            pred_label = "POSITIVE" if rule['prediction'] == 1 else "NEGATIVE"

            if include_stats:
                lines.append(f'    # Rule {rule["rule_id"]}: {pred_label} ({conf_pct:.1f}% confidence, {rule["samples"]} samples)')

            # Build condition
            conditions = []
            for feature_name, value in rule['conditions']:
                # Handle feature names with special characters
                safe_feature = feature_name.replace("'", "\\'")
                conditions.append(f'features.get(\'{safe_feature}\', 0) == {value}')

            if conditions:
                condition_str = ' and\n        '.join(conditions)
                lines.append(f'    if ({condition_str}):')
            else:
                lines.append('    if True:  # Root node')

            # Build return statement
            return_dict = {
                'prediction': rule['prediction'],
                'confidence': round(rule['confidence'], 3)
            }

            if include_stats:
                return_dict.update({
                    'rule_id': rule['rule_id'],
                    'samples': rule['samples'],
                    'good_count': rule['good_count'],
                    'bad_count': rule['bad_count']
                })

            lines.append(f'        return {return_dict}')

        # Add default fallback
        lines.extend([
            '',
            '    # Default fallback (should not be reached if tree is complete)',
            '    return {\'prediction\': 0, \'confidence\': 0.500, \'rule_id\': -1}',
            '',
            '',
            'def predict_batch(features_list):',
            '    """',
            '    Classify multiple samples',
            '    ',
            '    Parameters',
            '    ----------',
            '    features_list : list of dict',
            '        List of feature dictionaries',
            '    ',
            '    Returns',
            '    -------',
            '    list of dict',
            '        List of prediction results',
            '    """',
            '    return [predict_sample(features) for features in features_list]',
            '',
            '',
            'if __name__ == \'__main__\':',
            '    # Example usage',
            '    sample_features = {',
        ])

        # Add example features
        for i, feature_name in enumerate(self.feature_names[:5]):  # Show first 5 features
            safe_feature = feature_name.replace("'", "\\'")
            lines.append(f'        \'{safe_feature}\': {i % 2},')

        if len(self.feature_names) > 5:
            lines.append(f'        # ... and {len(self.feature_names) - 5} more features')

        lines.extend([
            '    }',
            '    ',
            '    result = predict_sample(sample_features)',
            '    print(f"Prediction: {result[\'prediction\']}, Confidence: {result[\'confidence\']:.3f}")',
            f'    print(f"Total rules in model: {len(self.rules)}")'
        ])

        return '\n'.join(lines)

    def generate_java(self, class_name: str = "CartOlapDecisionRules", include_stats: bool = True) -> str:
        """Generate Java if-then-else rules"""

        lines = [
            '// Generated decision rules for classification from CART-OLAP model',
            f'// Source: {self.model_name}',
            f'// Total rules: {len(self.rules)}',
            f'// Feature count: {len(self.feature_names)}',
            '',
            'import java.util.*;',
            '',
            f'public class {class_name} {{',
            ''
        ]

        # Define result record
        if include_stats:
            lines.append('    public record PredictionResult(int prediction, double confidence, int ruleId, int samples, int goodCount, int badCount) {}')
        else:
            lines.append('    public record PredictionResult(int prediction, double confidence) {}')

        lines.extend([
            '',
            '    /**',
            '     * Classify a single sample using decision rules',
            '     * @param features Feature map with binary values (0/1)',
            '     * @return Prediction result with confidence and metadata',
            '     */',
            '    public static PredictionResult predict(Map<String, Integer> features) {'
        ])

        # Generate rules
        for rule in self.rules:
            lines.append('')

            # Add rule comment
            conf_pct = rule['confidence'] * 100
            pred_label = "POSITIVE" if rule['prediction'] == 1 else "NEGATIVE"

            if include_stats:
                lines.append(f'        // Rule {rule["rule_id"]}: {pred_label} ({conf_pct:.1f}% confidence, {rule["samples"]} samples)')

            # Build condition
            conditions = []
            for feature_name, value in rule['conditions']:
                # Escape quotes in feature names
                safe_feature = feature_name.replace('"', '\\"')
                conditions.append(f'features.getOrDefault("{safe_feature}", 0) == {value}')

            if conditions:
                condition_str = ' &&\n            '.join(conditions)
                lines.append(f'        if ({condition_str}) {{')
            else:
                lines.append('        if (true) { // Root node')

            # Build return statement
            if include_stats:
                return_stmt = f'new PredictionResult({rule["prediction"]}, {rule["confidence"]:.3f}, {rule["rule_id"]}, {rule["samples"]}, {rule["good_count"]}, {rule["bad_count"]})'
            else:
                return_stmt = f'new PredictionResult({rule["prediction"]}, {rule["confidence"]:.3f})'

            lines.extend([
                f'            return {return_stmt};',
                '        }'
            ])

        # Add default fallback
        if include_stats:
            default_return = 'new PredictionResult(0, 0.500, -1, 0, 0, 0)'
        else:
            default_return = 'new PredictionResult(0, 0.500)'

        lines.extend([
            '',
            '        // Default fallback',
            f'        return {default_return};',
            '    }',
            '',
            '    /**',
            '     * Classify multiple samples',
            '     * @param featuresList List of feature maps',
            '     * @return List of prediction results',
            '     */',
            f'    public static List<PredictionResult> predictBatch(List<Map<String, Integer>> featuresList) {{',
            '        return featuresList.stream()',
            f'                          .map({class_name}::predict)',
            '                          .toList();',
            '    }',
            '',
            '    // Example usage',
            '    public static void main(String[] args) {',
            '        Map<String, Integer> sampleFeatures = Map.of(',
        ])

        # Add example features (limit to 3 for Java Map.of() limitation)
        example_features = self.feature_names[:3]
        for i, feature_name in enumerate(example_features):
            # Escape quotes and limit length for readability
            safe_feature = feature_name.replace('"', '\\"')
            if len(safe_feature) > 50:
                safe_feature = safe_feature[:47] + "..."
            comma = ',' if i < len(example_features) - 1 else ''
            lines.append(f'            "{safe_feature}", {i % 2}{comma}')

        lines.extend([
            '        );',
            '        ',
            '        var result = predict(sampleFeatures);',
            '        System.out.println("Prediction: " + result.prediction() + ", Confidence: " + result.confidence());',
            f'        System.out.println("Total rules in model: {len(self.rules)}");',
            '    }',
            '}'
        ])

        return '\n'.join(lines)

    def generate_cpp(self, include_stats: bool = True) -> str:
        """Generate C++ if-then-else rules"""

        lines = [
            '// Generated decision rules for classification from CART-OLAP model',
            f'// Source: {self.model_name}',
            f'// Total rules: {len(self.rules)}',
            f'// Feature count: {len(self.feature_names)}',
            '',
            '#include <unordered_map>',
            '#include <string>',
            '#include <vector>',
            '#include <iostream>',
            '',
            'struct PredictionResult {',
            '    int prediction;',
            '    double confidence;'
        ]

        if include_stats:
            lines.extend([
                '    int rule_id;',
                '    int samples;',
                '    int good_count;',
                '    int bad_count;'
            ])

        lines.extend([
            '};',
            '',
            '// Helper function to get feature value with default',
            'inline int get_feature(const std::unordered_map<std::string, int>& features, const std::string& name) {',
            '    auto it = features.find(name);',
            '    return (it != features.end()) ? it->second : 0;',
            '}',
            '',
            '/**',
            ' * Classify a single sample using decision rules',
            ' * @param features Feature map with binary values (0/1)',
            ' * @return Prediction result with confidence and metadata',
            ' */',
            'PredictionResult predict(const std::unordered_map<std::string, int>& features) {'
        ])

        # Generate rules
        for rule in self.rules:
            lines.append('')

            # Add rule comment
            conf_pct = rule['confidence'] * 100
            pred_label = "POSITIVE" if rule['prediction'] == 1 else "NEGATIVE"

            if include_stats:
                lines.append(f'    // Rule {rule["rule_id"]}: {pred_label} ({conf_pct:.1f}% confidence, {rule["samples"]} samples)')

            # Build condition
            conditions = []
            for feature_name, value in rule['conditions']:
                # Escape quotes in feature names
                safe_feature = feature_name.replace('"', '\\"')
                conditions.append(f'get_feature(features, "{safe_feature}") == {value}')

            if conditions:
                condition_str = ' &&\n        '.join(conditions)
                lines.append(f'    if ({condition_str}) {{')
            else:
                lines.append('    if (true) { // Root node')

            # Build return statement
            if include_stats:
                return_stmt = f'{{{rule["prediction"]}, {rule["confidence"]:.3f}, {rule["rule_id"]}, {rule["samples"]}, {rule["good_count"]}, {rule["bad_count"]}}}'
            else:
                return_stmt = f'{{{rule["prediction"]}, {rule["confidence"]:.3f}}}'

            lines.extend([
                f'        return {return_stmt};',
                '    }'
            ])

        # Add default fallback
        if include_stats:
            default_return = '{0, 0.500, -1, 0, 0, 0}'
        else:
            default_return = '{0, 0.500}'

        lines.extend([
            '',
            '    // Default fallback',
            f'    return {default_return};',
            '}',
            '',
            '/**',
            ' * Classify multiple samples',
            ' * @param features_list Vector of feature maps',
            ' * @return Vector of prediction results',
            ' */',
            'std::vector<PredictionResult> predict_batch(const std::vector<std::unordered_map<std::string, int>>& features_list) {',
            '    std::vector<PredictionResult> results;',
            '    results.reserve(features_list.size());',
            '    ',
            '    for (const auto& features : features_list) {',
            '        results.push_back(predict(features));',
            '    }',
            '    ',
            '    return results;',
            '}',
            '',
            '// Example usage',
            'int main() {',
            '    std::unordered_map<std::string, int> sample_features = {'
        ])

        # Add example features
        for i, feature_name in enumerate(self.feature_names[:3]):  # Show first 3 features
            safe_feature = feature_name.replace('"', '\\"')
            if len(safe_feature) > 50:
                safe_feature = safe_feature[:47] + "..."
            comma = ',' if i < min(2, len(self.feature_names) - 1) else ''
            lines.append(f'        {{"{safe_feature}", {i % 2}}}{comma}')

        lines.extend([
            '    };',
            '    ',
            '    auto result = predict(sample_features);',
            '    std::cout << "Prediction: " << result.prediction << ", Confidence: " << result.confidence << std::endl;',
            f'    std::cout << "Total rules in model: {len(self.rules)}" << std::endl;',
            '    ',
            '    return 0;',
            '}'
        ])

        return '\n'.join(lines)

    def generate_summary(self) -> str:
        """Generate summary report of the generated rules"""

        positive_rules = sum(1 for r in self.rules if r['prediction'] == 1)
        negative_rules = len(self.rules) - positive_rules

        conditions_list = [len(r['conditions']) for r in self.rules]
        avg_conditions = sum(conditions_list) / len(conditions_list) if conditions_list else 0
        max_conditions = max(conditions_list) if conditions_list else 0

        total_samples = sum(r['samples'] for r in self.rules)
        confidence_list = [r['confidence'] for r in self.rules]
        avg_confidence = sum(confidence_list) / len(confidence_list) if confidence_list else 0

        high_conf_rules = sum(1 for r in self.rules if r['confidence'] > 0.8)

        lines = [
            '# Generated CART-OLAP Decision Rules Summary',
            f'**Source Model**: {self.model_name}',
            '',
            '## Rule Statistics',
            f'- **Total Rules**: {len(self.rules)}',
            f'- **Positive Predictions**: {positive_rules} ({positive_rules/len(self.rules)*100:.1f}%)',
            f'- **Negative Predictions**: {negative_rules} ({negative_rules/len(self.rules)*100:.1f}%)',
            f'- **Average Conditions per Rule**: {avg_conditions:.1f}',
            f'- **Maximum Conditions**: {max_conditions}',
            f'- **High Confidence Rules** (>80%): {high_conf_rules} ({high_conf_rules/len(self.rules)*100:.1f}%)',
            '',
            '## Model Statistics',
            f'- **Total Training Samples**: {total_samples:,}',
            f'- **Average Rule Confidence**: {avg_confidence:.3f}',
            f'- **Feature Count**: {len(self.feature_names)}',
            f'- **Classes**: {self.classes}',
            '',
            '## Top 5 Rules by Sample Count',
            '| Rule | Prediction | Confidence | Samples | Good/Bad | Conditions |',
            '|------|------------|------------|---------|----------|------------|'
        ]

        for rule in self.rules[:5]:
            pred_label = "POSITIVE" if rule['prediction'] == 1 else "NEGATIVE"
            conditions_str = f"{len(rule['conditions'])} conditions"
            good_bad = f"{rule['good_count']}/{rule['bad_count']}"
            lines.append(f'| {rule["rule_id"]} | {pred_label} | {rule["confidence"]:.3f} | {rule["samples"]} | {good_bad} | {conditions_str} |')

        lines.extend([
            '',
            '## Usage Instructions',
            '',
            'See generated code files for usage examples in Python, Java, and C++.',
            f'',
            f'## Feature Information',
            f'Total features: {len(self.feature_names)}',
            '',
            'Example features:',
        ])

        # Show first few features as examples
        for feature in self.feature_names[:10]:
            lines.append(f'- {feature}')

        if len(self.feature_names) > 10:
            lines.append(f'- ... and {len(self.feature_names) - 10} more features')

        return '\n'.join(lines)


def main():
    parser = argparse.ArgumentParser(description='Generate if-then-else rule code from CART-OLAP decision tree model')

    parser.add_argument('--input', required=True,
                       help='Path to CART-OLAP model JSON file')
    parser.add_argument('--languages', default='python',
                       help='Comma-separated list of languages: python,java,cpp (default: python)')
    parser.add_argument('--output', required=True,
                       help='Output directory for generated files')
    parser.add_argument('--optimize_order', action='store_true', default=True,
                       help='Order rules by sample frequency for performance (default: True)')
    parser.add_argument('--include_stats', action='store_true', default=True,
                       help='Include rule statistics in generated code (default: True)')
    parser.add_argument('--class_name', default='CartOlapDecisionRules',
                       help='Class name for Java/C++ code (default: CartOlapDecisionRules)')

    args = parser.parse_args()

    # Create output directory
    output_dir = Path(args.output)
    output_dir.mkdir(parents=True, exist_ok=True)

    print(f"🎯 Generating rule code from CART-OLAP model: {args.input}")
    print(f"📁 Output directory: {args.output}")

    # Initialize generator
    generator = OlapCartRuleCodeGenerator(args.input, args.optimize_order)
    print(f"📊 Extracted {len(generator.rules)} decision rules")

    # Generate requested languages
    languages = [lang.strip() for lang in args.languages.split(',')]

    for lang in languages:
        if lang == 'python':
            print(f"🐍 Generating Python rules...")
            code = generator.generate_python(args.include_stats)
            output_file = output_dir / 'cart_olap_decision_rules.py'

        elif lang == 'java':
            print(f"☕ Generating Java rules...")
            code = generator.generate_java(args.class_name, args.include_stats)
            output_file = output_dir / f'{args.class_name}.java'

        elif lang == 'cpp':
            print(f"⚡ Generating C++ rules...")
            code = generator.generate_cpp(args.include_stats)
            output_file = output_dir / 'cart_olap_decision_rules.cpp'

        else:
            print(f"❌ Unsupported language: {lang}")
            continue

        # Write generated code
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(code)

        print(f"   ✅ Generated: {output_file}")

    # Generate summary
    print(f"📋 Generating summary...")
    summary = generator.generate_summary()
    summary_file = output_dir / 'README.md'

    with open(summary_file, 'w', encoding='utf-8') as f:
        f.write(summary)

    print(f"   ✅ Generated: {summary_file}")

    print(f"\n🎉 Rule generation completed!")
    print(f"📁 All files available in: {args.output}")


if __name__ == '__main__':
    main()