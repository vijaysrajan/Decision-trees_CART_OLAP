"""
Export the DU (Demand-Utilization) tree to JSON format.

This script trains a CART tree on the DUAggregateData.csv and exports it to JSON.
"""

import pandas as pd
import sys
from pathlib import Path

# Add parent directory to path for imports
sys.path.append(str(Path(__file__).parent.parent))

from cart_olap import AggregateCART


def main():
    print("Exporting DU Tree to JSON")
    print("=" * 40)

    # Load the DU aggregate data
    data_path = Path(__file__).parent / "DUAggregateData.csv"
    print(f"Loading data from: {data_path}")

    df = pd.read_csv(data_path)
    print(f"Data shape: {df.shape}")
    print(f"Total good samples: {df['DU_good_cnt'].sum():,}")
    print(f"Total bad samples: {df['DU_Bad_Count'].sum():,}")
    print()

    # Define features
    feature_cols = [
        'source',
        'estimated_usage_bins',
        'city',
        'zone_demand_popularity',
        'dayType',
        'pickUpHourOfDay',
        'sla',
        'booking_type'
    ]

    print(f"Training tree with {len(feature_cols)} features...")

    # Train tree with hyperparameters matching du_config.yaml from CART_sketch
    cart = AggregateCART(
        criterion='gini',
        max_depth=6,
        min_samples_split=100,
        min_samples_leaf=50,
        min_impurity_decrease=0.0,
        random_state=42
    )

    cart.fit(df, feature_cols, 'DU_good_cnt', 'DU_Bad_Count')

    print(f"✅ Training complete!")
    print(f"Tree depth: {cart.get_depth()}")
    print(f"Number of leaves: {cart.get_n_leaves()}")
    print()

    # Export to JSON
    output_file = "DU_tree_model.json"
    print(f"Exporting tree to {output_file}...")

    cart.save_json(output_file, indent=2)

    # Check file size
    import os
    file_size = os.path.getsize(output_file)
    print(f"✅ Exported successfully!")
    print(f"File size: {file_size:,} bytes ({file_size/1024:.1f} KB)")
    print()

    # Show a sample of the JSON structure
    json_str = cart.to_json(indent=2)
    lines = json_str.split('\n')

    print("JSON structure preview (first 20 lines):")
    print("-" * 40)
    for i, line in enumerate(lines[:20]):
        print(f"{i+1:2d}: {line}")

    if len(lines) > 20:
        print("...")
        print(f"Total lines: {len(lines)}")

    print()
    print(f"✅ DU tree exported to {output_file}")
    print("\nTo load this tree later:")
    print("  from cart_olap import AggregateCART")
    print(f"  cart = AggregateCART.load_json('{output_file}')")


if __name__ == "__main__":
    main()