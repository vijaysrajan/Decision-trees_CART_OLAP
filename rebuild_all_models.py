#!/usr/bin/env python3
"""
Rebuild all model files with the new condition fields and consistent hyperparameters.
"""

import pandas as pd
from cart_olap import AggregateCART
from pathlib import Path

def rebuild_models():
    """Rebuild all models with consistent hyperparameters."""

    # Load data
    data_path = "examples/DUAggregateData.csv"
    print(f"Loading data from: {data_path}")

    # Load the CSV file
    df = pd.read_csv(data_path)

    # Check if the dataset contains aggregated data
    if 'DU_good_cnt' in df.columns and 'DU_Bad_Count' in df.columns:
        print("Dataset contains aggregated data")
        # Define feature columns as in the working example
        feature_columns = [
            'source',
            'estimated_usage_bins',
            'city',
            'zone_demand_popularity',
            'dayType',
            'pickUpHourOfDay',
            'sla',
            'booking_type'
        ]

        # Total samples and good/bad counts
        total_good = df['DU_good_cnt'].sum()
        total_bad = df['DU_Bad_Count'].sum()
        print(f"Total good samples: {total_good:,}")
        print(f"Total bad samples: {total_bad:,}")
    else:
        raise ValueError(f"Expected aggregated dataset with 'DU_good_cnt' and 'DU_Bad_Count' columns. Found: {df.columns.tolist()}")

    print(f"Data shape: {df.shape}")
    print(f"Training with {len(feature_columns)} features: {feature_columns}")

    # Standard hyperparameters matching du_config.yaml
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

    print(f"\nTraining with hyperparameters:")
    for key, value in hyperparams.items():
        print(f"  {key}: {value}")

    # Initialize and train the model
    cart = AggregateCART(**hyperparams)
    print(f"\nPerforming one-hot encoding of categorical features...")
    cart.fit(df, feature_columns, 'DU_good_cnt', 'DU_Bad_Count')
    print(f"✅ Training complete!")
    print(f"Binary features after encoding: {len(cart.feature_names_)}")
    print(f"Tree depth: {cart.get_depth()}")
    print(f"Number of leaves: {cart.get_n_leaves()}")

    # Models to generate
    models_to_generate = [
        ("output/du_model_cli.json", "Main CLI model"),
        ("output/du_model_cli_cart_sketch_compatible.json", "CART-sketch compatible format"),
        ("output/du_model_cli_enhanced_format.json", "Enhanced format"),
        ("output/du_model_cli_compact.json", "Compact format"),
        ("output/du_model_gini_enhanced.json", "Gini enhanced model"),
        ("output/test_model.json", "Test model"),
        ("output/du_model_final.json", "Final model")
    ]

    print(f"\nGenerating {len(models_to_generate)} model files...")

    for filepath, description in models_to_generate:
        print(f"\n📄 Generating {description}: {filepath}")
        cart.save_json(filepath, indent=2)

        # Get file size for verification
        file_size = Path(filepath).stat().st_size
        print(f"✅ Saved successfully - Size: {file_size:,} bytes ({file_size/1024:.1f} KB)")

    print(f"\n🎉 All models rebuilt successfully!")

    # Verify condition fields are present
    print(f"\n🔍 Verifying condition fields in main model...")
    with open("output/du_model_cli.json", 'r') as f:
        content = f.read()

    condition_fields = ['split_condition', 'left_condition', 'right_condition']
    for field in condition_fields:
        count = content.count(f'"{field}":')
        print(f"  {field}: {count} occurrences")

    if all(content.count(f'"{field}":') > 0 for field in condition_fields):
        print("✅ All condition fields verified!")
    else:
        print("❌ Some condition fields missing!")

if __name__ == "__main__":
    rebuild_models()