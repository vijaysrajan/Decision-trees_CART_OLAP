#!/usr/bin/env python3
"""
Generated decision rules for classification from CART-OLAP model
Source: CART-OLAP_du_model_cli_compact
Total rules: 34
Feature count: 354
"""

def predict_sample(features):
    """
    Classify a single sample using decision rules
    
    Parameters
    ----------
    features : dict
        Feature dictionary with binary values (0/1)
        Keys should match feature names from training
    
    Returns
    -------
    dict
        Prediction result with confidence and metadata
    """

    # Rule 1: POSITIVE (90.4% confidence, 12794 samples)
    if (features.get('pickUpHourOfDay=VERYLATE', 0) == 0 and
        features.get('zone_demand_popularity=POPULARITY_INDEX_5', 0) == 0 and
        features.get('pickUpHourOfDay=LATENIGHT', 0) == 0 and
        features.get('zone=221', 0) == 0 and
        features.get('zone=194', 0) == 0 and
        features.get('sla=Immediate', 0) == 0):
        return {'prediction': 1, 'confidence': 0.904, 'rule_id': 1, 'samples': 12794, 'good_count': 11560, 'bad_count': 1234}

    # Rule 2: POSITIVE (89.0% confidence, 1397 samples)
    if (features.get('pickUpHourOfDay=VERYLATE', 0) == 0 and
        features.get('zone_demand_popularity=POPULARITY_INDEX_5', 0) == 1 and
        features.get('pickUpHourOfDay=LATENIGHT', 0) == 0 and
        features.get('city=Pune', 0) == 0 and
        features.get('city=Mumbai', 0) == 0 and
        features.get('city=Hyderabad', 0) == 0):
        return {'prediction': 1, 'confidence': 0.89, 'rule_id': 2, 'samples': 1397, 'good_count': 1244, 'bad_count': 153}

    # Rule 3: POSITIVE (74.4% confidence, 996 samples)
    if (features.get('pickUpHourOfDay=VERYLATE', 0) == 1 and
        features.get('city=Delhi NCR', 0) == 0 and
        features.get('dayType=WEEKEND', 0) == 1 and
        features.get('city=Chennai', 0) == 0 and
        features.get('zone_demand_popularity=POPULARITY_INDEX_4', 0) == 0 and
        features.get('zone=216', 0) == 0):
        return {'prediction': 1, 'confidence': 0.744, 'rule_id': 3, 'samples': 996, 'good_count': 741, 'bad_count': 255}

    # Rule 4: POSITIVE (99.0% confidence, 697 samples)
    if (features.get('pickUpHourOfDay=VERYLATE', 0) == 0 and
        features.get('zone_demand_popularity=POPULARITY_INDEX_5', 0) == 0 and
        features.get('pickUpHourOfDay=LATENIGHT', 0) == 0 and
        features.get('zone=221', 0) == 0 and
        features.get('zone=194', 0) == 0 and
        features.get('sla=Immediate', 0) == 1):
        return {'prediction': 1, 'confidence': 0.99, 'rule_id': 4, 'samples': 697, 'good_count': 690, 'bad_count': 7}

    # Rule 5: POSITIVE (72.0% confidence, 644 samples)
    if (features.get('pickUpHourOfDay=VERYLATE', 0) == 0 and
        features.get('zone_demand_popularity=POPULARITY_INDEX_5', 0) == 0 and
        features.get('pickUpHourOfDay=LATENIGHT', 0) == 1 and
        features.get('dayType=NORMAL_WEEKDAY', 0) == 0 and
        features.get('zone=217', 0) == 0 and
        features.get('city=Mumbai', 0) == 0):
        return {'prediction': 1, 'confidence': 0.72, 'rule_id': 5, 'samples': 644, 'good_count': 464, 'bad_count': 180}

    # Rule 6: POSITIVE (82.1% confidence, 397 samples)
    if (features.get('pickUpHourOfDay=VERYLATE', 0) == 0 and
        features.get('zone_demand_popularity=POPULARITY_INDEX_5', 0) == 1 and
        features.get('pickUpHourOfDay=LATENIGHT', 0) == 0 and
        features.get('city=Pune', 0) == 0 and
        features.get('city=Mumbai', 0) == 1 and
        features.get('booking_type=round_trip', 0) == 0):
        return {'prediction': 1, 'confidence': 0.821, 'rule_id': 6, 'samples': 397, 'good_count': 326, 'bad_count': 71}

    # Rule 7: POSITIVE (88.6% confidence, 395 samples)
    if (features.get('pickUpHourOfDay=VERYLATE', 0) == 1 and
        features.get('city=Delhi NCR', 0) == 0 and
        features.get('dayType=WEEKEND', 0) == 0 and
        features.get('zone_demand_popularity=POPULARITY_INDEX_5', 0) == 0 and
        features.get('city=Hyderabad', 0) == 0 and
        features.get('zone_demand_popularity=POPULARITY_INDEX_1', 0) == 0):
        return {'prediction': 1, 'confidence': 0.886, 'rule_id': 7, 'samples': 395, 'good_count': 350, 'bad_count': 45}

    # Rule 8: POSITIVE (95.4% confidence, 326 samples)
    if (features.get('pickUpHourOfDay=VERYLATE', 0) == 1 and
        features.get('city=Delhi NCR', 0) == 0 and
        features.get('dayType=WEEKEND', 0) == 0 and
        features.get('zone_demand_popularity=POPULARITY_INDEX_5', 0) == 0 and
        features.get('city=Hyderabad', 0) == 0 and
        features.get('zone_demand_popularity=POPULARITY_INDEX_1', 0) == 1):
        return {'prediction': 1, 'confidence': 0.954, 'rule_id': 8, 'samples': 326, 'good_count': 311, 'bad_count': 15}

    # Rule 9: POSITIVE (81.9% confidence, 249 samples)
    if (features.get('pickUpHourOfDay=VERYLATE', 0) == 0 and
        features.get('zone_demand_popularity=POPULARITY_INDEX_5', 0) == 0 and
        features.get('pickUpHourOfDay=LATENIGHT', 0) == 1 and
        features.get('dayType=NORMAL_WEEKDAY', 0) == 1 and
        features.get('zone_demand_popularity=POPULARITY_INDEX_1', 0) == 0 and
        features.get('city=Mumbai', 0) == 0):
        return {'prediction': 1, 'confidence': 0.819, 'rule_id': 9, 'samples': 249, 'good_count': 204, 'bad_count': 45}

    # Rule 10: POSITIVE (94.2% confidence, 241 samples)
    if (features.get('pickUpHourOfDay=VERYLATE', 0) == 0 and
        features.get('zone_demand_popularity=POPULARITY_INDEX_5', 0) == 0 and
        features.get('pickUpHourOfDay=LATENIGHT', 0) == 1 and
        features.get('dayType=NORMAL_WEEKDAY', 0) == 1 and
        features.get('zone_demand_popularity=POPULARITY_INDEX_1', 0) == 1 and
        features.get('zone=219', 0) == 0):
        return {'prediction': 1, 'confidence': 0.942, 'rule_id': 10, 'samples': 241, 'good_count': 227, 'bad_count': 14}

    # Rule 11: POSITIVE (83.9% confidence, 230 samples)
    if (features.get('pickUpHourOfDay=VERYLATE', 0) == 0 and
        features.get('zone_demand_popularity=POPULARITY_INDEX_5', 0) == 0 and
        features.get('pickUpHourOfDay=LATENIGHT', 0) == 1 and
        features.get('dayType=NORMAL_WEEKDAY', 0) == 0 and
        features.get('zone=217', 0) == 0 and
        features.get('city=Mumbai', 0) == 1):
        return {'prediction': 1, 'confidence': 0.839, 'rule_id': 11, 'samples': 230, 'good_count': 193, 'bad_count': 37}

    # Rule 12: POSITIVE (61.2% confidence, 201 samples)
    if (features.get('pickUpHourOfDay=VERYLATE', 0) == 0 and
        features.get('zone_demand_popularity=POPULARITY_INDEX_5', 0) == 1 and
        features.get('pickUpHourOfDay=LATENIGHT', 0) == 0 and
        features.get('city=Pune', 0) == 1 and
        features.get('booking_type=outstation', 0) == 0 and
        features.get('pickUpHourOfDay=MORNING', 0) == 0):
        return {'prediction': 1, 'confidence': 0.612, 'rule_id': 12, 'samples': 201, 'good_count': 123, 'bad_count': 78}

    # Rule 13: POSITIVE (68.3% confidence, 189 samples)
    if (features.get('pickUpHourOfDay=VERYLATE', 0) == 0 and
        features.get('zone_demand_popularity=POPULARITY_INDEX_5', 0) == 1 and
        features.get('pickUpHourOfDay=LATENIGHT', 0) == 0 and
        features.get('city=Pune', 0) == 0 and
        features.get('city=Mumbai', 0) == 1 and
        features.get('booking_type=round_trip', 0) == 1):
        return {'prediction': 1, 'confidence': 0.683, 'rule_id': 13, 'samples': 189, 'good_count': 129, 'bad_count': 60}

    # Rule 14: POSITIVE (96.6% confidence, 116 samples)
    if (features.get('pickUpHourOfDay=VERYLATE', 0) == 0 and
        features.get('zone_demand_popularity=POPULARITY_INDEX_5', 0) == 0 and
        features.get('pickUpHourOfDay=LATENIGHT', 0) == 1 and
        features.get('dayType=NORMAL_WEEKDAY', 0) == 1 and
        features.get('zone_demand_popularity=POPULARITY_INDEX_1', 0) == 0 and
        features.get('city=Mumbai', 0) == 1):
        return {'prediction': 1, 'confidence': 0.966, 'rule_id': 14, 'samples': 116, 'good_count': 112, 'bad_count': 4}

    # Rule 15: POSITIVE (84.5% confidence, 97 samples)
    if (features.get('pickUpHourOfDay=VERYLATE', 0) == 0 and
        features.get('zone_demand_popularity=POPULARITY_INDEX_5', 0) == 0 and
        features.get('pickUpHourOfDay=LATENIGHT', 0) == 0 and
        features.get('zone=221', 0) == 1 and
        features.get('booking_type=one_way_trip', 0) == 0 and
        features.get('estimated_usage_bins=GT_3_LTE_4_HOURS', 0) == 0):
        return {'prediction': 1, 'confidence': 0.845, 'rule_id': 15, 'samples': 97, 'good_count': 82, 'bad_count': 15}

    # Rule 16: POSITIVE (96.9% confidence, 96 samples)
    if (features.get('pickUpHourOfDay=VERYLATE', 0) == 0 and
        features.get('zone_demand_popularity=POPULARITY_INDEX_5', 0) == 0 and
        features.get('pickUpHourOfDay=LATENIGHT', 0) == 1 and
        features.get('dayType=NORMAL_WEEKDAY', 0) == 1 and
        features.get('zone_demand_popularity=POPULARITY_INDEX_1', 0) == 1 and
        features.get('zone=219', 0) == 1):
        return {'prediction': 1, 'confidence': 0.969, 'rule_id': 16, 'samples': 96, 'good_count': 93, 'bad_count': 3}

    # Rule 17: POSITIVE (71.7% confidence, 92 samples)
    if (features.get('pickUpHourOfDay=VERYLATE', 0) == 0 and
        features.get('zone_demand_popularity=POPULARITY_INDEX_5', 0) == 1 and
        features.get('pickUpHourOfDay=LATENIGHT', 0) == 0 and
        features.get('city=Pune', 0) == 0 and
        features.get('city=Mumbai', 0) == 0 and
        features.get('city=Hyderabad', 0) == 1):
        return {'prediction': 1, 'confidence': 0.717, 'rule_id': 17, 'samples': 92, 'good_count': 66, 'bad_count': 26}

    # Rule 18: POSITIVE (61.1% confidence, 90 samples)
    if (features.get('pickUpHourOfDay=VERYLATE', 0) == 0 and
        features.get('zone_demand_popularity=POPULARITY_INDEX_5', 0) == 0 and
        features.get('pickUpHourOfDay=LATENIGHT', 0) == 0 and
        features.get('zone=221', 0) == 1 and
        features.get('booking_type=one_way_trip', 0) == 1):
        return {'prediction': 1, 'confidence': 0.611, 'rule_id': 18, 'samples': 90, 'good_count': 55, 'bad_count': 35}

    # Rule 19: POSITIVE (81.1% confidence, 90 samples)
    if (features.get('pickUpHourOfDay=VERYLATE', 0) == 0 and
        features.get('zone_demand_popularity=POPULARITY_INDEX_5', 0) == 1 and
        features.get('pickUpHourOfDay=LATENIGHT', 0) == 0 and
        features.get('city=Pune', 0) == 1 and
        features.get('booking_type=outstation', 0) == 0 and
        features.get('pickUpHourOfDay=MORNING', 0) == 1):
        return {'prediction': 1, 'confidence': 0.811, 'rule_id': 19, 'samples': 90, 'good_count': 73, 'bad_count': 17}

    # Rule 20: POSITIVE (74.4% confidence, 90 samples)
    if (features.get('pickUpHourOfDay=VERYLATE', 0) == 1 and
        features.get('city=Delhi NCR', 0) == 0 and
        features.get('dayType=WEEKEND', 0) == 0 and
        features.get('zone_demand_popularity=POPULARITY_INDEX_5', 0) == 0 and
        features.get('city=Hyderabad', 0) == 1):
        return {'prediction': 1, 'confidence': 0.744, 'rule_id': 20, 'samples': 90, 'good_count': 67, 'bad_count': 23}

    # Rule 21: POSITIVE (50.6% confidence, 85 samples)
    if (features.get('pickUpHourOfDay=VERYLATE', 0) == 0 and
        features.get('zone_demand_popularity=POPULARITY_INDEX_5', 0) == 1 and
        features.get('pickUpHourOfDay=LATENIGHT', 0) == 1 and
        features.get('city=Mumbai', 0) == 0):
        return {'prediction': 1, 'confidence': 0.506, 'rule_id': 21, 'samples': 85, 'good_count': 43, 'bad_count': 42}

    # Rule 22: POSITIVE (92.8% confidence, 83 samples)
    if (features.get('pickUpHourOfDay=VERYLATE', 0) == 1 and
        features.get('city=Delhi NCR', 0) == 0 and
        features.get('dayType=WEEKEND', 0) == 1 and
        features.get('city=Chennai', 0) == 0 and
        features.get('zone_demand_popularity=POPULARITY_INDEX_4', 0) == 0 and
        features.get('zone=216', 0) == 1):
        return {'prediction': 1, 'confidence': 0.928, 'rule_id': 22, 'samples': 83, 'good_count': 77, 'bad_count': 6}

    # Rule 23: POSITIVE (51.8% confidence, 83 samples)
    if (features.get('pickUpHourOfDay=VERYLATE', 0) == 1 and
        features.get('city=Delhi NCR', 0) == 0 and
        features.get('dayType=WEEKEND', 0) == 1 and
        features.get('city=Chennai', 0) == 0 and
        features.get('zone_demand_popularity=POPULARITY_INDEX_4', 0) == 1 and
        features.get('city=Mumbai', 0) == 1):
        return {'prediction': 1, 'confidence': 0.518, 'rule_id': 23, 'samples': 83, 'good_count': 43, 'bad_count': 40}

    # Rule 24: POSITIVE (60.9% confidence, 69 samples)
    if (features.get('pickUpHourOfDay=VERYLATE', 0) == 0 and
        features.get('zone_demand_popularity=POPULARITY_INDEX_5', 0) == 0 and
        features.get('pickUpHourOfDay=LATENIGHT', 0) == 0 and
        features.get('zone=221', 0) == 0 and
        features.get('zone=194', 0) == 1):
        return {'prediction': 1, 'confidence': 0.609, 'rule_id': 24, 'samples': 69, 'good_count': 42, 'bad_count': 27}

    # Rule 25: POSITIVE (60.6% confidence, 66 samples)
    if (features.get('pickUpHourOfDay=VERYLATE', 0) == 1 and
        features.get('city=Delhi NCR', 0) == 0 and
        features.get('dayType=WEEKEND', 0) == 1 and
        features.get('city=Chennai', 0) == 0 and
        features.get('zone_demand_popularity=POPULARITY_INDEX_4', 0) == 1 and
        features.get('city=Mumbai', 0) == 0):
        return {'prediction': 1, 'confidence': 0.606, 'rule_id': 25, 'samples': 66, 'good_count': 40, 'bad_count': 26}

    # Rule 26: POSITIVE (95.5% confidence, 66 samples)
    if (features.get('pickUpHourOfDay=VERYLATE', 0) == 1 and
        features.get('city=Delhi NCR', 0) == 0 and
        features.get('dayType=WEEKEND', 0) == 1 and
        features.get('city=Chennai', 0) == 1):
        return {'prediction': 1, 'confidence': 0.955, 'rule_id': 26, 'samples': 66, 'good_count': 63, 'bad_count': 3}

    # Rule 27: POSITIVE (96.8% confidence, 62 samples)
    if (features.get('pickUpHourOfDay=VERYLATE', 0) == 0 and
        features.get('zone_demand_popularity=POPULARITY_INDEX_5', 0) == 0 and
        features.get('pickUpHourOfDay=LATENIGHT', 0) == 1 and
        features.get('dayType=NORMAL_WEEKDAY', 0) == 0 and
        features.get('zone=217', 0) == 1):
        return {'prediction': 1, 'confidence': 0.968, 'rule_id': 27, 'samples': 62, 'good_count': 60, 'bad_count': 2}

    # Rule 28: POSITIVE (90.3% confidence, 62 samples)
    if (features.get('pickUpHourOfDay=VERYLATE', 0) == 0 and
        features.get('zone_demand_popularity=POPULARITY_INDEX_5', 0) == 1 and
        features.get('pickUpHourOfDay=LATENIGHT', 0) == 0 and
        features.get('city=Pune', 0) == 1 and
        features.get('booking_type=outstation', 0) == 1):
        return {'prediction': 1, 'confidence': 0.903, 'rule_id': 28, 'samples': 62, 'good_count': 56, 'bad_count': 6}

    # Rule 29: POSITIVE (77.0% confidence, 61 samples)
    if (features.get('pickUpHourOfDay=VERYLATE', 0) == 0 and
        features.get('zone_demand_popularity=POPULARITY_INDEX_5', 0) == 0 and
        features.get('pickUpHourOfDay=LATENIGHT', 0) == 0 and
        features.get('zone=221', 0) == 1 and
        features.get('booking_type=one_way_trip', 0) == 0 and
        features.get('estimated_usage_bins=GT_3_LTE_4_HOURS', 0) == 1):
        return {'prediction': 1, 'confidence': 0.77, 'rule_id': 29, 'samples': 61, 'good_count': 47, 'bad_count': 14}

    # Rule 30: NEGATIVE (63.3% confidence, 60 samples)
    if (features.get('pickUpHourOfDay=VERYLATE', 0) == 1 and
        features.get('city=Delhi NCR', 0) == 1 and
        features.get('zone_demand_popularity=POPULARITY_INDEX_2', 0) == 0 and
        features.get('zone_demand_popularity=POPULARITY_INDEX_4', 0) == 0):
        return {'prediction': 0, 'confidence': 0.633, 'rule_id': 30, 'samples': 60, 'good_count': 22, 'bad_count': 38}

    # Rule 31: POSITIVE (68.4% confidence, 57 samples)
    if (features.get('pickUpHourOfDay=VERYLATE', 0) == 1 and
        features.get('city=Delhi NCR', 0) == 0 and
        features.get('dayType=WEEKEND', 0) == 0 and
        features.get('zone_demand_popularity=POPULARITY_INDEX_5', 0) == 1):
        return {'prediction': 1, 'confidence': 0.684, 'rule_id': 31, 'samples': 57, 'good_count': 39, 'bad_count': 18}

    # Rule 32: POSITIVE (52.6% confidence, 57 samples)
    if (features.get('pickUpHourOfDay=VERYLATE', 0) == 1 and
        features.get('city=Delhi NCR', 0) == 1 and
        features.get('zone_demand_popularity=POPULARITY_INDEX_2', 0) == 1):
        return {'prediction': 1, 'confidence': 0.526, 'rule_id': 32, 'samples': 57, 'good_count': 30, 'bad_count': 27}

    # Rule 33: POSITIVE (70.4% confidence, 54 samples)
    if (features.get('pickUpHourOfDay=VERYLATE', 0) == 0 and
        features.get('zone_demand_popularity=POPULARITY_INDEX_5', 0) == 1 and
        features.get('pickUpHourOfDay=LATENIGHT', 0) == 1 and
        features.get('city=Mumbai', 0) == 1):
        return {'prediction': 1, 'confidence': 0.704, 'rule_id': 33, 'samples': 54, 'good_count': 38, 'bad_count': 16}

    # Rule 34: NEGATIVE (51.0% confidence, 51 samples)
    if (features.get('pickUpHourOfDay=VERYLATE', 0) == 1 and
        features.get('city=Delhi NCR', 0) == 1 and
        features.get('zone_demand_popularity=POPULARITY_INDEX_2', 0) == 0 and
        features.get('zone_demand_popularity=POPULARITY_INDEX_4', 0) == 1):
        return {'prediction': 0, 'confidence': 0.51, 'rule_id': 34, 'samples': 51, 'good_count': 25, 'bad_count': 26}

    # Default fallback (should not be reached if tree is complete)
    return {'prediction': 0, 'confidence': 0.500, 'rule_id': -1}


def predict_batch(features_list):
    """
    Classify multiple samples
    
    Parameters
    ----------
    features_list : list of dict
        List of feature dictionaries
    
    Returns
    -------
    list of dict
        List of prediction results
    """
    return [predict_sample(features) for features in features_list]


if __name__ == '__main__':
    # Example usage
    sample_features = {
        'source=B2B Portal': 0,
        'source=Phone': 1,
        'source=android': 0,
        'source=ios': 1,
        'source=msite': 0,
        # ... and 349 more features
    }
    
    result = predict_sample(sample_features)
    print(f"Prediction: {result['prediction']}, Confidence: {result['confidence']:.3f}")
    print(f"Total rules in model: 34")