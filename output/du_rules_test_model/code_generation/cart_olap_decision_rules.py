#!/usr/bin/env python3
"""
Generated decision rules for classification from CART-OLAP model
Source: CART-OLAP_test_model
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

    # Rule 1: POSITIVE (90.4% confidence, 13808 samples)
    if (features.get('pickUpHourOfDay=VERYLATE', 0) == 0 and
        features.get('zone_demand_popularity=POPULARITY_INDEX_5', 0) == 0 and
        features.get('pickUpHourOfDay=LATENIGHT', 0) == 0):
        return {'prediction': 1, 'confidence': 0.904, 'rule_id': 1, 'samples': 13808, 'good_count': 12476, 'bad_count': 1332}

    # Rule 2: POSITIVE (88.7% confidence, 1471 samples)
    if (features.get('pickUpHourOfDay=VERYLATE', 0) == 0 and
        features.get('zone_demand_popularity=POPULARITY_INDEX_5', 0) == 1 and
        features.get('pickUpHourOfDay=LATENIGHT', 0) == 0 and
        features.get('city=Pune', 0) == 0 and
        features.get('zone=67', 0) == 0 and
        features.get('city=Mumbai', 0) == 0):
        return {'prediction': 1, 'confidence': 0.887, 'rule_id': 2, 'samples': 1471, 'good_count': 1305, 'bad_count': 166}

    # Rule 3: POSITIVE (72.8% confidence, 1127 samples)
    if (features.get('pickUpHourOfDay=VERYLATE', 0) == 1 and
        features.get('city=Delhi NCR', 0) == 0 and
        features.get('dayType=WEEKEND', 0) == 1 and
        features.get('zone=399', 0) == 0 and
        features.get('city=Chennai', 0) == 0 and
        features.get('zone=216', 0) == 0):
        return {'prediction': 1, 'confidence': 0.728, 'rule_id': 3, 'samples': 1127, 'good_count': 821, 'bad_count': 306}

    # Rule 4: POSITIVE (91.5% confidence, 754 samples)
    if (features.get('pickUpHourOfDay=VERYLATE', 0) == 1 and
        features.get('city=Delhi NCR', 0) == 0 and
        features.get('dayType=WEEKEND', 0) == 0 and
        features.get('city=Pune', 0) == 0 and
        features.get('zone=399', 0) == 0 and
        features.get('city=Hyderabad', 0) == 0):
        return {'prediction': 1, 'confidence': 0.915, 'rule_id': 4, 'samples': 754, 'good_count': 690, 'bad_count': 64}

    # Rule 5: POSITIVE (92.0% confidence, 690 samples)
    if (features.get('pickUpHourOfDay=VERYLATE', 0) == 0 and
        features.get('zone_demand_popularity=POPULARITY_INDEX_5', 0) == 0 and
        features.get('pickUpHourOfDay=LATENIGHT', 0) == 1 and
        features.get('dayType=NORMAL_WEEKDAY', 0) == 1 and
        features.get('zone=500', 0) == 0 and
        features.get('zone=75', 0) == 0):
        return {'prediction': 1, 'confidence': 0.92, 'rule_id': 5, 'samples': 690, 'good_count': 635, 'bad_count': 55}

    # Rule 6: POSITIVE (72.0% confidence, 644 samples)
    if (features.get('pickUpHourOfDay=VERYLATE', 0) == 0 and
        features.get('zone_demand_popularity=POPULARITY_INDEX_5', 0) == 0 and
        features.get('pickUpHourOfDay=LATENIGHT', 0) == 1 and
        features.get('dayType=NORMAL_WEEKDAY', 0) == 0 and
        features.get('zone=217', 0) == 0 and
        features.get('city=Mumbai', 0) == 0):
        return {'prediction': 1, 'confidence': 0.72, 'rule_id': 6, 'samples': 644, 'good_count': 464, 'bad_count': 180}

    # Rule 7: POSITIVE (77.6% confidence, 586 samples)
    if (features.get('pickUpHourOfDay=VERYLATE', 0) == 0 and
        features.get('zone_demand_popularity=POPULARITY_INDEX_5', 0) == 1 and
        features.get('pickUpHourOfDay=LATENIGHT', 0) == 0 and
        features.get('city=Pune', 0) == 0 and
        features.get('zone=67', 0) == 0 and
        features.get('city=Mumbai', 0) == 1):
        return {'prediction': 1, 'confidence': 0.776, 'rule_id': 7, 'samples': 586, 'good_count': 455, 'bad_count': 131}

    # Rule 8: POSITIVE (69.0% confidence, 284 samples)
    if (features.get('pickUpHourOfDay=VERYLATE', 0) == 0 and
        features.get('zone_demand_popularity=POPULARITY_INDEX_5', 0) == 1 and
        features.get('pickUpHourOfDay=LATENIGHT', 0) == 0 and
        features.get('city=Pune', 0) == 1 and
        features.get('zone=329', 0) == 0 and
        features.get('booking_type=outstation', 0) == 0):
        return {'prediction': 1, 'confidence': 0.69, 'rule_id': 8, 'samples': 284, 'good_count': 196, 'bad_count': 88}

    # Rule 9: POSITIVE (83.9% confidence, 230 samples)
    if (features.get('pickUpHourOfDay=VERYLATE', 0) == 0 and
        features.get('zone_demand_popularity=POPULARITY_INDEX_5', 0) == 0 and
        features.get('pickUpHourOfDay=LATENIGHT', 0) == 1 and
        features.get('dayType=NORMAL_WEEKDAY', 0) == 0 and
        features.get('zone=217', 0) == 0 and
        features.get('city=Mumbai', 0) == 1):
        return {'prediction': 1, 'confidence': 0.839, 'rule_id': 9, 'samples': 230, 'good_count': 193, 'bad_count': 37}

    # Rule 10: NEGATIVE (57.4% confidence, 141 samples)
    if (features.get('pickUpHourOfDay=VERYLATE', 0) == 1 and
        features.get('city=Delhi NCR', 0) == 1 and
        features.get('sla=Immediate', 0) == 0 and
        features.get('zone=346', 0) == 0 and
        features.get('zone=360', 0) == 0 and
        features.get('zone=75', 0) == 0):
        return {'prediction': 0, 'confidence': 0.574, 'rule_id': 10, 'samples': 141, 'good_count': 60, 'bad_count': 81}

    # Rule 11: POSITIVE (75.3% confidence, 93 samples)
    if (features.get('pickUpHourOfDay=VERYLATE', 0) == 1 and
        features.get('city=Delhi NCR', 0) == 0 and
        features.get('dayType=WEEKEND', 0) == 0 and
        features.get('city=Pune', 0) == 0 and
        features.get('zone=399', 0) == 0 and
        features.get('city=Hyderabad', 0) == 1):
        return {'prediction': 1, 'confidence': 0.753, 'rule_id': 11, 'samples': 93, 'good_count': 70, 'bad_count': 23}

    # Rule 12: POSITIVE (92.8% confidence, 83 samples)
    if (features.get('pickUpHourOfDay=VERYLATE', 0) == 1 and
        features.get('city=Delhi NCR', 0) == 0 and
        features.get('dayType=WEEKEND', 0) == 1 and
        features.get('zone=399', 0) == 0 and
        features.get('city=Chennai', 0) == 0 and
        features.get('zone=216', 0) == 1):
        return {'prediction': 1, 'confidence': 0.928, 'rule_id': 12, 'samples': 83, 'good_count': 77, 'bad_count': 6}

    # Rule 13: POSITIVE (96.9% confidence, 64 samples)
    if (features.get('pickUpHourOfDay=VERYLATE', 0) == 1 and
        features.get('city=Delhi NCR', 0) == 0 and
        features.get('dayType=WEEKEND', 0) == 1 and
        features.get('zone=399', 0) == 0 and
        features.get('city=Chennai', 0) == 1 and
        features.get('zone=482', 0) == 0):
        return {'prediction': 1, 'confidence': 0.969, 'rule_id': 13, 'samples': 64, 'good_count': 62, 'bad_count': 2}

    # Rule 14: POSITIVE (94.6% confidence, 56 samples)
    if (features.get('pickUpHourOfDay=VERYLATE', 0) == 0 and
        features.get('zone_demand_popularity=POPULARITY_INDEX_5', 0) == 1 and
        features.get('pickUpHourOfDay=LATENIGHT', 0) == 0 and
        features.get('city=Pune', 0) == 1 and
        features.get('zone=329', 0) == 0 and
        features.get('booking_type=outstation', 0) == 1):
        return {'prediction': 1, 'confidence': 0.946, 'rule_id': 14, 'samples': 56, 'good_count': 53, 'bad_count': 3}

    # Rule 15: POSITIVE (52.7% confidence, 55 samples)
    if (features.get('pickUpHourOfDay=VERYLATE', 0) == 0 and
        features.get('zone_demand_popularity=POPULARITY_INDEX_5', 0) == 1 and
        features.get('pickUpHourOfDay=LATENIGHT', 0) == 1 and
        features.get('city=Mumbai', 0) == 0 and
        features.get('zone=339', 0) == 0 and
        features.get('dayType=WEEKEND', 0) == 0):
        return {'prediction': 1, 'confidence': 0.527, 'rule_id': 15, 'samples': 55, 'good_count': 29, 'bad_count': 26}

    # Rule 16: POSITIVE (76.0% confidence, 50 samples)
    if (features.get('pickUpHourOfDay=VERYLATE', 0) == 0 and
        features.get('zone_demand_popularity=POPULARITY_INDEX_5', 0) == 1 and
        features.get('pickUpHourOfDay=LATENIGHT', 0) == 1 and
        features.get('city=Mumbai', 0) == 1 and
        features.get('zone=401', 0) == 0 and
        features.get('zone=467', 0) == 0):
        return {'prediction': 1, 'confidence': 0.76, 'rule_id': 16, 'samples': 50, 'good_count': 38, 'bad_count': 12}

    # Rule 17: POSITIVE (100.0% confidence, 38 samples)
    if (features.get('pickUpHourOfDay=VERYLATE', 0) == 0 and
        features.get('zone_demand_popularity=POPULARITY_INDEX_5', 0) == 0 and
        features.get('pickUpHourOfDay=LATENIGHT', 0) == 1 and
        features.get('dayType=NORMAL_WEEKDAY', 0) == 0 and
        features.get('zone=217', 0) == 1 and
        features.get('dayType=FRIDAY', 0) == 0):
        return {'prediction': 1, 'confidence': 1.0, 'rule_id': 17, 'samples': 38, 'good_count': 38, 'bad_count': 0}

    # Rule 18: POSITIVE (91.7% confidence, 24 samples)
    if (features.get('pickUpHourOfDay=VERYLATE', 0) == 0 and
        features.get('zone_demand_popularity=POPULARITY_INDEX_5', 0) == 0 and
        features.get('pickUpHourOfDay=LATENIGHT', 0) == 1 and
        features.get('dayType=NORMAL_WEEKDAY', 0) == 0 and
        features.get('zone=217', 0) == 1 and
        features.get('dayType=FRIDAY', 0) == 1):
        return {'prediction': 1, 'confidence': 0.917, 'rule_id': 18, 'samples': 24, 'good_count': 22, 'bad_count': 2}

    # Rule 19: NEGATIVE (66.7% confidence, 24 samples)
    if (features.get('pickUpHourOfDay=VERYLATE', 0) == 0 and
        features.get('zone_demand_popularity=POPULARITY_INDEX_5', 0) == 1 and
        features.get('pickUpHourOfDay=LATENIGHT', 0) == 1 and
        features.get('city=Mumbai', 0) == 0 and
        features.get('zone=339', 0) == 0 and
        features.get('dayType=WEEKEND', 0) == 1):
        return {'prediction': 0, 'confidence': 0.667, 'rule_id': 19, 'samples': 24, 'good_count': 8, 'bad_count': 16}

    # Rule 20: NEGATIVE (72.2% confidence, 18 samples)
    if (features.get('pickUpHourOfDay=VERYLATE', 0) == 0 and
        features.get('zone_demand_popularity=POPULARITY_INDEX_5', 0) == 1 and
        features.get('pickUpHourOfDay=LATENIGHT', 0) == 0 and
        features.get('city=Pune', 0) == 0 and
        features.get('zone=67', 0) == 1):
        return {'prediction': 0, 'confidence': 0.722, 'rule_id': 20, 'samples': 18, 'good_count': 5, 'bad_count': 13}

    # Rule 21: NEGATIVE (83.3% confidence, 18 samples)
    if (features.get('pickUpHourOfDay=VERYLATE', 0) == 1 and
        features.get('city=Delhi NCR', 0) == 0 and
        features.get('dayType=WEEKEND', 0) == 1 and
        features.get('zone=399', 0) == 1):
        return {'prediction': 0, 'confidence': 0.833, 'rule_id': 21, 'samples': 18, 'good_count': 3, 'bad_count': 15}

    # Rule 22: NEGATIVE (64.3% confidence, 14 samples)
    if (features.get('pickUpHourOfDay=VERYLATE', 0) == 1 and
        features.get('city=Delhi NCR', 0) == 0 and
        features.get('dayType=WEEKEND', 0) == 0 and
        features.get('city=Pune', 0) == 1):
        return {'prediction': 0, 'confidence': 0.643, 'rule_id': 22, 'samples': 14, 'good_count': 5, 'bad_count': 9}

    # Rule 23: NEGATIVE (76.9% confidence, 13 samples)
    if (features.get('pickUpHourOfDay=VERYLATE', 0) == 0 and
        features.get('zone_demand_popularity=POPULARITY_INDEX_5', 0) == 1 and
        features.get('pickUpHourOfDay=LATENIGHT', 0) == 0 and
        features.get('city=Pune', 0) == 1 and
        features.get('zone=329', 0) == 1):
        return {'prediction': 0, 'confidence': 0.769, 'rule_id': 23, 'samples': 13, 'good_count': 3, 'bad_count': 10}

    # Rule 24: NEGATIVE (90.9% confidence, 11 samples)
    if (features.get('pickUpHourOfDay=VERYLATE', 0) == 1 and
        features.get('city=Delhi NCR', 0) == 1 and
        features.get('sla=Immediate', 0) == 0 and
        features.get('zone=346', 0) == 0 and
        features.get('zone=360', 0) == 0 and
        features.get('zone=75', 0) == 1):
        return {'prediction': 0, 'confidence': 0.909, 'rule_id': 24, 'samples': 11, 'good_count': 1, 'bad_count': 10}

    # Rule 25: NEGATIVE (87.5% confidence, 8 samples)
    if (features.get('pickUpHourOfDay=VERYLATE', 0) == 0 and
        features.get('zone_demand_popularity=POPULARITY_INDEX_5', 0) == 0 and
        features.get('pickUpHourOfDay=LATENIGHT', 0) == 1 and
        features.get('dayType=NORMAL_WEEKDAY', 0) == 1 and
        features.get('zone=500', 0) == 1):
        return {'prediction': 0, 'confidence': 0.875, 'rule_id': 25, 'samples': 8, 'good_count': 1, 'bad_count': 7}

    # Rule 26: NEGATIVE (71.4% confidence, 7 samples)
    if (features.get('pickUpHourOfDay=VERYLATE', 0) == 1 and
        features.get('city=Delhi NCR', 0) == 0 and
        features.get('dayType=WEEKEND', 0) == 0 and
        features.get('city=Pune', 0) == 0 and
        features.get('zone=399', 0) == 1):
        return {'prediction': 0, 'confidence': 0.714, 'rule_id': 26, 'samples': 7, 'good_count': 2, 'bad_count': 5}

    # Rule 27: POSITIVE (100.0% confidence, 7 samples)
    if (features.get('pickUpHourOfDay=VERYLATE', 0) == 1 and
        features.get('city=Delhi NCR', 0) == 1 and
        features.get('sla=Immediate', 0) == 1):
        return {'prediction': 1, 'confidence': 1.0, 'rule_id': 27, 'samples': 7, 'good_count': 7, 'bad_count': 0}

    # Rule 28: POSITIVE (100.0% confidence, 6 samples)
    if (features.get('pickUpHourOfDay=VERYLATE', 0) == 0 and
        features.get('zone_demand_popularity=POPULARITY_INDEX_5', 0) == 1 and
        features.get('pickUpHourOfDay=LATENIGHT', 0) == 1 and
        features.get('city=Mumbai', 0) == 0 and
        features.get('zone=339', 0) == 1):
        return {'prediction': 1, 'confidence': 1.0, 'rule_id': 28, 'samples': 6, 'good_count': 6, 'bad_count': 0}

    # Rule 29: POSITIVE (100.0% confidence, 5 samples)
    if (features.get('pickUpHourOfDay=VERYLATE', 0) == 1 and
        features.get('city=Delhi NCR', 0) == 1 and
        features.get('sla=Immediate', 0) == 0 and
        features.get('zone=346', 0) == 1):
        return {'prediction': 1, 'confidence': 1.0, 'rule_id': 29, 'samples': 5, 'good_count': 5, 'bad_count': 0}

    # Rule 30: NEGATIVE (100.0% confidence, 4 samples)
    if (features.get('pickUpHourOfDay=VERYLATE', 0) == 0 and
        features.get('zone_demand_popularity=POPULARITY_INDEX_5', 0) == 0 and
        features.get('pickUpHourOfDay=LATENIGHT', 0) == 1 and
        features.get('dayType=NORMAL_WEEKDAY', 0) == 1 and
        features.get('zone=500', 0) == 0 and
        features.get('zone=75', 0) == 1):
        return {'prediction': 0, 'confidence': 1.0, 'rule_id': 30, 'samples': 4, 'good_count': 0, 'bad_count': 4}

    # Rule 31: POSITIVE (100.0% confidence, 4 samples)
    if (features.get('pickUpHourOfDay=VERYLATE', 0) == 1 and
        features.get('city=Delhi NCR', 0) == 1 and
        features.get('sla=Immediate', 0) == 0 and
        features.get('zone=346', 0) == 0 and
        features.get('zone=360', 0) == 1):
        return {'prediction': 1, 'confidence': 1.0, 'rule_id': 31, 'samples': 4, 'good_count': 4, 'bad_count': 0}

    # Rule 32: NEGATIVE (100.0% confidence, 2 samples)
    if (features.get('pickUpHourOfDay=VERYLATE', 0) == 0 and
        features.get('zone_demand_popularity=POPULARITY_INDEX_5', 0) == 1 and
        features.get('pickUpHourOfDay=LATENIGHT', 0) == 1 and
        features.get('city=Mumbai', 0) == 1 and
        features.get('zone=401', 0) == 0 and
        features.get('zone=467', 0) == 1):
        return {'prediction': 0, 'confidence': 1.0, 'rule_id': 32, 'samples': 2, 'good_count': 0, 'bad_count': 2}

    # Rule 33: NEGATIVE (100.0% confidence, 2 samples)
    if (features.get('pickUpHourOfDay=VERYLATE', 0) == 0 and
        features.get('zone_demand_popularity=POPULARITY_INDEX_5', 0) == 1 and
        features.get('pickUpHourOfDay=LATENIGHT', 0) == 1 and
        features.get('city=Mumbai', 0) == 1 and
        features.get('zone=401', 0) == 1):
        return {'prediction': 0, 'confidence': 1.0, 'rule_id': 33, 'samples': 2, 'good_count': 0, 'bad_count': 2}

    # Rule 34: POSITIVE (50.0% confidence, 2 samples)
    if (features.get('pickUpHourOfDay=VERYLATE', 0) == 1 and
        features.get('city=Delhi NCR', 0) == 0 and
        features.get('dayType=WEEKEND', 0) == 1 and
        features.get('zone=399', 0) == 0 and
        features.get('city=Chennai', 0) == 1 and
        features.get('zone=482', 0) == 1):
        return {'prediction': 1, 'confidence': 0.5, 'rule_id': 34, 'samples': 2, 'good_count': 1, 'bad_count': 1}

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