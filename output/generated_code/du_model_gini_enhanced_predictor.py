#!/usr/bin/env python3
"""
Auto-generated Decision Tree Prediction Code
Generated from: du_model_gini_enhanced.json
Generated on: 2026-01-10 13:54:03
"""

from typing import Dict, List, Union, Optional
import json

# Model Statistics
TOTAL_RULES = 34
TOTAL_TRAINING_SAMPLES = 20343
AVERAGE_CONFIDENCE = 0.8726
MODEL_METADATA = {}

def predict_du_quality(features: Dict[str, Union[int, float, str]]) -> Dict[str, Union[int, float, str]]:
    """
    Predict demand-utilization quality based on feature values
    
    Args:
        features: Dictionary of feature values
    
    Returns:
        Dictionary with prediction, confidence, and metadata
    """
    if (features.get("pickUpHourOfDay=VERYLATE", 0) == 0 and
         features.get("zone_demand_popularity=POPULARITY_INDEX_5", 0) == 0 and
         features.get("pickUpHourOfDay=LATENIGHT", 0) == 0 and
         features.get("zone=221", 0) == 0 and
         features.get("zone=194", 0) == 0 and
         features.get("sla=Immediate", 0) == 0):
        return {
            "prediction": 1,
            "prediction_label": "Good_DU",
            "confidence": 0.9035,
            "samples": 12794,
            "class_counts": {'good': 11560, 'bad': 1234},
            "rule_index": 0
        }
    elif (features.get("pickUpHourOfDay=VERYLATE", 0) == 0 and
         features.get("zone_demand_popularity=POPULARITY_INDEX_5", 0) == 1 and
         features.get("pickUpHourOfDay=LATENIGHT", 0) == 0 and
         features.get("city=Pune", 0) == 0 and
         features.get("city=Mumbai", 0) == 0 and
         features.get("city=Hyderabad", 0) == 0):
        return {
            "prediction": 1,
            "prediction_label": "Good_DU",
            "confidence": 0.8905,
            "samples": 1397,
            "class_counts": {'good': 1244, 'bad': 153},
            "rule_index": 1
        }
    elif (features.get("pickUpHourOfDay=VERYLATE", 0) == 1 and
         features.get("city=Delhi NCR", 0) == 0 and
         features.get("dayType=WEEKEND", 0) == 1 and
         features.get("city=Chennai", 0) == 0 and
         features.get("zone_demand_popularity=POPULARITY_INDEX_4", 0) == 0 and
         features.get("zone=216", 0) == 0):
        return {
            "prediction": 1,
            "prediction_label": "Good_DU",
            "confidence": 0.7440,
            "samples": 996,
            "class_counts": {'good': 741, 'bad': 255},
            "rule_index": 2
        }
    elif (features.get("pickUpHourOfDay=VERYLATE", 0) == 0 and
         features.get("zone_demand_popularity=POPULARITY_INDEX_5", 0) == 0 and
         features.get("pickUpHourOfDay=LATENIGHT", 0) == 0 and
         features.get("zone=221", 0) == 0 and
         features.get("zone=194", 0) == 0 and
         features.get("sla=Immediate", 0) == 1):
        return {
            "prediction": 1,
            "prediction_label": "Good_DU",
            "confidence": 0.9900,
            "samples": 697,
            "class_counts": {'good': 690, 'bad': 7},
            "rule_index": 3
        }
    elif (features.get("pickUpHourOfDay=VERYLATE", 0) == 0 and
         features.get("zone_demand_popularity=POPULARITY_INDEX_5", 0) == 0 and
         features.get("pickUpHourOfDay=LATENIGHT", 0) == 1 and
         features.get("dayType=NORMAL_WEEKDAY", 0) == 0 and
         features.get("zone=217", 0) == 0 and
         features.get("city=Mumbai", 0) == 0):
        return {
            "prediction": 1,
            "prediction_label": "Good_DU",
            "confidence": 0.7205,
            "samples": 644,
            "class_counts": {'good': 464, 'bad': 180},
            "rule_index": 4
        }
    elif (features.get("pickUpHourOfDay=VERYLATE", 0) == 0 and
         features.get("zone_demand_popularity=POPULARITY_INDEX_5", 0) == 1 and
         features.get("pickUpHourOfDay=LATENIGHT", 0) == 0 and
         features.get("city=Pune", 0) == 0 and
         features.get("city=Mumbai", 0) == 1 and
         features.get("booking_type=round_trip", 0) == 0):
        return {
            "prediction": 1,
            "prediction_label": "Good_DU",
            "confidence": 0.8212,
            "samples": 397,
            "class_counts": {'good': 326, 'bad': 71},
            "rule_index": 5
        }
    elif (features.get("pickUpHourOfDay=VERYLATE", 0) == 1 and
         features.get("city=Delhi NCR", 0) == 0 and
         features.get("dayType=WEEKEND", 0) == 0 and
         features.get("zone_demand_popularity=POPULARITY_INDEX_5", 0) == 0 and
         features.get("city=Hyderabad", 0) == 0 and
         features.get("zone_demand_popularity=POPULARITY_INDEX_1", 0) == 0):
        return {
            "prediction": 1,
            "prediction_label": "Good_DU",
            "confidence": 0.8861,
            "samples": 395,
            "class_counts": {'good': 350, 'bad': 45},
            "rule_index": 6
        }
    elif (features.get("pickUpHourOfDay=VERYLATE", 0) == 1 and
         features.get("city=Delhi NCR", 0) == 0 and
         features.get("dayType=WEEKEND", 0) == 0 and
         features.get("zone_demand_popularity=POPULARITY_INDEX_5", 0) == 0 and
         features.get("city=Hyderabad", 0) == 0 and
         features.get("zone_demand_popularity=POPULARITY_INDEX_1", 0) == 1):
        return {
            "prediction": 1,
            "prediction_label": "Good_DU",
            "confidence": 0.9540,
            "samples": 326,
            "class_counts": {'good': 311, 'bad': 15},
            "rule_index": 7
        }
    elif (features.get("pickUpHourOfDay=VERYLATE", 0) == 0 and
         features.get("zone_demand_popularity=POPULARITY_INDEX_5", 0) == 0 and
         features.get("pickUpHourOfDay=LATENIGHT", 0) == 1 and
         features.get("dayType=NORMAL_WEEKDAY", 0) == 1 and
         features.get("zone_demand_popularity=POPULARITY_INDEX_1", 0) == 0 and
         features.get("city=Mumbai", 0) == 0):
        return {
            "prediction": 1,
            "prediction_label": "Good_DU",
            "confidence": 0.8193,
            "samples": 249,
            "class_counts": {'good': 204, 'bad': 45},
            "rule_index": 8
        }
    elif (features.get("pickUpHourOfDay=VERYLATE", 0) == 0 and
         features.get("zone_demand_popularity=POPULARITY_INDEX_5", 0) == 0 and
         features.get("pickUpHourOfDay=LATENIGHT", 0) == 1 and
         features.get("dayType=NORMAL_WEEKDAY", 0) == 1 and
         features.get("zone_demand_popularity=POPULARITY_INDEX_1", 0) == 1 and
         features.get("zone=219", 0) == 0):
        return {
            "prediction": 1,
            "prediction_label": "Good_DU",
            "confidence": 0.9419,
            "samples": 241,
            "class_counts": {'good': 227, 'bad': 14},
            "rule_index": 9
        }
    elif (features.get("pickUpHourOfDay=VERYLATE", 0) == 0 and
         features.get("zone_demand_popularity=POPULARITY_INDEX_5", 0) == 0 and
         features.get("pickUpHourOfDay=LATENIGHT", 0) == 1 and
         features.get("dayType=NORMAL_WEEKDAY", 0) == 0 and
         features.get("zone=217", 0) == 0 and
         features.get("city=Mumbai", 0) == 1):
        return {
            "prediction": 1,
            "prediction_label": "Good_DU",
            "confidence": 0.8391,
            "samples": 230,
            "class_counts": {'good': 193, 'bad': 37},
            "rule_index": 10
        }
    elif (features.get("pickUpHourOfDay=VERYLATE", 0) == 0 and
         features.get("zone_demand_popularity=POPULARITY_INDEX_5", 0) == 1 and
         features.get("pickUpHourOfDay=LATENIGHT", 0) == 0 and
         features.get("city=Pune", 0) == 1 and
         features.get("booking_type=outstation", 0) == 0 and
         features.get("pickUpHourOfDay=MORNING", 0) == 0):
        return {
            "prediction": 1,
            "prediction_label": "Good_DU",
            "confidence": 0.6119,
            "samples": 201,
            "class_counts": {'good': 123, 'bad': 78},
            "rule_index": 11
        }
    elif (features.get("pickUpHourOfDay=VERYLATE", 0) == 0 and
         features.get("zone_demand_popularity=POPULARITY_INDEX_5", 0) == 1 and
         features.get("pickUpHourOfDay=LATENIGHT", 0) == 0 and
         features.get("city=Pune", 0) == 0 and
         features.get("city=Mumbai", 0) == 1 and
         features.get("booking_type=round_trip", 0) == 1):
        return {
            "prediction": 1,
            "prediction_label": "Good_DU",
            "confidence": 0.6825,
            "samples": 189,
            "class_counts": {'good': 129, 'bad': 60},
            "rule_index": 12
        }
    elif (features.get("pickUpHourOfDay=VERYLATE", 0) == 0 and
         features.get("zone_demand_popularity=POPULARITY_INDEX_5", 0) == 0 and
         features.get("pickUpHourOfDay=LATENIGHT", 0) == 1 and
         features.get("dayType=NORMAL_WEEKDAY", 0) == 1 and
         features.get("zone_demand_popularity=POPULARITY_INDEX_1", 0) == 0 and
         features.get("city=Mumbai", 0) == 1):
        return {
            "prediction": 1,
            "prediction_label": "Good_DU",
            "confidence": 0.9655,
            "samples": 116,
            "class_counts": {'good': 112, 'bad': 4},
            "rule_index": 13
        }
    elif (features.get("pickUpHourOfDay=VERYLATE", 0) == 0 and
         features.get("zone_demand_popularity=POPULARITY_INDEX_5", 0) == 0 and
         features.get("pickUpHourOfDay=LATENIGHT", 0) == 0 and
         features.get("zone=221", 0) == 1 and
         features.get("booking_type=one_way_trip", 0) == 0 and
         features.get("estimated_usage_bins=GT_3_LTE_4_HOURS", 0) == 0):
        return {
            "prediction": 1,
            "prediction_label": "Good_DU",
            "confidence": 0.8454,
            "samples": 97,
            "class_counts": {'good': 82, 'bad': 15},
            "rule_index": 14
        }
    elif (features.get("pickUpHourOfDay=VERYLATE", 0) == 0 and
         features.get("zone_demand_popularity=POPULARITY_INDEX_5", 0) == 0 and
         features.get("pickUpHourOfDay=LATENIGHT", 0) == 1 and
         features.get("dayType=NORMAL_WEEKDAY", 0) == 1 and
         features.get("zone_demand_popularity=POPULARITY_INDEX_1", 0) == 1 and
         features.get("zone=219", 0) == 1):
        return {
            "prediction": 1,
            "prediction_label": "Good_DU",
            "confidence": 0.9688,
            "samples": 96,
            "class_counts": {'good': 93, 'bad': 3},
            "rule_index": 15
        }
    elif (features.get("pickUpHourOfDay=VERYLATE", 0) == 0 and
         features.get("zone_demand_popularity=POPULARITY_INDEX_5", 0) == 1 and
         features.get("pickUpHourOfDay=LATENIGHT", 0) == 0 and
         features.get("city=Pune", 0) == 0 and
         features.get("city=Mumbai", 0) == 0 and
         features.get("city=Hyderabad", 0) == 1):
        return {
            "prediction": 1,
            "prediction_label": "Good_DU",
            "confidence": 0.7174,
            "samples": 92,
            "class_counts": {'good': 66, 'bad': 26},
            "rule_index": 16
        }
    elif (features.get("pickUpHourOfDay=VERYLATE", 0) == 0 and
         features.get("zone_demand_popularity=POPULARITY_INDEX_5", 0) == 0 and
         features.get("pickUpHourOfDay=LATENIGHT", 0) == 0 and
         features.get("zone=221", 0) == 1 and
         features.get("booking_type=one_way_trip", 0) == 1):
        return {
            "prediction": 1,
            "prediction_label": "Good_DU",
            "confidence": 0.6111,
            "samples": 90,
            "class_counts": {'good': 55, 'bad': 35},
            "rule_index": 17
        }
    elif (features.get("pickUpHourOfDay=VERYLATE", 0) == 0 and
         features.get("zone_demand_popularity=POPULARITY_INDEX_5", 0) == 1 and
         features.get("pickUpHourOfDay=LATENIGHT", 0) == 0 and
         features.get("city=Pune", 0) == 1 and
         features.get("booking_type=outstation", 0) == 0 and
         features.get("pickUpHourOfDay=MORNING", 0) == 1):
        return {
            "prediction": 1,
            "prediction_label": "Good_DU",
            "confidence": 0.8111,
            "samples": 90,
            "class_counts": {'good': 73, 'bad': 17},
            "rule_index": 18
        }
    elif (features.get("pickUpHourOfDay=VERYLATE", 0) == 1 and
         features.get("city=Delhi NCR", 0) == 0 and
         features.get("dayType=WEEKEND", 0) == 0 and
         features.get("zone_demand_popularity=POPULARITY_INDEX_5", 0) == 0 and
         features.get("city=Hyderabad", 0) == 1):
        return {
            "prediction": 1,
            "prediction_label": "Good_DU",
            "confidence": 0.7444,
            "samples": 90,
            "class_counts": {'good': 67, 'bad': 23},
            "rule_index": 19
        }
    elif (features.get("pickUpHourOfDay=VERYLATE", 0) == 0 and
         features.get("zone_demand_popularity=POPULARITY_INDEX_5", 0) == 1 and
         features.get("pickUpHourOfDay=LATENIGHT", 0) == 1 and
         features.get("city=Mumbai", 0) == 0):
        return {
            "prediction": 1,
            "prediction_label": "Good_DU",
            "confidence": 0.5059,
            "samples": 85,
            "class_counts": {'good': 43, 'bad': 42},
            "rule_index": 20
        }
    elif (features.get("pickUpHourOfDay=VERYLATE", 0) == 1 and
         features.get("city=Delhi NCR", 0) == 0 and
         features.get("dayType=WEEKEND", 0) == 1 and
         features.get("city=Chennai", 0) == 0 and
         features.get("zone_demand_popularity=POPULARITY_INDEX_4", 0) == 0 and
         features.get("zone=216", 0) == 1):
        return {
            "prediction": 1,
            "prediction_label": "Good_DU",
            "confidence": 0.9277,
            "samples": 83,
            "class_counts": {'good': 77, 'bad': 6},
            "rule_index": 21
        }
    elif (features.get("pickUpHourOfDay=VERYLATE", 0) == 1 and
         features.get("city=Delhi NCR", 0) == 0 and
         features.get("dayType=WEEKEND", 0) == 1 and
         features.get("city=Chennai", 0) == 0 and
         features.get("zone_demand_popularity=POPULARITY_INDEX_4", 0) == 1 and
         features.get("city=Mumbai", 0) == 1):
        return {
            "prediction": 1,
            "prediction_label": "Good_DU",
            "confidence": 0.5181,
            "samples": 83,
            "class_counts": {'good': 43, 'bad': 40},
            "rule_index": 22
        }
    elif (features.get("pickUpHourOfDay=VERYLATE", 0) == 0 and
         features.get("zone_demand_popularity=POPULARITY_INDEX_5", 0) == 0 and
         features.get("pickUpHourOfDay=LATENIGHT", 0) == 0 and
         features.get("zone=221", 0) == 0 and
         features.get("zone=194", 0) == 1):
        return {
            "prediction": 1,
            "prediction_label": "Good_DU",
            "confidence": 0.6087,
            "samples": 69,
            "class_counts": {'good': 42, 'bad': 27},
            "rule_index": 23
        }
    elif (features.get("pickUpHourOfDay=VERYLATE", 0) == 1 and
         features.get("city=Delhi NCR", 0) == 0 and
         features.get("dayType=WEEKEND", 0) == 1 and
         features.get("city=Chennai", 0) == 0 and
         features.get("zone_demand_popularity=POPULARITY_INDEX_4", 0) == 1 and
         features.get("city=Mumbai", 0) == 0):
        return {
            "prediction": 1,
            "prediction_label": "Good_DU",
            "confidence": 0.6061,
            "samples": 66,
            "class_counts": {'good': 40, 'bad': 26},
            "rule_index": 24
        }
    elif (features.get("pickUpHourOfDay=VERYLATE", 0) == 1 and
         features.get("city=Delhi NCR", 0) == 0 and
         features.get("dayType=WEEKEND", 0) == 1 and
         features.get("city=Chennai", 0) == 1):
        return {
            "prediction": 1,
            "prediction_label": "Good_DU",
            "confidence": 0.9545,
            "samples": 66,
            "class_counts": {'good': 63, 'bad': 3},
            "rule_index": 25
        }
    elif (features.get("pickUpHourOfDay=VERYLATE", 0) == 0 and
         features.get("zone_demand_popularity=POPULARITY_INDEX_5", 0) == 0 and
         features.get("pickUpHourOfDay=LATENIGHT", 0) == 1 and
         features.get("dayType=NORMAL_WEEKDAY", 0) == 0 and
         features.get("zone=217", 0) == 1):
        return {
            "prediction": 1,
            "prediction_label": "Good_DU",
            "confidence": 0.9677,
            "samples": 62,
            "class_counts": {'good': 60, 'bad': 2},
            "rule_index": 26
        }
    elif (features.get("pickUpHourOfDay=VERYLATE", 0) == 0 and
         features.get("zone_demand_popularity=POPULARITY_INDEX_5", 0) == 1 and
         features.get("pickUpHourOfDay=LATENIGHT", 0) == 0 and
         features.get("city=Pune", 0) == 1 and
         features.get("booking_type=outstation", 0) == 1):
        return {
            "prediction": 1,
            "prediction_label": "Good_DU",
            "confidence": 0.9032,
            "samples": 62,
            "class_counts": {'good': 56, 'bad': 6},
            "rule_index": 27
        }
    elif (features.get("pickUpHourOfDay=VERYLATE", 0) == 0 and
         features.get("zone_demand_popularity=POPULARITY_INDEX_5", 0) == 0 and
         features.get("pickUpHourOfDay=LATENIGHT", 0) == 0 and
         features.get("zone=221", 0) == 1 and
         features.get("booking_type=one_way_trip", 0) == 0 and
         features.get("estimated_usage_bins=GT_3_LTE_4_HOURS", 0) == 1):
        return {
            "prediction": 1,
            "prediction_label": "Good_DU",
            "confidence": 0.7705,
            "samples": 61,
            "class_counts": {'good': 47, 'bad': 14},
            "rule_index": 28
        }
    elif (features.get("pickUpHourOfDay=VERYLATE", 0) == 1 and
         features.get("city=Delhi NCR", 0) == 1 and
         features.get("zone_demand_popularity=POPULARITY_INDEX_2", 0) == 0 and
         features.get("zone_demand_popularity=POPULARITY_INDEX_4", 0) == 0):
        return {
            "prediction": 0,
            "prediction_label": "Bad_DU",
            "confidence": 0.6333,
            "samples": 60,
            "class_counts": {'good': 22, 'bad': 38},
            "rule_index": 29
        }
    elif (features.get("pickUpHourOfDay=VERYLATE", 0) == 1 and
         features.get("city=Delhi NCR", 0) == 0 and
         features.get("dayType=WEEKEND", 0) == 0 and
         features.get("zone_demand_popularity=POPULARITY_INDEX_5", 0) == 1):
        return {
            "prediction": 1,
            "prediction_label": "Good_DU",
            "confidence": 0.6842,
            "samples": 57,
            "class_counts": {'good': 39, 'bad': 18},
            "rule_index": 30
        }
    elif (features.get("pickUpHourOfDay=VERYLATE", 0) == 1 and
         features.get("city=Delhi NCR", 0) == 1 and
         features.get("zone_demand_popularity=POPULARITY_INDEX_2", 0) == 1):
        return {
            "prediction": 1,
            "prediction_label": "Good_DU",
            "confidence": 0.5263,
            "samples": 57,
            "class_counts": {'good': 30, 'bad': 27},
            "rule_index": 31
        }
    elif (features.get("pickUpHourOfDay=VERYLATE", 0) == 0 and
         features.get("zone_demand_popularity=POPULARITY_INDEX_5", 0) == 1 and
         features.get("pickUpHourOfDay=LATENIGHT", 0) == 1 and
         features.get("city=Mumbai", 0) == 1):
        return {
            "prediction": 1,
            "prediction_label": "Good_DU",
            "confidence": 0.7037,
            "samples": 54,
            "class_counts": {'good': 38, 'bad': 16},
            "rule_index": 32
        }
    elif (features.get("pickUpHourOfDay=VERYLATE", 0) == 1 and
         features.get("city=Delhi NCR", 0) == 1 and
         features.get("zone_demand_popularity=POPULARITY_INDEX_2", 0) == 0 and
         features.get("zone_demand_popularity=POPULARITY_INDEX_4", 0) == 1):
        return {
            "prediction": 0,
            "prediction_label": "Bad_DU",
            "confidence": 0.5098,
            "samples": 51,
            "class_counts": {'good': 25, 'bad': 26},
            "rule_index": 33
        }
    else:
        # Fallback for unknown patterns
        return {
            "prediction": 1,  # Default to Good_DU
            "prediction_label": "Good_DU",
            "confidence": 0.872,  # Overall dataset average
            "samples": 0,
            "class_counts": {"good": 0, "bad": 0},
            "rule_index": -1
        }

def predict_batch(feature_list: List[Dict[str, Union[int, float, str]]]) -> List[Dict[str, Union[int, float, str]]]:
    """
    Predict for a batch of feature dictionaries
    
    Args:
        feature_list: List of feature dictionaries
    
    Returns:
        List of prediction results
    """
    return [predict_du_quality(features) for features in feature_list]

if __name__ == "__main__":
    # Example usage
    sample_features = {
        "pickUpHourOfDay=VERYLATE": 0,
        "zone_demand_popularity=POPULARITY_INDEX_5": 0,
        "pickUpHourOfDay=LATENIGHT": 0,
        "zone=221": 0,
        "zone=194": 0,
        "sla=Immediate": 0,
    }

    result = predict_du_quality(sample_features)
    print("Prediction Result:")
    print(json.dumps(result, indent=2))
