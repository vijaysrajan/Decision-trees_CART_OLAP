// Generated decision rules for classification from CART-OLAP model
// Source: CART-OLAP_test_model
// Total rules: 34
// Feature count: 354

import java.util.*;

public class CartOlapDecisionRules {

    public record PredictionResult(int prediction, double confidence, int ruleId, int samples, int goodCount, int badCount) {}

    /**
     * Classify a single sample using decision rules
     * @param features Feature map with binary values (0/1)
     * @return Prediction result with confidence and metadata
     */
    public static PredictionResult predict(Map<String, Integer> features) {

        // Rule 1: POSITIVE (90.4% confidence, 13808 samples)
        if (features.getOrDefault("pickUpHourOfDay=VERYLATE", 0) == 0 &&
            features.getOrDefault("zone_demand_popularity=POPULARITY_INDEX_5", 0) == 0 &&
            features.getOrDefault("pickUpHourOfDay=LATENIGHT", 0) == 0) {
            return new PredictionResult(1, 0.904, 1, 13808, 12476, 1332);
        }

        // Rule 2: POSITIVE (88.7% confidence, 1471 samples)
        if (features.getOrDefault("pickUpHourOfDay=VERYLATE", 0) == 0 &&
            features.getOrDefault("zone_demand_popularity=POPULARITY_INDEX_5", 0) == 1 &&
            features.getOrDefault("pickUpHourOfDay=LATENIGHT", 0) == 0 &&
            features.getOrDefault("city=Pune", 0) == 0 &&
            features.getOrDefault("zone=67", 0) == 0 &&
            features.getOrDefault("city=Mumbai", 0) == 0) {
            return new PredictionResult(1, 0.887, 2, 1471, 1305, 166);
        }

        // Rule 3: POSITIVE (72.8% confidence, 1127 samples)
        if (features.getOrDefault("pickUpHourOfDay=VERYLATE", 0) == 1 &&
            features.getOrDefault("city=Delhi NCR", 0) == 0 &&
            features.getOrDefault("dayType=WEEKEND", 0) == 1 &&
            features.getOrDefault("zone=399", 0) == 0 &&
            features.getOrDefault("city=Chennai", 0) == 0 &&
            features.getOrDefault("zone=216", 0) == 0) {
            return new PredictionResult(1, 0.728, 3, 1127, 821, 306);
        }

        // Rule 4: POSITIVE (91.5% confidence, 754 samples)
        if (features.getOrDefault("pickUpHourOfDay=VERYLATE", 0) == 1 &&
            features.getOrDefault("city=Delhi NCR", 0) == 0 &&
            features.getOrDefault("dayType=WEEKEND", 0) == 0 &&
            features.getOrDefault("city=Pune", 0) == 0 &&
            features.getOrDefault("zone=399", 0) == 0 &&
            features.getOrDefault("city=Hyderabad", 0) == 0) {
            return new PredictionResult(1, 0.915, 4, 754, 690, 64);
        }

        // Rule 5: POSITIVE (92.0% confidence, 690 samples)
        if (features.getOrDefault("pickUpHourOfDay=VERYLATE", 0) == 0 &&
            features.getOrDefault("zone_demand_popularity=POPULARITY_INDEX_5", 0) == 0 &&
            features.getOrDefault("pickUpHourOfDay=LATENIGHT", 0) == 1 &&
            features.getOrDefault("dayType=NORMAL_WEEKDAY", 0) == 1 &&
            features.getOrDefault("zone=500", 0) == 0 &&
            features.getOrDefault("zone=75", 0) == 0) {
            return new PredictionResult(1, 0.920, 5, 690, 635, 55);
        }

        // Rule 6: POSITIVE (72.0% confidence, 644 samples)
        if (features.getOrDefault("pickUpHourOfDay=VERYLATE", 0) == 0 &&
            features.getOrDefault("zone_demand_popularity=POPULARITY_INDEX_5", 0) == 0 &&
            features.getOrDefault("pickUpHourOfDay=LATENIGHT", 0) == 1 &&
            features.getOrDefault("dayType=NORMAL_WEEKDAY", 0) == 0 &&
            features.getOrDefault("zone=217", 0) == 0 &&
            features.getOrDefault("city=Mumbai", 0) == 0) {
            return new PredictionResult(1, 0.720, 6, 644, 464, 180);
        }

        // Rule 7: POSITIVE (77.6% confidence, 586 samples)
        if (features.getOrDefault("pickUpHourOfDay=VERYLATE", 0) == 0 &&
            features.getOrDefault("zone_demand_popularity=POPULARITY_INDEX_5", 0) == 1 &&
            features.getOrDefault("pickUpHourOfDay=LATENIGHT", 0) == 0 &&
            features.getOrDefault("city=Pune", 0) == 0 &&
            features.getOrDefault("zone=67", 0) == 0 &&
            features.getOrDefault("city=Mumbai", 0) == 1) {
            return new PredictionResult(1, 0.776, 7, 586, 455, 131);
        }

        // Rule 8: POSITIVE (69.0% confidence, 284 samples)
        if (features.getOrDefault("pickUpHourOfDay=VERYLATE", 0) == 0 &&
            features.getOrDefault("zone_demand_popularity=POPULARITY_INDEX_5", 0) == 1 &&
            features.getOrDefault("pickUpHourOfDay=LATENIGHT", 0) == 0 &&
            features.getOrDefault("city=Pune", 0) == 1 &&
            features.getOrDefault("zone=329", 0) == 0 &&
            features.getOrDefault("booking_type=outstation", 0) == 0) {
            return new PredictionResult(1, 0.690, 8, 284, 196, 88);
        }

        // Rule 9: POSITIVE (83.9% confidence, 230 samples)
        if (features.getOrDefault("pickUpHourOfDay=VERYLATE", 0) == 0 &&
            features.getOrDefault("zone_demand_popularity=POPULARITY_INDEX_5", 0) == 0 &&
            features.getOrDefault("pickUpHourOfDay=LATENIGHT", 0) == 1 &&
            features.getOrDefault("dayType=NORMAL_WEEKDAY", 0) == 0 &&
            features.getOrDefault("zone=217", 0) == 0 &&
            features.getOrDefault("city=Mumbai", 0) == 1) {
            return new PredictionResult(1, 0.839, 9, 230, 193, 37);
        }

        // Rule 10: NEGATIVE (57.4% confidence, 141 samples)
        if (features.getOrDefault("pickUpHourOfDay=VERYLATE", 0) == 1 &&
            features.getOrDefault("city=Delhi NCR", 0) == 1 &&
            features.getOrDefault("sla=Immediate", 0) == 0 &&
            features.getOrDefault("zone=346", 0) == 0 &&
            features.getOrDefault("zone=360", 0) == 0 &&
            features.getOrDefault("zone=75", 0) == 0) {
            return new PredictionResult(0, 0.574, 10, 141, 60, 81);
        }

        // Rule 11: POSITIVE (75.3% confidence, 93 samples)
        if (features.getOrDefault("pickUpHourOfDay=VERYLATE", 0) == 1 &&
            features.getOrDefault("city=Delhi NCR", 0) == 0 &&
            features.getOrDefault("dayType=WEEKEND", 0) == 0 &&
            features.getOrDefault("city=Pune", 0) == 0 &&
            features.getOrDefault("zone=399", 0) == 0 &&
            features.getOrDefault("city=Hyderabad", 0) == 1) {
            return new PredictionResult(1, 0.753, 11, 93, 70, 23);
        }

        // Rule 12: POSITIVE (92.8% confidence, 83 samples)
        if (features.getOrDefault("pickUpHourOfDay=VERYLATE", 0) == 1 &&
            features.getOrDefault("city=Delhi NCR", 0) == 0 &&
            features.getOrDefault("dayType=WEEKEND", 0) == 1 &&
            features.getOrDefault("zone=399", 0) == 0 &&
            features.getOrDefault("city=Chennai", 0) == 0 &&
            features.getOrDefault("zone=216", 0) == 1) {
            return new PredictionResult(1, 0.928, 12, 83, 77, 6);
        }

        // Rule 13: POSITIVE (96.9% confidence, 64 samples)
        if (features.getOrDefault("pickUpHourOfDay=VERYLATE", 0) == 1 &&
            features.getOrDefault("city=Delhi NCR", 0) == 0 &&
            features.getOrDefault("dayType=WEEKEND", 0) == 1 &&
            features.getOrDefault("zone=399", 0) == 0 &&
            features.getOrDefault("city=Chennai", 0) == 1 &&
            features.getOrDefault("zone=482", 0) == 0) {
            return new PredictionResult(1, 0.969, 13, 64, 62, 2);
        }

        // Rule 14: POSITIVE (94.6% confidence, 56 samples)
        if (features.getOrDefault("pickUpHourOfDay=VERYLATE", 0) == 0 &&
            features.getOrDefault("zone_demand_popularity=POPULARITY_INDEX_5", 0) == 1 &&
            features.getOrDefault("pickUpHourOfDay=LATENIGHT", 0) == 0 &&
            features.getOrDefault("city=Pune", 0) == 1 &&
            features.getOrDefault("zone=329", 0) == 0 &&
            features.getOrDefault("booking_type=outstation", 0) == 1) {
            return new PredictionResult(1, 0.946, 14, 56, 53, 3);
        }

        // Rule 15: POSITIVE (52.7% confidence, 55 samples)
        if (features.getOrDefault("pickUpHourOfDay=VERYLATE", 0) == 0 &&
            features.getOrDefault("zone_demand_popularity=POPULARITY_INDEX_5", 0) == 1 &&
            features.getOrDefault("pickUpHourOfDay=LATENIGHT", 0) == 1 &&
            features.getOrDefault("city=Mumbai", 0) == 0 &&
            features.getOrDefault("zone=339", 0) == 0 &&
            features.getOrDefault("dayType=WEEKEND", 0) == 0) {
            return new PredictionResult(1, 0.527, 15, 55, 29, 26);
        }

        // Rule 16: POSITIVE (76.0% confidence, 50 samples)
        if (features.getOrDefault("pickUpHourOfDay=VERYLATE", 0) == 0 &&
            features.getOrDefault("zone_demand_popularity=POPULARITY_INDEX_5", 0) == 1 &&
            features.getOrDefault("pickUpHourOfDay=LATENIGHT", 0) == 1 &&
            features.getOrDefault("city=Mumbai", 0) == 1 &&
            features.getOrDefault("zone=401", 0) == 0 &&
            features.getOrDefault("zone=467", 0) == 0) {
            return new PredictionResult(1, 0.760, 16, 50, 38, 12);
        }

        // Rule 17: POSITIVE (100.0% confidence, 38 samples)
        if (features.getOrDefault("pickUpHourOfDay=VERYLATE", 0) == 0 &&
            features.getOrDefault("zone_demand_popularity=POPULARITY_INDEX_5", 0) == 0 &&
            features.getOrDefault("pickUpHourOfDay=LATENIGHT", 0) == 1 &&
            features.getOrDefault("dayType=NORMAL_WEEKDAY", 0) == 0 &&
            features.getOrDefault("zone=217", 0) == 1 &&
            features.getOrDefault("dayType=FRIDAY", 0) == 0) {
            return new PredictionResult(1, 1.000, 17, 38, 38, 0);
        }

        // Rule 18: POSITIVE (91.7% confidence, 24 samples)
        if (features.getOrDefault("pickUpHourOfDay=VERYLATE", 0) == 0 &&
            features.getOrDefault("zone_demand_popularity=POPULARITY_INDEX_5", 0) == 0 &&
            features.getOrDefault("pickUpHourOfDay=LATENIGHT", 0) == 1 &&
            features.getOrDefault("dayType=NORMAL_WEEKDAY", 0) == 0 &&
            features.getOrDefault("zone=217", 0) == 1 &&
            features.getOrDefault("dayType=FRIDAY", 0) == 1) {
            return new PredictionResult(1, 0.917, 18, 24, 22, 2);
        }

        // Rule 19: NEGATIVE (66.7% confidence, 24 samples)
        if (features.getOrDefault("pickUpHourOfDay=VERYLATE", 0) == 0 &&
            features.getOrDefault("zone_demand_popularity=POPULARITY_INDEX_5", 0) == 1 &&
            features.getOrDefault("pickUpHourOfDay=LATENIGHT", 0) == 1 &&
            features.getOrDefault("city=Mumbai", 0) == 0 &&
            features.getOrDefault("zone=339", 0) == 0 &&
            features.getOrDefault("dayType=WEEKEND", 0) == 1) {
            return new PredictionResult(0, 0.667, 19, 24, 8, 16);
        }

        // Rule 20: NEGATIVE (72.2% confidence, 18 samples)
        if (features.getOrDefault("pickUpHourOfDay=VERYLATE", 0) == 0 &&
            features.getOrDefault("zone_demand_popularity=POPULARITY_INDEX_5", 0) == 1 &&
            features.getOrDefault("pickUpHourOfDay=LATENIGHT", 0) == 0 &&
            features.getOrDefault("city=Pune", 0) == 0 &&
            features.getOrDefault("zone=67", 0) == 1) {
            return new PredictionResult(0, 0.722, 20, 18, 5, 13);
        }

        // Rule 21: NEGATIVE (83.3% confidence, 18 samples)
        if (features.getOrDefault("pickUpHourOfDay=VERYLATE", 0) == 1 &&
            features.getOrDefault("city=Delhi NCR", 0) == 0 &&
            features.getOrDefault("dayType=WEEKEND", 0) == 1 &&
            features.getOrDefault("zone=399", 0) == 1) {
            return new PredictionResult(0, 0.833, 21, 18, 3, 15);
        }

        // Rule 22: NEGATIVE (64.3% confidence, 14 samples)
        if (features.getOrDefault("pickUpHourOfDay=VERYLATE", 0) == 1 &&
            features.getOrDefault("city=Delhi NCR", 0) == 0 &&
            features.getOrDefault("dayType=WEEKEND", 0) == 0 &&
            features.getOrDefault("city=Pune", 0) == 1) {
            return new PredictionResult(0, 0.643, 22, 14, 5, 9);
        }

        // Rule 23: NEGATIVE (76.9% confidence, 13 samples)
        if (features.getOrDefault("pickUpHourOfDay=VERYLATE", 0) == 0 &&
            features.getOrDefault("zone_demand_popularity=POPULARITY_INDEX_5", 0) == 1 &&
            features.getOrDefault("pickUpHourOfDay=LATENIGHT", 0) == 0 &&
            features.getOrDefault("city=Pune", 0) == 1 &&
            features.getOrDefault("zone=329", 0) == 1) {
            return new PredictionResult(0, 0.769, 23, 13, 3, 10);
        }

        // Rule 24: NEGATIVE (90.9% confidence, 11 samples)
        if (features.getOrDefault("pickUpHourOfDay=VERYLATE", 0) == 1 &&
            features.getOrDefault("city=Delhi NCR", 0) == 1 &&
            features.getOrDefault("sla=Immediate", 0) == 0 &&
            features.getOrDefault("zone=346", 0) == 0 &&
            features.getOrDefault("zone=360", 0) == 0 &&
            features.getOrDefault("zone=75", 0) == 1) {
            return new PredictionResult(0, 0.909, 24, 11, 1, 10);
        }

        // Rule 25: NEGATIVE (87.5% confidence, 8 samples)
        if (features.getOrDefault("pickUpHourOfDay=VERYLATE", 0) == 0 &&
            features.getOrDefault("zone_demand_popularity=POPULARITY_INDEX_5", 0) == 0 &&
            features.getOrDefault("pickUpHourOfDay=LATENIGHT", 0) == 1 &&
            features.getOrDefault("dayType=NORMAL_WEEKDAY", 0) == 1 &&
            features.getOrDefault("zone=500", 0) == 1) {
            return new PredictionResult(0, 0.875, 25, 8, 1, 7);
        }

        // Rule 26: NEGATIVE (71.4% confidence, 7 samples)
        if (features.getOrDefault("pickUpHourOfDay=VERYLATE", 0) == 1 &&
            features.getOrDefault("city=Delhi NCR", 0) == 0 &&
            features.getOrDefault("dayType=WEEKEND", 0) == 0 &&
            features.getOrDefault("city=Pune", 0) == 0 &&
            features.getOrDefault("zone=399", 0) == 1) {
            return new PredictionResult(0, 0.714, 26, 7, 2, 5);
        }

        // Rule 27: POSITIVE (100.0% confidence, 7 samples)
        if (features.getOrDefault("pickUpHourOfDay=VERYLATE", 0) == 1 &&
            features.getOrDefault("city=Delhi NCR", 0) == 1 &&
            features.getOrDefault("sla=Immediate", 0) == 1) {
            return new PredictionResult(1, 1.000, 27, 7, 7, 0);
        }

        // Rule 28: POSITIVE (100.0% confidence, 6 samples)
        if (features.getOrDefault("pickUpHourOfDay=VERYLATE", 0) == 0 &&
            features.getOrDefault("zone_demand_popularity=POPULARITY_INDEX_5", 0) == 1 &&
            features.getOrDefault("pickUpHourOfDay=LATENIGHT", 0) == 1 &&
            features.getOrDefault("city=Mumbai", 0) == 0 &&
            features.getOrDefault("zone=339", 0) == 1) {
            return new PredictionResult(1, 1.000, 28, 6, 6, 0);
        }

        // Rule 29: POSITIVE (100.0% confidence, 5 samples)
        if (features.getOrDefault("pickUpHourOfDay=VERYLATE", 0) == 1 &&
            features.getOrDefault("city=Delhi NCR", 0) == 1 &&
            features.getOrDefault("sla=Immediate", 0) == 0 &&
            features.getOrDefault("zone=346", 0) == 1) {
            return new PredictionResult(1, 1.000, 29, 5, 5, 0);
        }

        // Rule 30: NEGATIVE (100.0% confidence, 4 samples)
        if (features.getOrDefault("pickUpHourOfDay=VERYLATE", 0) == 0 &&
            features.getOrDefault("zone_demand_popularity=POPULARITY_INDEX_5", 0) == 0 &&
            features.getOrDefault("pickUpHourOfDay=LATENIGHT", 0) == 1 &&
            features.getOrDefault("dayType=NORMAL_WEEKDAY", 0) == 1 &&
            features.getOrDefault("zone=500", 0) == 0 &&
            features.getOrDefault("zone=75", 0) == 1) {
            return new PredictionResult(0, 1.000, 30, 4, 0, 4);
        }

        // Rule 31: POSITIVE (100.0% confidence, 4 samples)
        if (features.getOrDefault("pickUpHourOfDay=VERYLATE", 0) == 1 &&
            features.getOrDefault("city=Delhi NCR", 0) == 1 &&
            features.getOrDefault("sla=Immediate", 0) == 0 &&
            features.getOrDefault("zone=346", 0) == 0 &&
            features.getOrDefault("zone=360", 0) == 1) {
            return new PredictionResult(1, 1.000, 31, 4, 4, 0);
        }

        // Rule 32: NEGATIVE (100.0% confidence, 2 samples)
        if (features.getOrDefault("pickUpHourOfDay=VERYLATE", 0) == 0 &&
            features.getOrDefault("zone_demand_popularity=POPULARITY_INDEX_5", 0) == 1 &&
            features.getOrDefault("pickUpHourOfDay=LATENIGHT", 0) == 1 &&
            features.getOrDefault("city=Mumbai", 0) == 1 &&
            features.getOrDefault("zone=401", 0) == 0 &&
            features.getOrDefault("zone=467", 0) == 1) {
            return new PredictionResult(0, 1.000, 32, 2, 0, 2);
        }

        // Rule 33: NEGATIVE (100.0% confidence, 2 samples)
        if (features.getOrDefault("pickUpHourOfDay=VERYLATE", 0) == 0 &&
            features.getOrDefault("zone_demand_popularity=POPULARITY_INDEX_5", 0) == 1 &&
            features.getOrDefault("pickUpHourOfDay=LATENIGHT", 0) == 1 &&
            features.getOrDefault("city=Mumbai", 0) == 1 &&
            features.getOrDefault("zone=401", 0) == 1) {
            return new PredictionResult(0, 1.000, 33, 2, 0, 2);
        }

        // Rule 34: POSITIVE (50.0% confidence, 2 samples)
        if (features.getOrDefault("pickUpHourOfDay=VERYLATE", 0) == 1 &&
            features.getOrDefault("city=Delhi NCR", 0) == 0 &&
            features.getOrDefault("dayType=WEEKEND", 0) == 1 &&
            features.getOrDefault("zone=399", 0) == 0 &&
            features.getOrDefault("city=Chennai", 0) == 1 &&
            features.getOrDefault("zone=482", 0) == 1) {
            return new PredictionResult(1, 0.500, 34, 2, 1, 1);
        }

        // Default fallback
        return new PredictionResult(0, 0.500, -1, 0, 0, 0);
    }

    /**
     * Classify multiple samples
     * @param featuresList List of feature maps
     * @return List of prediction results
     */
    public static List<PredictionResult> predictBatch(List<Map<String, Integer>> featuresList) {
        return featuresList.stream()
                          .map(CartOlapDecisionRules::predict)
                          .toList();
    }

    // Example usage
    public static void main(String[] args) {
        Map<String, Integer> sampleFeatures = Map.of(
            "source=B2B Portal", 0,
            "source=Phone", 1,
            "source=android", 0
        );
        
        var result = predict(sampleFeatures);
        System.out.println("Prediction: " + result.prediction() + ", Confidence: " + result.confidence());
        System.out.println("Total rules in model: 34");
    }
}