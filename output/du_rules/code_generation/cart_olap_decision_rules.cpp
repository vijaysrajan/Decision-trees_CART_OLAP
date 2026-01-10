// Generated decision rules for classification from CART-OLAP model
// Source: CART-OLAP_du_model_cli
// Total rules: 34
// Feature count: 354

#include <unordered_map>
#include <string>
#include <vector>
#include <iostream>

struct PredictionResult {
    int prediction;
    double confidence;
    int rule_id;
    int samples;
    int good_count;
    int bad_count;
};

// Helper function to get feature value with default
inline int get_feature(const std::unordered_map<std::string, int>& features, const std::string& name) {
    auto it = features.find(name);
    return (it != features.end()) ? it->second : 0;
}

/**
 * Classify a single sample using decision rules
 * @param features Feature map with binary values (0/1)
 * @return Prediction result with confidence and metadata
 */
PredictionResult predict(const std::unordered_map<std::string, int>& features) {

    // Rule 1: POSITIVE (90.4% confidence, 12794 samples)
    if (get_feature(features, "pickUpHourOfDay=VERYLATE") == 0 &&
        get_feature(features, "zone_demand_popularity=POPULARITY_INDEX_5") == 0 &&
        get_feature(features, "pickUpHourOfDay=LATENIGHT") == 0 &&
        get_feature(features, "zone=221") == 0 &&
        get_feature(features, "zone=194") == 0 &&
        get_feature(features, "sla=Immediate") == 0) {
        return {1, 0.904, 1, 12794, 11560, 1234};
    }

    // Rule 2: POSITIVE (89.0% confidence, 1397 samples)
    if (get_feature(features, "pickUpHourOfDay=VERYLATE") == 0 &&
        get_feature(features, "zone_demand_popularity=POPULARITY_INDEX_5") == 1 &&
        get_feature(features, "pickUpHourOfDay=LATENIGHT") == 0 &&
        get_feature(features, "city=Pune") == 0 &&
        get_feature(features, "city=Mumbai") == 0 &&
        get_feature(features, "city=Hyderabad") == 0) {
        return {1, 0.890, 2, 1397, 1244, 153};
    }

    // Rule 3: POSITIVE (74.4% confidence, 996 samples)
    if (get_feature(features, "pickUpHourOfDay=VERYLATE") == 1 &&
        get_feature(features, "city=Delhi NCR") == 0 &&
        get_feature(features, "dayType=WEEKEND") == 1 &&
        get_feature(features, "city=Chennai") == 0 &&
        get_feature(features, "zone_demand_popularity=POPULARITY_INDEX_4") == 0 &&
        get_feature(features, "zone=216") == 0) {
        return {1, 0.744, 3, 996, 741, 255};
    }

    // Rule 4: POSITIVE (99.0% confidence, 697 samples)
    if (get_feature(features, "pickUpHourOfDay=VERYLATE") == 0 &&
        get_feature(features, "zone_demand_popularity=POPULARITY_INDEX_5") == 0 &&
        get_feature(features, "pickUpHourOfDay=LATENIGHT") == 0 &&
        get_feature(features, "zone=221") == 0 &&
        get_feature(features, "zone=194") == 0 &&
        get_feature(features, "sla=Immediate") == 1) {
        return {1, 0.990, 4, 697, 690, 7};
    }

    // Rule 5: POSITIVE (72.0% confidence, 644 samples)
    if (get_feature(features, "pickUpHourOfDay=VERYLATE") == 0 &&
        get_feature(features, "zone_demand_popularity=POPULARITY_INDEX_5") == 0 &&
        get_feature(features, "pickUpHourOfDay=LATENIGHT") == 1 &&
        get_feature(features, "dayType=NORMAL_WEEKDAY") == 0 &&
        get_feature(features, "zone=217") == 0 &&
        get_feature(features, "city=Mumbai") == 0) {
        return {1, 0.720, 5, 644, 464, 180};
    }

    // Rule 6: POSITIVE (82.1% confidence, 397 samples)
    if (get_feature(features, "pickUpHourOfDay=VERYLATE") == 0 &&
        get_feature(features, "zone_demand_popularity=POPULARITY_INDEX_5") == 1 &&
        get_feature(features, "pickUpHourOfDay=LATENIGHT") == 0 &&
        get_feature(features, "city=Pune") == 0 &&
        get_feature(features, "city=Mumbai") == 1 &&
        get_feature(features, "booking_type=round_trip") == 0) {
        return {1, 0.821, 6, 397, 326, 71};
    }

    // Rule 7: POSITIVE (88.6% confidence, 395 samples)
    if (get_feature(features, "pickUpHourOfDay=VERYLATE") == 1 &&
        get_feature(features, "city=Delhi NCR") == 0 &&
        get_feature(features, "dayType=WEEKEND") == 0 &&
        get_feature(features, "zone_demand_popularity=POPULARITY_INDEX_5") == 0 &&
        get_feature(features, "city=Hyderabad") == 0 &&
        get_feature(features, "zone_demand_popularity=POPULARITY_INDEX_1") == 0) {
        return {1, 0.886, 7, 395, 350, 45};
    }

    // Rule 8: POSITIVE (95.4% confidence, 326 samples)
    if (get_feature(features, "pickUpHourOfDay=VERYLATE") == 1 &&
        get_feature(features, "city=Delhi NCR") == 0 &&
        get_feature(features, "dayType=WEEKEND") == 0 &&
        get_feature(features, "zone_demand_popularity=POPULARITY_INDEX_5") == 0 &&
        get_feature(features, "city=Hyderabad") == 0 &&
        get_feature(features, "zone_demand_popularity=POPULARITY_INDEX_1") == 1) {
        return {1, 0.954, 8, 326, 311, 15};
    }

    // Rule 9: POSITIVE (81.9% confidence, 249 samples)
    if (get_feature(features, "pickUpHourOfDay=VERYLATE") == 0 &&
        get_feature(features, "zone_demand_popularity=POPULARITY_INDEX_5") == 0 &&
        get_feature(features, "pickUpHourOfDay=LATENIGHT") == 1 &&
        get_feature(features, "dayType=NORMAL_WEEKDAY") == 1 &&
        get_feature(features, "zone_demand_popularity=POPULARITY_INDEX_1") == 0 &&
        get_feature(features, "city=Mumbai") == 0) {
        return {1, 0.819, 9, 249, 204, 45};
    }

    // Rule 10: POSITIVE (94.2% confidence, 241 samples)
    if (get_feature(features, "pickUpHourOfDay=VERYLATE") == 0 &&
        get_feature(features, "zone_demand_popularity=POPULARITY_INDEX_5") == 0 &&
        get_feature(features, "pickUpHourOfDay=LATENIGHT") == 1 &&
        get_feature(features, "dayType=NORMAL_WEEKDAY") == 1 &&
        get_feature(features, "zone_demand_popularity=POPULARITY_INDEX_1") == 1 &&
        get_feature(features, "zone=219") == 0) {
        return {1, 0.942, 10, 241, 227, 14};
    }

    // Rule 11: POSITIVE (83.9% confidence, 230 samples)
    if (get_feature(features, "pickUpHourOfDay=VERYLATE") == 0 &&
        get_feature(features, "zone_demand_popularity=POPULARITY_INDEX_5") == 0 &&
        get_feature(features, "pickUpHourOfDay=LATENIGHT") == 1 &&
        get_feature(features, "dayType=NORMAL_WEEKDAY") == 0 &&
        get_feature(features, "zone=217") == 0 &&
        get_feature(features, "city=Mumbai") == 1) {
        return {1, 0.839, 11, 230, 193, 37};
    }

    // Rule 12: POSITIVE (61.2% confidence, 201 samples)
    if (get_feature(features, "pickUpHourOfDay=VERYLATE") == 0 &&
        get_feature(features, "zone_demand_popularity=POPULARITY_INDEX_5") == 1 &&
        get_feature(features, "pickUpHourOfDay=LATENIGHT") == 0 &&
        get_feature(features, "city=Pune") == 1 &&
        get_feature(features, "booking_type=outstation") == 0 &&
        get_feature(features, "pickUpHourOfDay=MORNING") == 0) {
        return {1, 0.612, 12, 201, 123, 78};
    }

    // Rule 13: POSITIVE (68.3% confidence, 189 samples)
    if (get_feature(features, "pickUpHourOfDay=VERYLATE") == 0 &&
        get_feature(features, "zone_demand_popularity=POPULARITY_INDEX_5") == 1 &&
        get_feature(features, "pickUpHourOfDay=LATENIGHT") == 0 &&
        get_feature(features, "city=Pune") == 0 &&
        get_feature(features, "city=Mumbai") == 1 &&
        get_feature(features, "booking_type=round_trip") == 1) {
        return {1, 0.683, 13, 189, 129, 60};
    }

    // Rule 14: POSITIVE (96.6% confidence, 116 samples)
    if (get_feature(features, "pickUpHourOfDay=VERYLATE") == 0 &&
        get_feature(features, "zone_demand_popularity=POPULARITY_INDEX_5") == 0 &&
        get_feature(features, "pickUpHourOfDay=LATENIGHT") == 1 &&
        get_feature(features, "dayType=NORMAL_WEEKDAY") == 1 &&
        get_feature(features, "zone_demand_popularity=POPULARITY_INDEX_1") == 0 &&
        get_feature(features, "city=Mumbai") == 1) {
        return {1, 0.966, 14, 116, 112, 4};
    }

    // Rule 15: POSITIVE (84.5% confidence, 97 samples)
    if (get_feature(features, "pickUpHourOfDay=VERYLATE") == 0 &&
        get_feature(features, "zone_demand_popularity=POPULARITY_INDEX_5") == 0 &&
        get_feature(features, "pickUpHourOfDay=LATENIGHT") == 0 &&
        get_feature(features, "zone=221") == 1 &&
        get_feature(features, "booking_type=one_way_trip") == 0 &&
        get_feature(features, "estimated_usage_bins=GT_3_LTE_4_HOURS") == 0) {
        return {1, 0.845, 15, 97, 82, 15};
    }

    // Rule 16: POSITIVE (96.9% confidence, 96 samples)
    if (get_feature(features, "pickUpHourOfDay=VERYLATE") == 0 &&
        get_feature(features, "zone_demand_popularity=POPULARITY_INDEX_5") == 0 &&
        get_feature(features, "pickUpHourOfDay=LATENIGHT") == 1 &&
        get_feature(features, "dayType=NORMAL_WEEKDAY") == 1 &&
        get_feature(features, "zone_demand_popularity=POPULARITY_INDEX_1") == 1 &&
        get_feature(features, "zone=219") == 1) {
        return {1, 0.969, 16, 96, 93, 3};
    }

    // Rule 17: POSITIVE (71.7% confidence, 92 samples)
    if (get_feature(features, "pickUpHourOfDay=VERYLATE") == 0 &&
        get_feature(features, "zone_demand_popularity=POPULARITY_INDEX_5") == 1 &&
        get_feature(features, "pickUpHourOfDay=LATENIGHT") == 0 &&
        get_feature(features, "city=Pune") == 0 &&
        get_feature(features, "city=Mumbai") == 0 &&
        get_feature(features, "city=Hyderabad") == 1) {
        return {1, 0.717, 17, 92, 66, 26};
    }

    // Rule 18: POSITIVE (61.1% confidence, 90 samples)
    if (get_feature(features, "pickUpHourOfDay=VERYLATE") == 0 &&
        get_feature(features, "zone_demand_popularity=POPULARITY_INDEX_5") == 0 &&
        get_feature(features, "pickUpHourOfDay=LATENIGHT") == 0 &&
        get_feature(features, "zone=221") == 1 &&
        get_feature(features, "booking_type=one_way_trip") == 1) {
        return {1, 0.611, 18, 90, 55, 35};
    }

    // Rule 19: POSITIVE (81.1% confidence, 90 samples)
    if (get_feature(features, "pickUpHourOfDay=VERYLATE") == 0 &&
        get_feature(features, "zone_demand_popularity=POPULARITY_INDEX_5") == 1 &&
        get_feature(features, "pickUpHourOfDay=LATENIGHT") == 0 &&
        get_feature(features, "city=Pune") == 1 &&
        get_feature(features, "booking_type=outstation") == 0 &&
        get_feature(features, "pickUpHourOfDay=MORNING") == 1) {
        return {1, 0.811, 19, 90, 73, 17};
    }

    // Rule 20: POSITIVE (74.4% confidence, 90 samples)
    if (get_feature(features, "pickUpHourOfDay=VERYLATE") == 1 &&
        get_feature(features, "city=Delhi NCR") == 0 &&
        get_feature(features, "dayType=WEEKEND") == 0 &&
        get_feature(features, "zone_demand_popularity=POPULARITY_INDEX_5") == 0 &&
        get_feature(features, "city=Hyderabad") == 1) {
        return {1, 0.744, 20, 90, 67, 23};
    }

    // Rule 21: POSITIVE (50.6% confidence, 85 samples)
    if (get_feature(features, "pickUpHourOfDay=VERYLATE") == 0 &&
        get_feature(features, "zone_demand_popularity=POPULARITY_INDEX_5") == 1 &&
        get_feature(features, "pickUpHourOfDay=LATENIGHT") == 1 &&
        get_feature(features, "city=Mumbai") == 0) {
        return {1, 0.506, 21, 85, 43, 42};
    }

    // Rule 22: POSITIVE (92.8% confidence, 83 samples)
    if (get_feature(features, "pickUpHourOfDay=VERYLATE") == 1 &&
        get_feature(features, "city=Delhi NCR") == 0 &&
        get_feature(features, "dayType=WEEKEND") == 1 &&
        get_feature(features, "city=Chennai") == 0 &&
        get_feature(features, "zone_demand_popularity=POPULARITY_INDEX_4") == 0 &&
        get_feature(features, "zone=216") == 1) {
        return {1, 0.928, 22, 83, 77, 6};
    }

    // Rule 23: POSITIVE (51.8% confidence, 83 samples)
    if (get_feature(features, "pickUpHourOfDay=VERYLATE") == 1 &&
        get_feature(features, "city=Delhi NCR") == 0 &&
        get_feature(features, "dayType=WEEKEND") == 1 &&
        get_feature(features, "city=Chennai") == 0 &&
        get_feature(features, "zone_demand_popularity=POPULARITY_INDEX_4") == 1 &&
        get_feature(features, "city=Mumbai") == 1) {
        return {1, 0.518, 23, 83, 43, 40};
    }

    // Rule 24: POSITIVE (60.9% confidence, 69 samples)
    if (get_feature(features, "pickUpHourOfDay=VERYLATE") == 0 &&
        get_feature(features, "zone_demand_popularity=POPULARITY_INDEX_5") == 0 &&
        get_feature(features, "pickUpHourOfDay=LATENIGHT") == 0 &&
        get_feature(features, "zone=221") == 0 &&
        get_feature(features, "zone=194") == 1) {
        return {1, 0.609, 24, 69, 42, 27};
    }

    // Rule 25: POSITIVE (60.6% confidence, 66 samples)
    if (get_feature(features, "pickUpHourOfDay=VERYLATE") == 1 &&
        get_feature(features, "city=Delhi NCR") == 0 &&
        get_feature(features, "dayType=WEEKEND") == 1 &&
        get_feature(features, "city=Chennai") == 0 &&
        get_feature(features, "zone_demand_popularity=POPULARITY_INDEX_4") == 1 &&
        get_feature(features, "city=Mumbai") == 0) {
        return {1, 0.606, 25, 66, 40, 26};
    }

    // Rule 26: POSITIVE (95.5% confidence, 66 samples)
    if (get_feature(features, "pickUpHourOfDay=VERYLATE") == 1 &&
        get_feature(features, "city=Delhi NCR") == 0 &&
        get_feature(features, "dayType=WEEKEND") == 1 &&
        get_feature(features, "city=Chennai") == 1) {
        return {1, 0.955, 26, 66, 63, 3};
    }

    // Rule 27: POSITIVE (96.8% confidence, 62 samples)
    if (get_feature(features, "pickUpHourOfDay=VERYLATE") == 0 &&
        get_feature(features, "zone_demand_popularity=POPULARITY_INDEX_5") == 0 &&
        get_feature(features, "pickUpHourOfDay=LATENIGHT") == 1 &&
        get_feature(features, "dayType=NORMAL_WEEKDAY") == 0 &&
        get_feature(features, "zone=217") == 1) {
        return {1, 0.968, 27, 62, 60, 2};
    }

    // Rule 28: POSITIVE (90.3% confidence, 62 samples)
    if (get_feature(features, "pickUpHourOfDay=VERYLATE") == 0 &&
        get_feature(features, "zone_demand_popularity=POPULARITY_INDEX_5") == 1 &&
        get_feature(features, "pickUpHourOfDay=LATENIGHT") == 0 &&
        get_feature(features, "city=Pune") == 1 &&
        get_feature(features, "booking_type=outstation") == 1) {
        return {1, 0.903, 28, 62, 56, 6};
    }

    // Rule 29: POSITIVE (77.0% confidence, 61 samples)
    if (get_feature(features, "pickUpHourOfDay=VERYLATE") == 0 &&
        get_feature(features, "zone_demand_popularity=POPULARITY_INDEX_5") == 0 &&
        get_feature(features, "pickUpHourOfDay=LATENIGHT") == 0 &&
        get_feature(features, "zone=221") == 1 &&
        get_feature(features, "booking_type=one_way_trip") == 0 &&
        get_feature(features, "estimated_usage_bins=GT_3_LTE_4_HOURS") == 1) {
        return {1, 0.770, 29, 61, 47, 14};
    }

    // Rule 30: NEGATIVE (63.3% confidence, 60 samples)
    if (get_feature(features, "pickUpHourOfDay=VERYLATE") == 1 &&
        get_feature(features, "city=Delhi NCR") == 1 &&
        get_feature(features, "zone_demand_popularity=POPULARITY_INDEX_2") == 0 &&
        get_feature(features, "zone_demand_popularity=POPULARITY_INDEX_4") == 0) {
        return {0, 0.633, 30, 60, 22, 38};
    }

    // Rule 31: POSITIVE (68.4% confidence, 57 samples)
    if (get_feature(features, "pickUpHourOfDay=VERYLATE") == 1 &&
        get_feature(features, "city=Delhi NCR") == 0 &&
        get_feature(features, "dayType=WEEKEND") == 0 &&
        get_feature(features, "zone_demand_popularity=POPULARITY_INDEX_5") == 1) {
        return {1, 0.684, 31, 57, 39, 18};
    }

    // Rule 32: POSITIVE (52.6% confidence, 57 samples)
    if (get_feature(features, "pickUpHourOfDay=VERYLATE") == 1 &&
        get_feature(features, "city=Delhi NCR") == 1 &&
        get_feature(features, "zone_demand_popularity=POPULARITY_INDEX_2") == 1) {
        return {1, 0.526, 32, 57, 30, 27};
    }

    // Rule 33: POSITIVE (70.4% confidence, 54 samples)
    if (get_feature(features, "pickUpHourOfDay=VERYLATE") == 0 &&
        get_feature(features, "zone_demand_popularity=POPULARITY_INDEX_5") == 1 &&
        get_feature(features, "pickUpHourOfDay=LATENIGHT") == 1 &&
        get_feature(features, "city=Mumbai") == 1) {
        return {1, 0.704, 33, 54, 38, 16};
    }

    // Rule 34: NEGATIVE (51.0% confidence, 51 samples)
    if (get_feature(features, "pickUpHourOfDay=VERYLATE") == 1 &&
        get_feature(features, "city=Delhi NCR") == 1 &&
        get_feature(features, "zone_demand_popularity=POPULARITY_INDEX_2") == 0 &&
        get_feature(features, "zone_demand_popularity=POPULARITY_INDEX_4") == 1) {
        return {0, 0.510, 34, 51, 25, 26};
    }

    // Default fallback
    return {0, 0.500, -1, 0, 0, 0};
}

/**
 * Classify multiple samples
 * @param features_list Vector of feature maps
 * @return Vector of prediction results
 */
std::vector<PredictionResult> predict_batch(const std::vector<std::unordered_map<std::string, int>>& features_list) {
    std::vector<PredictionResult> results;
    results.reserve(features_list.size());
    
    for (const auto& features : features_list) {
        results.push_back(predict(features));
    }
    
    return results;
}

// Example usage
int main() {
    std::unordered_map<std::string, int> sample_features = {
        {"source=B2B Portal", 0},
        {"source=Phone", 1},
        {"source=android", 0}
    };
    
    auto result = predict(sample_features);
    std::cout << "Prediction: " << result.prediction << ", Confidence: " << result.confidence << std::endl;
    std::cout << "Total rules in model: 34" << std::endl;
    
    return 0;
}