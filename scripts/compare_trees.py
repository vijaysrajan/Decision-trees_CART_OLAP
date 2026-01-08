"""
Create a tree from DUAggregateData.csv and compare with the theta sketches implementation
"""

import pandas as pd
import json
import sys
from pathlib import Path

# Add the cart_olap module to the path
sys.path.insert(0, str(Path(__file__).parent.parent))

from cart_olap import AggregateCART

def main():
    print("Creating Tree from DUAggregateData.csv")
    print("=" * 50)

    # Load the DU aggregate data
    df = pd.read_csv('output/DUAggregateData.csv')
    print(f"Data shape: {df.shape}")
    print(f"Total good samples: {df['DU_good_cnt'].sum():,}")
    print(f"Total bad samples: {df['DU_Bad_Count'].sum():,}")
    print()

    # Use similar features to the theta sketches model
    # Based on the JSON analysis: city, pickUpHourOfDay, dayType, etc.
    feature_cols = [
        'city',
        'pickUpHourOfDay',
        'dayType',
        'zone_demand_popularity',
        'booking_type',
        'sla'
    ]

    print(f"Using features: {feature_cols}")
    print()

    # Create tree with similar parameters to theta sketches
    cart = AggregateCART(
        max_depth=6,  # Match the theta sketches depth
        min_samples_leaf=20,
        min_impurity_decrease=0.001
    )

    print("Training tree...")
    cart.fit(df, feature_cols, 'DU_good_cnt', 'DU_Bad_Count')

    print(f"✅ Tree created!")
    print(f"Tree depth: {cart.get_depth()}")
    print(f"Number of leaves: {cart.get_n_leaves()}")
    print(f"Total samples processed: {df['DU_good_cnt'].sum() + df['DU_Bad_Count'].sum():,}")
    print()

    # Export to JSON for comparison
    output_file = "output/our_du_tree_model.json"
    cart.save_json(output_file, indent=2)
    print(f"✅ Exported tree to {output_file}")
    print()

    # Show tree structure preview
    print("Tree structure preview:")
    print("-" * 30)
    cart.print_tree()
    print()

    # Show first few lines of our JSON for comparison
    with open(output_file, 'r') as f:
        our_json = f.read()

    print("Our JSON structure (first 1000 chars):")
    print("-" * 40)
    print(our_json[:1000] + "...")
    print()

    # Compare key metrics
    our_tree_json = json.loads(our_json)
    print("Our tree metrics:")
    print(f"  - Features used: {len(cart.feature_names_)} binary features from {len(feature_cols)} original")
    print(f"  - Tree depth: {our_tree_json['model_info']['tree_depth']}")
    print(f"  - Number of leaves: {our_tree_json['model_info']['n_leaves']}")
    print(f"  - Original features: {our_tree_json['model_info']['feature_names'][:3]}...")  # Show first 3
    print()

    print("Key differences to check:")
    print("1. Feature encoding: One-hot vs direct categorical")
    print("2. Split logic: True/False vs exact value matching")
    print("3. Tree structure: Binary splits vs multi-way")
    print("4. Sample counts: Aggregate totals vs theta sketch approximations")

if __name__ == "__main__":
    main()