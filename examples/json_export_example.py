"""
Example demonstrating JSON export and import functionality for AggregateCART.

This example shows how to:
1. Train a tree on aggregate data
2. Export the tree to JSON format
3. Save the tree to a JSON file
4. Load the tree from JSON and verify it works
"""

import pandas as pd
import sys
from pathlib import Path

# Add parent directory to path for imports
sys.path.append(str(Path(__file__).parent.parent))

from cart_olap import AggregateCART


def create_sample_data():
    """Create a small sample dataset for demonstration."""
    return pd.DataFrame({
        'platform': ['ios', 'ios', 'android', 'android', 'web', 'web'],
        'city': ['NYC', 'SF', 'NYC', 'SF', 'NYC', 'SF'],
        'time': ['morning', 'evening', 'morning', 'evening', 'morning', 'evening'],
        'good_count': [150, 120, 80, 60, 40, 30],
        'bad_count': [50, 80, 120, 140, 160, 170],
        'total_count': [200, 200, 200, 200, 200, 200]
    })


def main():
    print("JSON Export/Import Example for AggregateCART")
    print("=" * 50)

    # Create sample data
    data = create_sample_data()
    print(f"Training data shape: {data.shape}")
    print(f"Features: platform, city, time")
    print(f"Total samples: {data['total_count'].sum()}")
    print()

    # Train the model
    feature_cols = ['platform', 'city', 'time']
    cart = AggregateCART(max_depth=4, min_samples_leaf=10)

    print("Training AggregateCART...")
    cart.fit(data, feature_cols, 'good_count', 'bad_count')

    print(f"Tree depth: {cart.get_depth()}")
    print(f"Number of leaves: {cart.get_n_leaves()}")
    print()

    # Export to JSON string
    print("Exporting tree to JSON...")
    json_str = cart.to_json(indent=2)
    print(f"JSON length: {len(json_str)} characters")
    print()

    # Show a snippet of the JSON
    print("JSON snippet (first 500 characters):")
    print(json_str[:500] + "...")
    print()

    # Save to file
    json_file = "trained_cart_model.json"
    cart.save_json(json_file)
    print(f"✅ Saved tree to {json_file}")
    print()

    # Load from file
    print("Loading tree from JSON file...")
    loaded_cart = AggregateCART.load_json(json_file)
    print(f"✅ Loaded tree successfully")
    print(f"Loaded tree depth: {loaded_cart.get_depth()}")
    print(f"Loaded tree leaves: {loaded_cart.get_n_leaves()}")
    print(f"Feature names: {loaded_cart.feature_names_}")
    print()

    # Test predictions to verify they match
    test_data = pd.DataFrame({
        'platform': ['ios', 'android', 'web'],
        'city': ['NYC', 'SF', 'NYC'],
        'time': ['morning', 'evening', 'morning']
    })

    print("Testing predictions on both models...")
    original_predictions = cart.predict(test_data)
    loaded_predictions = loaded_cart.predict(test_data)

    original_proba = cart.predict_proba(test_data)
    loaded_proba = loaded_cart.predict_proba(test_data)

    print("\nComparison Results:")
    print("-" * 30)
    for i, (idx, row) in enumerate(test_data.iterrows()):
        print(f"Sample {i+1}: {dict(row)}")
        print(f"  Original: prediction={original_predictions[i]}, proba={original_proba[i]}")
        print(f"  Loaded:   prediction={loaded_predictions[i]}, proba={loaded_proba[i]}")
        print(f"  Match: {original_predictions[i] == loaded_predictions[i] and all(abs(a-b) < 1e-10 for a,b in zip(original_proba[i], loaded_proba[i]))}")
        print()

    # Clean up
    import os
    if os.path.exists(json_file):
        os.remove(json_file)
        print(f"🧹 Cleaned up {json_file}")

    print("✅ JSON export/import example completed successfully!")


if __name__ == "__main__":
    main()