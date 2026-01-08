#!/usr/bin/env python3
"""
Example script showing how to load the saved JSON model and use it for prediction.

Usage:
    python load_and_predict.py <model_file.json>
"""

import sys
import pandas as pd
from pathlib import Path

# Add the cart_olap module to the path
sys.path.insert(0, str(Path(__file__).parent.parent))

from cart_olap import AggregateCART

def demo_load_and_predict(model_path="output/du_model_final.json"):
    """Demonstrate loading a saved model and making predictions"""

    print(f"🔄 Loading model from {model_path}...")

    # Load the model from JSON
    cart = AggregateCART.load_json(model_path)

    print(f"✅ Model loaded successfully!")
    print(f"   Tree depth: {cart.get_depth()}")
    print(f"   Number of leaves: {cart.get_n_leaves()}")
    print(f"   Binary features: {len(cart.feature_names_)}")

    # Create some example prediction samples
    print(f"\n🎯 Creating example prediction samples...")

    # Sample 1: Late night iOS trip in Bangalore
    sample1 = {
        'source': 'ios',
        'estimated_usage_bins': 'LTE_1_HOUR',
        'city': 'Bangalore',
        'zone': '219',
        'zone_demand_popularity': 'POPULARITY_INDEX_1',
        'dayType': 'WEEKEND',
        'pickUpHourOfDay': 'VERYLATE',
        'sla': 'Scheduled',
        'booking_type': 'one_way_trip'
    }

    # Sample 2: Morning Android trip in Delhi NCR
    sample2 = {
        'source': 'android',
        'estimated_usage_bins': 'LTE_1_HOUR',
        'city': 'Delhi NCR',
        'zone': '75',
        'zone_demand_popularity': 'POPULARITY_INDEX_2',
        'dayType': 'NORMAL_WEEKDAY',
        'pickUpHourOfDay': 'MORNING',
        'sla': 'Scheduled',
        'booking_type': 'one_way_trip'
    }

    # Sample 3: High demand zone trip
    sample3 = {
        'source': 'ios',
        'estimated_usage_bins': 'LTE_1_HOUR',
        'city': 'Mumbai',
        'zone': '401',
        'zone_demand_popularity': 'POPULARITY_INDEX_5',
        'dayType': 'WEEKEND',
        'pickUpHourOfDay': 'EVENING',
        'sla': 'Immediate',
        'booking_type': 'one_way_trip'
    }

    samples = [sample1, sample2, sample3]
    sample_names = [
        "Late night iOS trip (Bangalore, VERYLATE)",
        "Morning Android trip (Delhi NCR, MORNING)",
        "High demand zone trip (Mumbai, POPULARITY_INDEX_5)"
    ]

    print(f"\n🔮 Making predictions...")
    print("="*60)

    for i, (sample, name) in enumerate(zip(samples, sample_names), 1):
        # Convert to DataFrame for prediction
        sample_df = pd.DataFrame([sample])

        # Make prediction and get probability
        prediction = cart.predict(sample_df)[0]
        proba = cart.predict_proba(sample_df)[0]

        outcome = "Good DU" if prediction == 1 else "Bad DU"
        confidence = proba[1] if prediction == 1 else proba[0]

        print(f"Sample {i}: {name}")
        print(f"   Prediction: {outcome}")
        print(f"   Confidence: {confidence:.1%}")
        print(f"   Probabilities: Bad={proba[0]:.3f}, Good={proba[1]:.3f}")
        print()

    return cart

def batch_predict_from_csv(model_path, csv_path, output_path=None):
    """Load model and make batch predictions on a CSV file"""

    print(f"🔄 Loading model and CSV data...")

    # Load model
    cart = AggregateCART.load_json(model_path)

    # Load CSV data
    df = pd.read_csv(csv_path)
    print(f"   Loaded {len(df)} rows from {csv_path}")

    # Get feature columns (exclude count columns)
    feature_cols = [col for col in df.columns
                   if col not in ['DU_good_cnt', 'DU_Bad_Count', 'total_cnt']]

    print(f"   Using {len(feature_cols)} features: {feature_cols}")

    # Make predictions
    predictions = cart.predict(df[feature_cols])
    probabilities = cart.predict_proba(df[feature_cols])

    # Add predictions to dataframe
    result_df = df.copy()
    result_df['predicted_du'] = predictions
    result_df['predicted_du_label'] = ['Good' if p == 1 else 'Bad' for p in predictions]
    result_df['prob_bad'] = probabilities[:, 0]
    result_df['prob_good'] = probabilities[:, 1]
    result_df['confidence'] = [prob[pred] for pred, prob in zip(predictions, probabilities)]

    # Show summary
    print(f"\n📊 Prediction Summary:")
    print(f"   Total predictions: {len(predictions)}")
    print(f"   Predicted Good DU: {sum(predictions)} ({sum(predictions)/len(predictions):.1%})")
    print(f"   Predicted Bad DU: {len(predictions) - sum(predictions)} ({1 - sum(predictions)/len(predictions):.1%})")
    print(f"   Average confidence: {result_df['confidence'].mean():.3f}")

    # Save results if output path provided
    if output_path:
        result_df.to_csv(output_path, index=False)
        print(f"   Results saved to: {output_path}")

    return result_df

if __name__ == "__main__":
    model_file = sys.argv[1] if len(sys.argv) > 1 else "output/du_model_final.json"

    if not Path(model_file).exists():
        print(f"❌ Model file not found: {model_file}")
        print("   Available models:")
        for json_file in Path(".").glob("*.json"):
            print(f"   - {json_file}")
        sys.exit(1)

    print("🚀 CART Model Loading and Prediction Demo")
    print("="*50)

    # Demo individual predictions
    cart = demo_load_and_predict(model_file)

    # Demo batch prediction if DU data exists
    if Path("output/DUAggregateData.csv").exists():
        print("\n" + "="*50)
        print("📁 Batch Prediction Demo")
        print("="*50)

        # Take first 100 rows for demo
        df = pd.read_csv("output/DUAggregateData.csv").head(100)
        df.to_csv("output/sample_for_prediction.csv", index=False)

        result_df = batch_predict_from_csv(
            model_file,
            "output/sample_for_prediction.csv",
            "output/predictions_output.csv"
        )

        print("\n🎯 Sample predictions:")
        cols_to_show = ['city', 'pickUpHourOfDay', 'predicted_du_label', 'confidence']
        print(result_df[cols_to_show].head(10).to_string(index=False))

    print(f"\n✨ Demo completed! Model ready for use.")