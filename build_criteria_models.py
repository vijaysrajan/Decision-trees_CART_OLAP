#!/usr/bin/env python3
"""
Build CART models for all supported criteria (gini, entropy, log_loss).

Creates JSON model files for each criterion using the same hyperparameters
to enable comparison of how different split criteria affect tree structure.
"""

import pandas as pd
import json
from pathlib import Path
import sys
import os
from datetime import datetime

# Add project root to path
project_root = Path(__file__).parent
sys.path.insert(0, str(project_root))

from cart_olap.aggregate_cart import AggregateCART

def load_hyperparameters():
    """Load hyperparameters from config or use defaults"""
    config_path = project_root / "du_config.yaml"
    if config_path.exists():
        import yaml
        with open(config_path, 'r') as f:
            config = yaml.safe_load(f)
        hyperparams = config.get('hyperparameters', {})
    else:
        # Default hyperparameters
        hyperparams = {
            'max_depth': 6,
            'min_samples_split': 100,
            'min_samples_leaf': 50,
            'min_weight_fraction_leaf': 0.0,
            'max_features': None,
            'random_state': 42,
            'max_leaf_nodes': None,
            'min_impurity_decrease': 0.0,
            'ccp_alpha': 0.0
        }

    return hyperparams

def build_model_for_criterion(df, feature_columns, good_col, bad_col, criterion, base_hyperparams):
    """Build and return a CART model for the specified criterion"""

    print(f"🏗️  Building {criterion.upper()} model...")

    # Create hyperparameters for this criterion
    hyperparams = base_hyperparams.copy()
    hyperparams['criterion'] = criterion

    # Initialize and fit the CART model
    cart = AggregateCART(**hyperparams)
    cart.fit(df, feature_columns, good_col, bad_col)

    return cart

def analyze_model(cart, criterion):
    """Analyze and print model statistics"""
    depth = cart.get_depth()
    leaves = cart.get_n_leaves()
    features = len(cart.feature_names_) if hasattr(cart, 'feature_names_') else 0

    print(f"   📊 {criterion.upper()} Model Stats:")
    print(f"      - Tree depth: {depth}")
    print(f"      - Leaves: {leaves}")
    print(f"      - Features: {features}")

    return {
        'criterion': criterion,
        'tree_depth': depth,
        'n_leaves': leaves,
        'n_features': features
    }

def save_model_with_verification(cart, output_path, criterion):
    """Save model and verify the output"""
    cart.save_json(str(output_path))

    if output_path.exists():
        file_size = output_path.stat().st_size
        print(f"   ✅ Saved to {output_path}")
        print(f"   📁 File size: {file_size:,} bytes")

        # Verify condition fields are present
        with open(output_path, 'r') as f:
            content = f.read()
            split_count = content.count('"split_condition"')
            left_count = content.count('"left_condition"')
            right_count = content.count('"right_condition"')

        print(f"   🔍 Condition fields: split={split_count}, left={left_count}, right={right_count}")
        return file_size, split_count, left_count, right_count
    else:
        print(f"   ❌ Failed to save {output_path}")
        return None, 0, 0, 0

def main():
    """Build CART models for all supported criteria"""

    print("🚀 Building CART Models for All Split Criteria")
    print("=" * 60)

    # Load the data
    data_path = project_root / "examples" / "DUAggregateData.csv"
    if not data_path.exists():
        print(f"❌ Data file not found: {data_path}")
        return 1

    df = pd.read_csv(data_path)
    print(f"📊 Loaded data with shape: {df.shape}")
    print(f"📋 Columns: {list(df.columns)}")

    # Extract feature columns (exclude target and total columns)
    feature_columns = [col for col in df.columns if col not in ['DU_Bad_Count', 'DU_good_cnt', 'total_cnt']]
    print(f"🎯 Feature columns ({len(feature_columns)}): {feature_columns}")

    # Load base hyperparameters
    base_hyperparams = load_hyperparameters()
    print(f"⚙️  Base hyperparameters: {base_hyperparams}")

    # Ensure output directory exists
    output_dir = project_root / "output"
    output_dir.mkdir(exist_ok=True)

    # Define criteria and output files
    criteria_configs = [
        ('gini', 'du_model_cli_gini.json'),
        ('entropy', 'du_model_cli_entropy.json'),
        ('log_loss', 'du_model_cli_log_loss.json')
    ]

    # Track results for comparison
    model_stats = []
    build_results = {}

    print("\n🔄 Building models for each criterion...")
    print("-" * 60)

    for criterion, filename in criteria_configs:
        try:
            # Build model
            cart = build_model_for_criterion(
                df, feature_columns, 'DU_good_cnt', 'DU_Bad_Count',
                criterion, base_hyperparams
            )

            # Analyze model
            stats = analyze_model(cart, criterion)
            model_stats.append(stats)

            # Save model
            output_path = output_dir / filename
            file_size, split_count, left_count, right_count = save_model_with_verification(
                cart, output_path, criterion
            )

            build_results[criterion] = {
                'success': file_size is not None,
                'file_size': file_size,
                'output_path': str(output_path),
                'condition_fields': {
                    'split_condition': split_count,
                    'left_condition': left_count,
                    'right_condition': right_count
                }
            }

            print()

        except Exception as e:
            print(f"   ❌ Failed to build {criterion} model: {e}")
            build_results[criterion] = {'success': False, 'error': str(e)}
            print()

    # Print comparison summary
    print("📈 Model Comparison Summary")
    print("=" * 60)

    print("| Criterion | Depth | Leaves | Features | File Size (bytes) | Status |")
    print("|-----------|--------|--------|----------|-------------------|--------|")

    for stats in model_stats:
        criterion = stats['criterion']
        result = build_results[criterion]
        status = "✅ Success" if result['success'] else "❌ Failed"
        file_size = result.get('file_size', 0) or 0

        print(f"| {criterion:<9} | {stats['tree_depth']:<6} | {stats['n_leaves']:<6} | {stats['n_features']:<8} | {file_size:>17,} | {status} |")

    # Save build metadata
    metadata = {
        'build_timestamp': datetime.now().isoformat(),
        'data_source': str(data_path),
        'base_hyperparameters': base_hyperparams,
        'criteria_built': list(build_results.keys()),
        'model_statistics': model_stats,
        'build_results': build_results
    }

    metadata_path = output_dir / "criteria_models_metadata.json"
    with open(metadata_path, 'w') as f:
        json.dump(metadata, f, indent=2)

    print(f"\n📋 Build metadata saved to: {metadata_path}")

    # Summary
    successful_builds = sum(1 for result in build_results.values() if result['success'])
    total_builds = len(build_results)

    print(f"\n🎯 Build Summary:")
    print(f"   ✅ Successful: {successful_builds}/{total_builds}")

    if successful_builds == total_builds:
        print(f"   🎉 All criteria models built successfully!")
        return 0
    else:
        print(f"   ⚠️  Some builds failed. Check error messages above.")
        return 1

if __name__ == "__main__":
    exit_code = main()
    sys.exit(exit_code)