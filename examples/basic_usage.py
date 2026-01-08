"""
Basic usage example of AggregateCART for ride-hailing demand-utilization prediction.

This example demonstrates how to:
1. Load aggregate OLAP cube data
2. Train a CART decision tree
3. Make predictions on new samples
4. Analyze the trained model
"""

import pandas as pd
import numpy as np
from pathlib import Path

# Add parent directory to path for imports
import sys
sys.path.append(str(Path(__file__).parent.parent))

from cart_olap import AggregateCART


def load_sample_data():
    """Load the DU (Demand-Utilization) aggregate data."""
    data_path = Path(__file__).parent / "DUAggregateData.csv"
    df = pd.read_csv(data_path)

    print(f"Loaded {len(df)} aggregate rows")
    print(f"Total good samples: {df['DU_good_cnt'].sum()}")
    print(f"Total bad samples: {df['DU_Bad_Count'].sum()}")
    print(f"Overall good rate: {df['DU_good_cnt'].sum() / (df['DU_good_cnt'].sum() + df['DU_Bad_Count'].sum()):.3f}")

    return df


def basic_training_example():
    """Basic training and prediction example."""
    print("=" * 60)
    print("BASIC TRAINING EXAMPLE")
    print("=" * 60)

    # Load data
    df = load_sample_data()

    # Define features (all categorical features in the dataset)
    feature_cols = [
        'source',                    # ios/android/Phone
        'estimated_usage_bins',      # LTE_1_HOUR/GT_1_LTE_2_HOURS/etc
        'city',                      # Bangalore/Mumbai/Delhi NCR/etc
        'zone',                      # Zone ID (numeric as string)
        'zone_demand_popularity',    # POPULARITY_INDEX_1/2/3/4/5
        'dayType',                   # WEEKEND/NORMAL_WEEKDAY/FRIDAY
        'pickUpHourOfDay',          # VERYLATE/LATENIGHT/MORNING/etc
        'sla',                       # Scheduled/OnDemand
        'booking_type'               # one_way_trip/round_trip/etc
    ]

    # Initialize classifier with reasonable parameters
    cart = AggregateCART(
        max_depth=8,                 # Limit tree depth
        min_samples_leaf=10,         # Minimum samples per leaf
        min_impurity_decrease=0.001  # Minimum improvement for splits
    )

    print(f"Training on features: {feature_cols}")

    # Train the model
    cart.fit(
        df,
        feature_cols=feature_cols,
        good_col='DU_good_cnt',
        bad_col='DU_Bad_Count',
        total_col='total_cnt'  # For validation
    )

    print(f"Tree depth: {cart.get_depth()}")
    print(f"Number of leaves: {cart.get_n_leaves()}")

    return cart, feature_cols


def prediction_examples(cart, feature_cols):
    """Demonstrate predictions on new samples."""
    print("\n" + "=" * 60)
    print("PREDICTION EXAMPLES")
    print("=" * 60)

    # Create test samples representing different scenarios
    test_scenarios = pd.DataFrame({
        'source': ['ios', 'android', 'Phone', 'ios'],
        'estimated_usage_bins': ['LTE_1_HOUR', 'LTE_1_HOUR', 'NOT_SPECIFIED', 'GT_1_LTE_2_HOURS'],
        'city': ['Bangalore', 'Mumbai', 'Delhi NCR', 'Bangalore'],
        'zone': ['219', '443', '264', '221'],
        'zone_demand_popularity': ['POPULARITY_INDEX_1', 'POPULARITY_INDEX_1', 'POPULARITY_INDEX_2', 'POPULARITY_INDEX_2'],
        'dayType': ['WEEKEND', 'NORMAL_WEEKDAY', 'WEEKEND', 'NORMAL_WEEKDAY'],
        'pickUpHourOfDay': ['VERYLATE', 'MORNING', 'VERYLATE', 'MORNING'],
        'sla': ['Scheduled', 'Scheduled', 'OnDemand', 'Scheduled'],
        'booking_type': ['one_way_trip', 'one_way_trip', 'one_way_trip', 'round_trip']
    })

    # Make predictions
    predictions = cart.predict(test_scenarios)
    probabilities = cart.predict_proba(test_scenarios)

    # Display results
    print("Test Scenarios and Predictions:")
    print("-" * 100)

    for i, (idx, row) in enumerate(test_scenarios.iterrows()):
        pred_class = predictions[i]
        prob_bad, prob_good = probabilities[i]

        print(f"Scenario {i+1}:")
        print(f"  Platform: {row['source']}, City: {row['city']}, Day: {row['dayType']}")
        print(f"  Time: {row['pickUpHourOfDay']}, Zone: {row['zone']}")
        print(f"  → Prediction: {'GOOD' if pred_class == 1 else 'BAD'} DU")
        print(f"  → Probability: {prob_good:.3f} good, {prob_bad:.3f} bad")
        print()


def model_analysis(cart):
    """Analyze the trained model."""
    print("=" * 60)
    print("MODEL ANALYSIS")
    print("=" * 60)

    print("Tree Structure:")
    cart.print_tree()

    print(f"\nModel Statistics:")
    print(f"  - Tree Depth: {cart.get_depth()}")
    print(f"  - Number of Leaves: {cart.get_n_leaves()}")
    print(f"  - Features Used: {cart.n_features_}")


def feature_importance_analysis(df, cart, feature_cols):
    """Analyze which features are most important (simple analysis)."""
    print("\n" + "=" * 60)
    print("FEATURE IMPORTANCE ANALYSIS")
    print("=" * 60)

    # Simple feature importance: count how often each feature appears in splits
    def count_feature_usage(node, feature_counts):
        if hasattr(node, 'feature'):  # Internal node
            feature_counts[node.feature] = feature_counts.get(node.feature, 0) + 1
            if node.left:
                count_feature_usage(node.left, feature_counts)
            if node.right:
                count_feature_usage(node.right, feature_counts)

    feature_counts = {}
    count_feature_usage(cart.tree_, feature_counts)

    print("Feature usage in tree splits:")
    for feature in sorted(feature_counts.keys(), key=lambda x: feature_counts[x], reverse=True):
        print(f"  {feature}: {feature_counts[feature]} splits")

    # Show unique values per feature
    print("\nFeature value distributions:")
    for feature in feature_cols:
        unique_vals = df[feature].nunique()
        total_rows = len(df)
        print(f"  {feature}: {unique_vals} unique values across {total_rows} aggregate rows")


def performance_comparison(df, feature_cols):
    """Compare different model configurations."""
    print("\n" + "=" * 60)
    print("PERFORMANCE COMPARISON")
    print("=" * 60)

    configurations = [
        {"name": "Shallow Tree", "max_depth": 3, "min_samples_leaf": 20},
        {"name": "Medium Tree", "max_depth": 6, "min_samples_leaf": 10},
        {"name": "Deep Tree", "max_depth": 10, "min_samples_leaf": 5},
        {"name": "Conservative", "max_depth": 5, "min_samples_leaf": 50, "min_impurity_decrease": 0.01}
    ]

    print("Model Configuration Comparison:")
    print("-" * 70)
    print(f"{'Configuration':<15} {'Depth':<8} {'Leaves':<8} {'Description':<25}")
    print("-" * 70)

    for config in configurations:
        cart_temp = AggregateCART(
            max_depth=config.get("max_depth"),
            min_samples_leaf=config.get("min_samples_leaf", 1),
            min_impurity_decrease=config.get("min_impurity_decrease", 0.0)
        )

        cart_temp.fit(df, feature_cols, 'DU_good_cnt', 'DU_Bad_Count')

        depth = cart_temp.get_depth()
        leaves = cart_temp.get_n_leaves()

        description = f"d={config.get('max_depth', 'None')}, min={config['min_samples_leaf']}"
        if config.get("min_impurity_decrease", 0) > 0:
            description += f", imp={config['min_impurity_decrease']}"

        print(f"{config['name']:<15} {depth:<8} {leaves:<8} {description:<25}")


def main():
    """Run the complete example."""
    print("CART Decision Tree for Aggregate OLAP Data")
    print("Ride-Hailing Demand-Utilization Prediction Example")
    print("=" * 80)

    # Load data and show basic info
    df = load_sample_data()

    print(f"\nDataset Overview:")
    print(f"  - Shape: {df.shape}")
    print(f"  - Features: {df.columns.tolist()}")
    print(f"  - Good/Bad ratio: {df['DU_good_cnt'].sum()}:{df['DU_Bad_Count'].sum()}")

    # Train model
    cart, feature_cols = basic_training_example()

    # Make predictions
    prediction_examples(cart, feature_cols)

    # Analyze model
    model_analysis(cart)

    # Feature importance
    feature_importance_analysis(df, cart, feature_cols)

    # Performance comparison
    performance_comparison(df, feature_cols)

    print("\n" + "=" * 80)
    print("Example completed successfully!")
    print("\nNext steps:")
    print("1. Try different hyperparameters")
    print("2. Evaluate on held-out test set")
    print("3. Compare with sklearn DecisionTreeClassifier on raw data")
    print("4. Deploy for real-time prediction")


if __name__ == "__main__":
    main()