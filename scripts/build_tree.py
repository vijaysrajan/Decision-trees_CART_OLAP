#!/usr/bin/env python3
"""
Command line script to build CART decision tree from CSV data using YAML configuration.

Usage:
    python build_tree.py <csv_file> <config_file> [options]

Arguments:
    csv_file      Path to CSV file containing aggregate data
    config_file   Path to YAML configuration file

Options:
    -o, --output <file>    Output JSON file for the trained model (default: model.json)
    -v, --verbose          Print detailed progress information
    --print-tree           Print the tree structure to console
    --no-save             Don't save the model to file

Examples:
    python scripts/build_tree.py output/DUAggregateData.csv config/config.yaml
    python scripts/build_tree.py output/data.csv config/config.yaml -o output/my_model.json --verbose
    python scripts/build_tree.py output/data.csv config/config.yaml --print-tree --no-save
"""

import sys
import argparse
import json
from pathlib import Path
import pandas as pd
import yaml

# Add the cart_olap module to the path
sys.path.insert(0, str(Path(__file__).parent.parent))

from cart_olap import AggregateCART


def load_config(config_path):
    """Load configuration from YAML file"""
    try:
        with open(config_path, 'r') as f:
            config = yaml.safe_load(f)
        return config
    except FileNotFoundError:
        raise FileNotFoundError(f"Configuration file not found: {config_path}")
    except yaml.YAMLError as e:
        raise ValueError(f"Invalid YAML configuration: {e}")


def validate_config(config):
    """Validate the configuration structure"""
    required_keys = ['features', 'target_good_col', 'target_bad_col']
    for key in required_keys:
        if key not in config:
            raise ValueError(f"Missing required configuration key: {key}")

    if not config['features']:
        raise ValueError("Features list cannot be empty")

    return True


def load_and_validate_data(csv_path, config):
    """Load CSV data and validate columns exist"""
    try:
        df = pd.read_csv(csv_path)
    except FileNotFoundError:
        raise FileNotFoundError(f"CSV file not found: {csv_path}")
    except pd.errors.EmptyDataError:
        raise ValueError(f"CSV file is empty: {csv_path}")

    # Check if required columns exist
    missing_cols = []

    # Check feature columns
    for feature in config['features']:
        if feature not in df.columns:
            missing_cols.append(feature)

    # Check target columns
    for col in [config['target_good_col'], config['target_bad_col']]:
        if col not in df.columns:
            missing_cols.append(col)

    if missing_cols:
        raise ValueError(f"Missing columns in CSV: {missing_cols}")

    return df


def create_cart_model(config):
    """Create AggregateCART model from configuration with enhanced hyperparameters"""
    # Extract hyperparameters with defaults
    hyperparams = config.get('hyperparameters', {})

    cart_params = {
        'criterion': hyperparams.get('criterion', 'gini'),
        'max_depth': hyperparams.get('max_depth'),
        'min_samples_split': hyperparams.get('min_samples_split', 2),
        'min_samples_leaf': hyperparams.get('min_samples_leaf', 1),
        'min_weight_fraction_leaf': hyperparams.get('min_weight_fraction_leaf', 0.0),
        'max_features': hyperparams.get('max_features'),
        'random_state': hyperparams.get('random_state'),
        'max_leaf_nodes': hyperparams.get('max_leaf_nodes'),
        'min_impurity_decrease': hyperparams.get('min_impurity_decrease', 0.0),
        'ccp_alpha': hyperparams.get('ccp_alpha', 0.0)
    }

    return AggregateCART(**cart_params)


def print_dataset_info(df, config, verbose=False):
    """Print information about the dataset"""
    print(f"📊 Dataset: {df.shape[0]:,} rows, {df.shape[1]} columns")

    good_col = config['target_good_col']
    bad_col = config['target_bad_col']

    total_good = df[good_col].sum()
    total_bad = df[bad_col].sum()
    total_samples = total_good + total_bad

    print(f"📈 Target distribution:")
    print(f"   Good samples: {total_good:,} ({total_good/total_samples:.1%})")
    print(f"   Bad samples:  {total_bad:,} ({total_bad/total_samples:.1%})")
    print(f"   Total:        {total_samples:,}")

    print(f"🎯 Features ({len(config['features'])}): {', '.join(config['features'])}")

    if verbose:
        print(f"\n🔍 Feature value counts:")
        for feature in config['features'][:3]:  # Show first 3 features
            unique_vals = df[feature].nunique()
            print(f"   {feature}: {unique_vals} unique values")


def print_model_info(cart, config):
    """Print information about the trained model"""
    print(f"\n🌳 Model trained successfully!")
    print(f"   Tree depth: {cart.get_depth()}")
    print(f"   Number of leaves: {cart.get_n_leaves()}")
    print(f"   Binary features created: {len(cart.feature_names_)}")

    # Show hyperparameters used
    hyperparams = config.get('hyperparameters', {})
    print(f"\n⚙️  Hyperparameters used:")
    print(f"   criterion: {hyperparams.get('criterion', 'gini')}")
    print(f"   max_depth: {hyperparams.get('max_depth', 'None')}")
    print(f"   min_samples_split: {hyperparams.get('min_samples_split', 2)}")
    print(f"   min_samples_leaf: {hyperparams.get('min_samples_leaf', 1)}")
    print(f"   max_features: {hyperparams.get('max_features', 'None')}")
    print(f"   min_impurity_decrease: {hyperparams.get('min_impurity_decrease', 0.0)}")
    print(f"   random_state: {hyperparams.get('random_state', 'None')}")


def main():
    parser = argparse.ArgumentParser(
        description='Build CART decision tree from CSV data using YAML configuration',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python build_tree.py DUAggregateData.csv config.yaml
  python build_tree.py data.csv config.yaml -o my_model.json --verbose
  python build_tree.py data.csv config.yaml --print-tree --no-save
        """
    )

    parser.add_argument('csv_file', help='Path to CSV file containing aggregate data')
    parser.add_argument('config_file', help='Path to YAML configuration file')
    parser.add_argument('-o', '--output', default='output/model.json',
                       help='Output JSON file for the trained model (default: model.json)')
    parser.add_argument('-v', '--verbose', action='store_true',
                       help='Print detailed progress information')
    parser.add_argument('--print-tree', action='store_true',
                       help='Print the tree structure to console')
    parser.add_argument('--no-save', action='store_true',
                       help="Don't save the model to file")

    args = parser.parse_args()

    try:
        # Load and validate configuration
        print(f"📋 Loading configuration from {args.config_file}...")
        config = load_config(args.config_file)
        validate_config(config)

        if args.verbose:
            print(f"✅ Configuration loaded successfully")
            print(f"   Features: {config['features']}")
            print(f"   Target columns: {config['target_good_col']}, {config['target_bad_col']}")

        # Load and validate data
        print(f"📁 Loading data from {args.csv_file}...")
        df = load_and_validate_data(args.csv_file, config)
        print(f"✅ Data loaded successfully")

        # Print dataset information
        print_dataset_info(df, config, args.verbose)

        # Create model
        print(f"\n🏗️  Creating CART model...")
        cart = create_cart_model(config)

        # Train model
        print(f"🚀 Training model...")
        cart.fit(
            df,
            config['features'],
            config['target_good_col'],
            config['target_bad_col']
        )

        # Print model information
        print_model_info(cart, config)

        # Print tree structure if requested
        if args.print_tree:
            print(f"\n🌲 Tree structure:")
            print("-" * 50)
            cart.print_tree()

        # Save model if requested
        if not args.no_save:
            print(f"\n💾 Saving model to {args.output}...")
            cart.save_json(args.output, indent=2)
            print(f"✅ Model saved successfully to {args.output}")

            # Show file size
            file_size = Path(args.output).stat().st_size / 1024  # KB
            print(f"   File size: {file_size:.1f} KB")

        print(f"\n🎉 Tree building completed successfully!")
        return 0

    except Exception as e:
        print(f"\n❌ Error: {e}")
        return 1


if __name__ == "__main__":
    sys.exit(main())