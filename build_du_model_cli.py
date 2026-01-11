#!/usr/bin/env python3
"""
Build CART tree for DUAggregateData.csv with support for different split criteria.

Supports gini, entropy, and log_loss criteria. Output filename includes criterion name.

Usage:
    python build_du_model_cli.py                    # Uses gini (default)
    python build_du_model_cli.py --criterion gini   # Uses gini explicitly
    python build_du_model_cli.py --criterion entropy # Uses entropy
    python build_du_model_cli.py --criterion log_loss # Uses log_loss
"""

import pandas as pd
import json
import argparse
from pathlib import Path
import sys
import os

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

    # Remove criterion if present in config (will be set by command line)
    hyperparams.pop('criterion', None)
    return hyperparams

def build_model(criterion='gini', output_filename=None):
    """Build CART tree with specified criterion"""

    print(f"🚀 Building CART Model with {criterion.upper()} criterion")
    print("=" * 50)

    # Load the data
    data_path = project_root / "examples" / "DUAggregateData.csv"
    if not data_path.exists():
        print(f"❌ Data file not found: {data_path}")
        return False

    df = pd.read_csv(data_path)
    print(f"📊 Loaded data with shape: {df.shape}")
    print(f"📋 Columns: {list(df.columns)}")

    # Extract feature columns (exclude target and total columns)
    feature_columns = [col for col in df.columns if col not in ['DU_Bad_Count', 'DU_good_cnt', 'total_cnt']]
    print(f"🎯 Feature columns ({len(feature_columns)}): {feature_columns}")

    # Load base hyperparameters and add criterion
    hyperparams = load_hyperparameters()
    hyperparams['criterion'] = criterion

    print(f"⚙️  Using hyperparameters: {hyperparams}")

    # Initialize and fit the CART model
    print(f"🏗️  Building model...")
    cart = AggregateCART(**hyperparams)
    cart.fit(df, feature_columns, 'DU_good_cnt', 'DU_Bad_Count')

    # Determine output filename
    if output_filename is None:
        if criterion == 'gini':
            output_filename = 'du_model_cli.json'  # Default for backwards compatibility
        else:
            output_filename = f'du_model_cli_{criterion}.json'

    # Export to JSON
    output_path = project_root / "output" / output_filename
    cart.save_json(str(output_path))

    # Verify the output
    if output_path.exists():
        file_size = output_path.stat().st_size
        print(f"✅ Successfully created {output_path}")
        print(f"📁 File size: {file_size:,} bytes")

        # Print model statistics
        depth = cart.get_depth()
        leaves = cart.get_n_leaves()
        features = len(cart.feature_names_) if hasattr(cart, 'feature_names_') else 0

        print(f"📊 Model Statistics:")
        print(f"   - Criterion: {criterion}")
        print(f"   - Tree depth: {depth}")
        print(f"   - Number of leaves: {leaves}")
        print(f"   - Binary features: {features}")

        # Verify condition fields are present
        with open(output_path, 'r') as f:
            content = f.read()
            split_count = content.count('"split_condition"')
            left_count = content.count('"left_condition"')
            right_count = content.count('"right_condition"')

        print(f"🔍 Condition fields verification:")
        print(f"   - split_condition: {split_count} occurrences")
        print(f"   - left_condition: {left_count} occurrences")
        print(f"   - right_condition: {right_count} occurrences")

        return True
    else:
        print(f"❌ Failed to create {output_path}")
        return False

def main():
    """Main function with argument parsing"""
    parser = argparse.ArgumentParser(
        description='Build CART tree with different split criteria',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python build_du_model_cli.py                    # Build with gini (default)
  python build_du_model_cli.py --criterion entropy # Build with entropy
  python build_du_model_cli.py --criterion log_loss # Build with log_loss
  python build_du_model_cli.py --output custom.json # Custom output filename
  python build_du_model_cli.py --all              # Build all criteria
        """
    )

    parser.add_argument(
        '--criterion',
        choices=['gini', 'entropy', 'log_loss'],
        default='gini',
        help='Split criterion to use (default: gini)'
    )

    parser.add_argument(
        '--output',
        help='Output filename (default: du_model_cli_{criterion}.json)'
    )

    parser.add_argument(
        '--all',
        action='store_true',
        help='Build models for all criteria (gini, entropy, log_loss)'
    )

    args = parser.parse_args()

    if args.all:
        print("🔄 Building models for all criteria...")
        criteria = ['gini', 'entropy', 'log_loss']
        success_count = 0

        for criterion in criteria:
            print(f"\n{'='*60}")
            if build_model(criterion):
                success_count += 1
            print()

        print(f"🎯 Summary: {success_count}/{len(criteria)} models built successfully")
        return success_count == len(criteria)
    else:
        return build_model(args.criterion, args.output)

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)