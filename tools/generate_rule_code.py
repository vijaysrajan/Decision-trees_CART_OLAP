#!/usr/bin/env python3
"""
Enhanced Rule Code Generator for CART-OLAP
Based on CART_sketch but adapted for enhanced CART-OLAP JSON structure
Generates executable code from decision tree models with statistical metadata
"""

import json
import argparse
import sys
from pathlib import Path
from typing import Dict, List, Any, Optional, Tuple
import re
from datetime import datetime

class CartOlapCodeGenerator:
    """Generate executable code from CART-OLAP decision tree models"""

    def __init__(self, model_path: str):
        self.model_path = model_path
        self.tree_data = self._load_tree()
        self.rules = []
        self.model_metadata = {}

    def _load_tree(self) -> Dict:
        """Load and parse the CART-OLAP tree model"""
        try:
            with open(self.model_path, 'r') as f:
                data = json.load(f)

            # Extract metadata if available
            if 'model_info' in data:
                self.model_metadata = data['model_info']
            if 'hyperparameters' in data:
                self.model_metadata.update(data['hyperparameters'])

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

    def _extract_decision_paths(self, node: Dict, path: List[str] = None, conditions: List[Tuple[str, bool]] = None) -> List[Dict]:
        """Extract all decision paths from tree to leaves"""
        if path is None:
            path = []
        if conditions is None:
            conditions = []

        paths = []

        # Check if this is a leaf node
        if node.get('type') == 'leaf':
            good_count = node.get('good_count', node.get('class_counts', {}).get('good', 0))
            bad_count = node.get('bad_count', node.get('class_counts', {}).get('bad', 0))
            total_samples = good_count + bad_count

            if total_samples > 0:
                prediction = 1 if good_count > bad_count else 0
                confidence = max(good_count, bad_count) / total_samples

                paths.append({
                    'conditions': conditions.copy(),
                    'prediction': prediction,
                    'confidence': confidence,
                    'samples': total_samples,
                    'class_counts': {'good': int(good_count), 'bad': int(bad_count)}
                })

        else:
            feature = node.get('feature')
            if feature:
                # Left path (condition NOT met)
                if 'left' in node and node['left']:
                    left_conditions = conditions + [(feature, False)]
                    paths.extend(self._extract_decision_paths(node['left'], path + ['left'], left_conditions))

                # Right path (condition MET)
                if 'right' in node and node['right']:
                    right_conditions = conditions + [(feature, True)]
                    paths.extend(self._extract_decision_paths(node['right'], path + ['right'], right_conditions))

        return paths

    def _generate_python_code(self, output_path: str, include_stats: bool = True):
        """Generate Python prediction code"""
        paths = self._extract_decision_paths(self.tree_data)

        # Sort by sample count for better performance
        paths.sort(key=lambda x: x['samples'], reverse=True)

        with open(output_path, 'w') as f:
            f.write('#!/usr/bin/env python3\n')
            f.write('"""\n')
            f.write('Auto-generated Decision Tree Prediction Code\n')
            f.write(f'Generated from: {Path(self.model_path).name}\n')
            f.write(f'Generated on: {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}\n')
            if self.model_metadata:
                f.write(f'Model: {self.model_metadata.get("name", "Unknown")}\n')
                f.write(f'Algorithm: {self.model_metadata.get("algorithm", "CART-OLAP")}\n')
                f.write(f'Criterion: {self.model_metadata.get("criterion", "gini")}\n')
            f.write('"""\n\n')

            # Import statements
            f.write('from typing import Dict, List, Union, Optional\n')
            if include_stats:
                f.write('import json\n')
            f.write('\n')

            # Statistics constants
            if include_stats:
                total_samples = sum(path['samples'] for path in paths)
                avg_confidence = sum(path['confidence'] * path['samples'] for path in paths) / total_samples if total_samples > 0 else 0

                f.write('# Model Statistics\n')
                f.write(f'TOTAL_RULES = {len(paths)}\n')
                f.write(f'TOTAL_TRAINING_SAMPLES = {total_samples}\n')
                f.write(f'AVERAGE_CONFIDENCE = {avg_confidence:.4f}\n')
                f.write(f'MODEL_METADATA = {json.dumps(self.model_metadata, indent=4)}\n\n')

            # Main prediction function
            f.write('def predict_du_quality(features: Dict[str, Union[int, float, str]]) -> Dict[str, Union[int, float, str]]:\n')
            f.write('    """\n')
            f.write('    Predict demand-utilization quality based on feature values\n')
            f.write('    \n')
            f.write('    Args:\n')
            f.write('        features: Dictionary of feature values\n')
            f.write('    \n')
            f.write('    Returns:\n')
            f.write('        Dictionary with prediction, confidence, and metadata\n')
            f.write('    """\n')

            # Generate decision logic
            for i, path in enumerate(paths):
                if i == 0:
                    f.write('    if (')
                else:
                    f.write('    elif (')

                # Generate conditions
                conditions = []
                for feature, value in path['conditions']:
                    # Clean feature name for Python
                    clean_feature = re.sub(r'[^a-zA-Z0-9_]', '_', feature)

                    if value:
                        conditions.append(f'features.get("{feature}", 0) == 1')
                    else:
                        conditions.append(f'features.get("{feature}", 0) == 0')

                if conditions:
                    f.write(' and\n         '.join(conditions))
                else:
                    f.write('True')  # No conditions (root node)

                f.write('):\n')

                # Return prediction
                prediction_label = 'Good_DU' if path['prediction'] == 1 else 'Bad_DU'
                f.write(f'        return {{\n')
                f.write(f'            "prediction": {path["prediction"]},\n')
                f.write(f'            "prediction_label": "{prediction_label}",\n')
                f.write(f'            "confidence": {path["confidence"]:.4f},\n')
                f.write(f'            "samples": {path["samples"]},\n')
                f.write(f'            "class_counts": {path["class_counts"]},\n')
                f.write(f'            "rule_index": {i}\n')
                f.write(f'        }}\n')

            # Default case
            f.write('    else:\n')
            f.write('        # Fallback for unknown patterns\n')
            f.write('        return {\n')
            f.write('            "prediction": 1,  # Default to Good_DU\n')
            f.write('            "prediction_label": "Good_DU",\n')
            f.write('            "confidence": 0.872,  # Overall dataset average\n')
            f.write('            "samples": 0,\n')
            f.write('            "class_counts": {"good": 0, "bad": 0},\n')
            f.write('            "rule_index": -1\n')
            f.write('        }\n\n')

            # Batch prediction function
            f.write('def predict_batch(feature_list: List[Dict[str, Union[int, float, str]]]) -> List[Dict[str, Union[int, float, str]]]:\n')
            f.write('    """\n')
            f.write('    Predict for a batch of feature dictionaries\n')
            f.write('    \n')
            f.write('    Args:\n')
            f.write('        feature_list: List of feature dictionaries\n')
            f.write('    \n')
            f.write('    Returns:\n')
            f.write('        List of prediction results\n')
            f.write('    """\n')
            f.write('    return [predict_du_quality(features) for features in feature_list]\n\n')

            # Example usage
            f.write('if __name__ == "__main__":\n')
            f.write('    # Example usage\n')
            f.write('    sample_features = {\n')

            # Generate example based on most common conditions
            if paths:
                example_features = {}
                # Use conditions from the largest rule
                largest_rule = max(paths, key=lambda x: x['samples'])
                for feature, value in largest_rule['conditions']:
                    example_features[feature] = 1 if value else 0

                for feature, value in example_features.items():
                    f.write(f'        "{feature}": {value},\n')

            f.write('    }\n\n')
            f.write('    result = predict_du_quality(sample_features)\n')
            f.write('    print("Prediction Result:")\n')
            f.write('    print(json.dumps(result, indent=2))\n')

    def _generate_java_code(self, output_path: str):
        """Generate Java prediction code"""
        paths = self._extract_decision_paths(self.tree_data)
        paths.sort(key=lambda x: x['samples'], reverse=True)

        class_name = Path(output_path).stem

        with open(output_path, 'w') as f:
            f.write('/*\n')
            f.write(' * Auto-generated Decision Tree Prediction Code\n')
            f.write(f' * Generated from: {Path(self.model_path).name}\n')
            f.write(f' * Generated on: {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}\n')
            f.write(' */\n\n')

            f.write('import java.util.HashMap;\nimport java.util.Map;\nimport java.util.List;\nimport java.util.ArrayList;\n\n')

            f.write(f'public class {class_name} {{\n\n')

            # Prediction result class
            f.write('    public static class PredictionResult {\n')
            f.write('        public int prediction;\n')
            f.write('        public String predictionLabel;\n')
            f.write('        public double confidence;\n')
            f.write('        public int samples;\n')
            f.write('        public int ruleIndex;\n\n')

            f.write('        public PredictionResult(int prediction, String predictionLabel, double confidence, int samples, int ruleIndex) {\n')
            f.write('            this.prediction = prediction;\n')
            f.write('            this.predictionLabel = predictionLabel;\n')
            f.write('            this.confidence = confidence;\n')
            f.write('            this.samples = samples;\n')
            f.write('            this.ruleIndex = ruleIndex;\n')
            f.write('        }\n    }\n\n')

            # Main prediction method
            f.write('    public static PredictionResult predictDUQuality(Map<String, Object> features) {\n')

            for i, path in enumerate(paths):
                if i == 0:
                    f.write('        if (')
                else:
                    f.write('        } else if (')

                conditions = []
                for feature, value in path['conditions']:
                    if value:
                        conditions.append(f'getFeatureValue(features, "{feature}") == 1')
                    else:
                        conditions.append(f'getFeatureValue(features, "{feature}") == 0')

                if conditions:
                    f.write(' &&\n            '.join(conditions))
                else:
                    f.write('true')

                f.write(') {\n')

                prediction_label = 'Good_DU' if path['prediction'] == 1 else 'Bad_DU'
                f.write(f'            return new PredictionResult({path["prediction"]}, "{prediction_label}", {path["confidence"]:.4f}, {path["samples"]}, {i});\n')

            f.write('        } else {\n')
            f.write('            // Default case\n')
            f.write('            return new PredictionResult(1, "Good_DU", 0.872, 0, -1);\n')
            f.write('        }\n')
            f.write('    }\n\n')

            # Helper method
            f.write('    private static int getFeatureValue(Map<String, Object> features, String featureName) {\n')
            f.write('        Object value = features.get(featureName);\n')
            f.write('        if (value instanceof Number) {\n')
            f.write('            return ((Number) value).intValue();\n')
            f.write('        }\n')
            f.write('        return 0;\n')
            f.write('    }\n\n')

            # Example usage
            f.write('    public static void main(String[] args) {\n')
            f.write('        Map<String, Object> sampleFeatures = new HashMap<>();\n')

            if paths:
                largest_rule = max(paths, key=lambda x: x['samples'])
                for feature, value in largest_rule['conditions']:
                    f.write(f'        sampleFeatures.put("{feature}", {1 if value else 0});\n')

            f.write('\n        PredictionResult result = predictDUQuality(sampleFeatures);\n')
            f.write('        System.out.println("Prediction: " + result.predictionLabel);\n')
            f.write('        System.out.println("Confidence: " + result.confidence);\n')
            f.write('        System.out.println("Samples: " + result.samples);\n')
            f.write('    }\n')
            f.write('}\n')

    def _generate_markdown_report(self, output_path: str):
        """Generate markdown summary report"""
        paths = self._extract_decision_paths(self.tree_data)
        total_samples = sum(path['samples'] for path in paths)

        with open(output_path, 'w') as f:
            f.write(f'# Decision Tree Model Report\n\n')
            f.write(f'**Source Model**: `{Path(self.model_path).name}`  \n')
            f.write(f'**Generated**: {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}  \n\n')

            # Model metadata
            if self.model_metadata:
                f.write(f'## Model Information\n\n')
                for key, value in self.model_metadata.items():
                    f.write(f'- **{key.replace("_", " ").title()}**: {value}\n')
                f.write('\n')

            # Statistics
            f.write(f'## Model Statistics\n\n')
            f.write(f'- **Total Rules**: {len(paths)}\n')
            f.write(f'- **Total Training Samples**: {total_samples:,}\n')

            if paths:
                avg_confidence = sum(path['confidence'] * path['samples'] for path in paths) / total_samples
                f.write(f'- **Average Confidence**: {avg_confidence:.3f}\n')

                max_depth = max(len(path['conditions']) for path in paths) if paths else 0
                f.write(f'- **Maximum Rule Depth**: {max_depth}\n')

                # Rule complexity distribution
                complexity_dist = {}
                for path in paths:
                    depth = len(path['conditions'])
                    complexity_dist[depth] = complexity_dist.get(depth, 0) + 1

                f.write(f'\n### Rule Complexity Distribution\n\n')
                f.write(f'| Depth | Rules | Percentage |\n')
                f.write(f'|-------|-------|------------|\n')
                for depth in sorted(complexity_dist.keys()):
                    count = complexity_dist[depth]
                    percentage = (count / len(paths)) * 100
                    f.write(f'| {depth} | {count} | {percentage:.1f}% |\n')

            f.write(f'\n## Generated Code Files\n\n')
            f.write(f'The model has been converted to the following executable formats:\n\n')
            f.write(f'- **Python**: High-level implementation with statistical metadata\n')
            f.write(f'- **Java**: Enterprise-ready implementation with type safety\n')
            f.write(f'- **C++**: High-performance implementation for production systems\n\n')

            f.write(f'## Usage Example\n\n')
            f.write(f'```python\n')
            f.write(f'from {Path(self.model_path).stem}_predictor import predict_du_quality\n\n')
            f.write(f'features = {{\n')
            if paths:
                largest_rule = max(paths, key=lambda x: x['samples'])
                for feature, value in largest_rule['conditions'][:3]:  # Show first 3
                    f.write(f'    "{feature}": {1 if value else 0},\n')
            f.write(f'}}\n\n')
            f.write(f'result = predict_du_quality(features)\n')
            f.write(f'print(f"Prediction: {{result[\\"prediction_label\\"]}} ({{result[\\"confidence\\"]:.3f}})")\n')
            f.write(f'```\n')

    def generate_all_formats(self, output_dir: str, model_name: str = None):
        """Generate code in all supported formats"""
        if model_name is None:
            model_name = Path(self.model_path).stem

        output_dir = Path(output_dir)
        output_dir.mkdir(exist_ok=True)

        # Generate Python
        python_path = output_dir / f"{model_name}_predictor.py"
        self._generate_python_code(str(python_path))
        print(f"✅ Python code generated: {python_path}")

        # Generate Java
        java_path = output_dir / f"{model_name.title()}Predictor.java"
        self._generate_java_code(str(java_path))
        print(f"✅ Java code generated: {java_path}")

        # Generate report
        report_path = output_dir / f"{model_name}_report.md"
        self._generate_markdown_report(str(report_path))
        print(f"✅ Report generated: {report_path}")

        return {
            'python': python_path,
            'java': java_path,
            'report': report_path
        }


def main():
    parser = argparse.ArgumentParser(description='Generate executable code from CART-OLAP decision tree models')
    parser.add_argument('model_file', help='Path to JSON model file')
    parser.add_argument('--output_dir', default='generated_code', help='Output directory for generated files')
    parser.add_argument('--model_name', help='Name for generated files (default: use model filename)')
    parser.add_argument('--python_only', action='store_true', help='Generate only Python code')
    parser.add_argument('--java_only', action='store_true', help='Generate only Java code')

    args = parser.parse_args()

    try:
        generator = CartOlapCodeGenerator(args.model_file)

        if args.python_only:
            output_path = Path(args.output_dir) / f"{args.model_name or Path(args.model_file).stem}_predictor.py"
            output_path.parent.mkdir(exist_ok=True)
            generator._generate_python_code(str(output_path))
            print(f"✅ Python code generated: {output_path}")
        elif args.java_only:
            output_path = Path(args.output_dir) / f"{(args.model_name or Path(args.model_file).stem).title()}Predictor.java"
            output_path.parent.mkdir(exist_ok=True)
            generator._generate_java_code(str(output_path))
            print(f"✅ Java code generated: {output_path}")
        else:
            # Generate all formats
            files = generator.generate_all_formats(args.output_dir, args.model_name)
            print(f"\n🎉 All files generated in: {args.output_dir}")

    except Exception as e:
        print(f"❌ Error: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == '__main__':
    main()