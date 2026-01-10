#!/usr/bin/env python3
"""
Build CART tree for DUAggregateData.csv and save to du_model_cli.json
"""

import pandas as pd
import json
from pathlib import Path
import sys
import os

# Add project root to path
project_root = Path(__file__).parent
sys.path.insert(0, str(project_root))

from cart_olap.aggregate_cart import AggregateCART

def main():
    """Build CART tree and save to du_model_cli.json"""

    # Load the data
    data_path = project_root / "examples" / "DUAggregateData.csv"
    df = pd.read_csv(data_path)

    print(f"Loaded data with shape: {df.shape}")
    print(f"Columns: {list(df.columns)}")

    # Extract feature columns (exclude target and total columns)
    feature_columns = [col for col in df.columns if col not in ['DU_Bad_Count', 'DU_good_cnt', 'total_cnt']]
    print(f"Feature columns ({len(feature_columns)}): {feature_columns}")

    # Load hyperparameters from config
    config_path = project_root / "du_config.yaml"
    if config_path.exists():
        import yaml
        with open(config_path, 'r') as f:
            config = yaml.safe_load(f)
        hyperparams = config.get('hyperparameters', {})
    else:
        # Default hyperparameters
        hyperparams = {
            'criterion': 'gini',
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

    print(f"Using hyperparameters: {hyperparams}")

    # Initialize and fit the CART model
    cart = AggregateCART(**hyperparams)
    cart.fit(df, feature_columns, 'DU_good_cnt', 'DU_Bad_Count')

    # Export to JSON
    output_path = project_root / "output" / "du_model_cli.json"
    cart.save_json(str(output_path))

    # Verify the output
    if output_path.exists():
        file_size = output_path.stat().st_size
        print(f"✅ Successfully created {output_path}")
        print(f"📁 File size: {file_size:,} bytes")

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
    else:
        print(f"❌ Failed to create {output_path}")

if __name__ == "__main__":
    main()