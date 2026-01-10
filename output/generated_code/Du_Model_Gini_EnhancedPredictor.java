/*
 * Auto-generated Decision Tree Prediction Code
 * Generated from: du_model_gini_enhanced.json
 * Generated on: 2026-01-10 13:54:03
 */

import java.util.HashMap;
import java.util.Map;
import java.util.List;
import java.util.ArrayList;

public class Du_Model_Gini_EnhancedPredictor {

    public static class PredictionResult {
        public int prediction;
        public String predictionLabel;
        public double confidence;
        public int samples;
        public int ruleIndex;

        public PredictionResult(int prediction, String predictionLabel, double confidence, int samples, int ruleIndex) {
            this.prediction = prediction;
            this.predictionLabel = predictionLabel;
            this.confidence = confidence;
            this.samples = samples;
            this.ruleIndex = ruleIndex;
        }
    }

    public static PredictionResult predictDUQuality(Map<String, Object> features) {
        if (getFeatureValue(features, "pickUpHourOfDay=VERYLATE") == 0 &&
            getFeatureValue(features, "zone_demand_popularity=POPULARITY_INDEX_5") == 0 &&
            getFeatureValue(features, "pickUpHourOfDay=LATENIGHT") == 0 &&
            getFeatureValue(features, "zone=221") == 0 &&
            getFeatureValue(features, "zone=194") == 0 &&
            getFeatureValue(features, "sla=Immediate") == 0) {
            return new PredictionResult(1, "Good_DU", 0.9035, 12794, 0);
        } else if (getFeatureValue(features, "pickUpHourOfDay=VERYLATE") == 0 &&
            getFeatureValue(features, "zone_demand_popularity=POPULARITY_INDEX_5") == 1 &&
            getFeatureValue(features, "pickUpHourOfDay=LATENIGHT") == 0 &&
            getFeatureValue(features, "city=Pune") == 0 &&
            getFeatureValue(features, "city=Mumbai") == 0 &&
            getFeatureValue(features, "city=Hyderabad") == 0) {
            return new PredictionResult(1, "Good_DU", 0.8905, 1397, 1);
        } else if (getFeatureValue(features, "pickUpHourOfDay=VERYLATE") == 1 &&
            getFeatureValue(features, "city=Delhi NCR") == 0 &&
            getFeatureValue(features, "dayType=WEEKEND") == 1 &&
            getFeatureValue(features, "city=Chennai") == 0 &&
            getFeatureValue(features, "zone_demand_popularity=POPULARITY_INDEX_4") == 0 &&
            getFeatureValue(features, "zone=216") == 0) {
            return new PredictionResult(1, "Good_DU", 0.7440, 996, 2);
        } else if (getFeatureValue(features, "pickUpHourOfDay=VERYLATE") == 0 &&
            getFeatureValue(features, "zone_demand_popularity=POPULARITY_INDEX_5") == 0 &&
            getFeatureValue(features, "pickUpHourOfDay=LATENIGHT") == 0 &&
            getFeatureValue(features, "zone=221") == 0 &&
            getFeatureValue(features, "zone=194") == 0 &&
            getFeatureValue(features, "sla=Immediate") == 1) {
            return new PredictionResult(1, "Good_DU", 0.9900, 697, 3);
        } else if (getFeatureValue(features, "pickUpHourOfDay=VERYLATE") == 0 &&
            getFeatureValue(features, "zone_demand_popularity=POPULARITY_INDEX_5") == 0 &&
            getFeatureValue(features, "pickUpHourOfDay=LATENIGHT") == 1 &&
            getFeatureValue(features, "dayType=NORMAL_WEEKDAY") == 0 &&
            getFeatureValue(features, "zone=217") == 0 &&
            getFeatureValue(features, "city=Mumbai") == 0) {
            return new PredictionResult(1, "Good_DU", 0.7205, 644, 4);
        } else if (getFeatureValue(features, "pickUpHourOfDay=VERYLATE") == 0 &&
            getFeatureValue(features, "zone_demand_popularity=POPULARITY_INDEX_5") == 1 &&
            getFeatureValue(features, "pickUpHourOfDay=LATENIGHT") == 0 &&
            getFeatureValue(features, "city=Pune") == 0 &&
            getFeatureValue(features, "city=Mumbai") == 1 &&
            getFeatureValue(features, "booking_type=round_trip") == 0) {
            return new PredictionResult(1, "Good_DU", 0.8212, 397, 5);
        } else if (getFeatureValue(features, "pickUpHourOfDay=VERYLATE") == 1 &&
            getFeatureValue(features, "city=Delhi NCR") == 0 &&
            getFeatureValue(features, "dayType=WEEKEND") == 0 &&
            getFeatureValue(features, "zone_demand_popularity=POPULARITY_INDEX_5") == 0 &&
            getFeatureValue(features, "city=Hyderabad") == 0 &&
            getFeatureValue(features, "zone_demand_popularity=POPULARITY_INDEX_1") == 0) {
            return new PredictionResult(1, "Good_DU", 0.8861, 395, 6);
        } else if (getFeatureValue(features, "pickUpHourOfDay=VERYLATE") == 1 &&
            getFeatureValue(features, "city=Delhi NCR") == 0 &&
            getFeatureValue(features, "dayType=WEEKEND") == 0 &&
            getFeatureValue(features, "zone_demand_popularity=POPULARITY_INDEX_5") == 0 &&
            getFeatureValue(features, "city=Hyderabad") == 0 &&
            getFeatureValue(features, "zone_demand_popularity=POPULARITY_INDEX_1") == 1) {
            return new PredictionResult(1, "Good_DU", 0.9540, 326, 7);
        } else if (getFeatureValue(features, "pickUpHourOfDay=VERYLATE") == 0 &&
            getFeatureValue(features, "zone_demand_popularity=POPULARITY_INDEX_5") == 0 &&
            getFeatureValue(features, "pickUpHourOfDay=LATENIGHT") == 1 &&
            getFeatureValue(features, "dayType=NORMAL_WEEKDAY") == 1 &&
            getFeatureValue(features, "zone_demand_popularity=POPULARITY_INDEX_1") == 0 &&
            getFeatureValue(features, "city=Mumbai") == 0) {
            return new PredictionResult(1, "Good_DU", 0.8193, 249, 8);
        } else if (getFeatureValue(features, "pickUpHourOfDay=VERYLATE") == 0 &&
            getFeatureValue(features, "zone_demand_popularity=POPULARITY_INDEX_5") == 0 &&
            getFeatureValue(features, "pickUpHourOfDay=LATENIGHT") == 1 &&
            getFeatureValue(features, "dayType=NORMAL_WEEKDAY") == 1 &&
            getFeatureValue(features, "zone_demand_popularity=POPULARITY_INDEX_1") == 1 &&
            getFeatureValue(features, "zone=219") == 0) {
            return new PredictionResult(1, "Good_DU", 0.9419, 241, 9);
        } else if (getFeatureValue(features, "pickUpHourOfDay=VERYLATE") == 0 &&
            getFeatureValue(features, "zone_demand_popularity=POPULARITY_INDEX_5") == 0 &&
            getFeatureValue(features, "pickUpHourOfDay=LATENIGHT") == 1 &&
            getFeatureValue(features, "dayType=NORMAL_WEEKDAY") == 0 &&
            getFeatureValue(features, "zone=217") == 0 &&
            getFeatureValue(features, "city=Mumbai") == 1) {
            return new PredictionResult(1, "Good_DU", 0.8391, 230, 10);
        } else if (getFeatureValue(features, "pickUpHourOfDay=VERYLATE") == 0 &&
            getFeatureValue(features, "zone_demand_popularity=POPULARITY_INDEX_5") == 1 &&
            getFeatureValue(features, "pickUpHourOfDay=LATENIGHT") == 0 &&
            getFeatureValue(features, "city=Pune") == 1 &&
            getFeatureValue(features, "booking_type=outstation") == 0 &&
            getFeatureValue(features, "pickUpHourOfDay=MORNING") == 0) {
            return new PredictionResult(1, "Good_DU", 0.6119, 201, 11);
        } else if (getFeatureValue(features, "pickUpHourOfDay=VERYLATE") == 0 &&
            getFeatureValue(features, "zone_demand_popularity=POPULARITY_INDEX_5") == 1 &&
            getFeatureValue(features, "pickUpHourOfDay=LATENIGHT") == 0 &&
            getFeatureValue(features, "city=Pune") == 0 &&
            getFeatureValue(features, "city=Mumbai") == 1 &&
            getFeatureValue(features, "booking_type=round_trip") == 1) {
            return new PredictionResult(1, "Good_DU", 0.6825, 189, 12);
        } else if (getFeatureValue(features, "pickUpHourOfDay=VERYLATE") == 0 &&
            getFeatureValue(features, "zone_demand_popularity=POPULARITY_INDEX_5") == 0 &&
            getFeatureValue(features, "pickUpHourOfDay=LATENIGHT") == 1 &&
            getFeatureValue(features, "dayType=NORMAL_WEEKDAY") == 1 &&
            getFeatureValue(features, "zone_demand_popularity=POPULARITY_INDEX_1") == 0 &&
            getFeatureValue(features, "city=Mumbai") == 1) {
            return new PredictionResult(1, "Good_DU", 0.9655, 116, 13);
        } else if (getFeatureValue(features, "pickUpHourOfDay=VERYLATE") == 0 &&
            getFeatureValue(features, "zone_demand_popularity=POPULARITY_INDEX_5") == 0 &&
            getFeatureValue(features, "pickUpHourOfDay=LATENIGHT") == 0 &&
            getFeatureValue(features, "zone=221") == 1 &&
            getFeatureValue(features, "booking_type=one_way_trip") == 0 &&
            getFeatureValue(features, "estimated_usage_bins=GT_3_LTE_4_HOURS") == 0) {
            return new PredictionResult(1, "Good_DU", 0.8454, 97, 14);
        } else if (getFeatureValue(features, "pickUpHourOfDay=VERYLATE") == 0 &&
            getFeatureValue(features, "zone_demand_popularity=POPULARITY_INDEX_5") == 0 &&
            getFeatureValue(features, "pickUpHourOfDay=LATENIGHT") == 1 &&
            getFeatureValue(features, "dayType=NORMAL_WEEKDAY") == 1 &&
            getFeatureValue(features, "zone_demand_popularity=POPULARITY_INDEX_1") == 1 &&
            getFeatureValue(features, "zone=219") == 1) {
            return new PredictionResult(1, "Good_DU", 0.9688, 96, 15);
        } else if (getFeatureValue(features, "pickUpHourOfDay=VERYLATE") == 0 &&
            getFeatureValue(features, "zone_demand_popularity=POPULARITY_INDEX_5") == 1 &&
            getFeatureValue(features, "pickUpHourOfDay=LATENIGHT") == 0 &&
            getFeatureValue(features, "city=Pune") == 0 &&
            getFeatureValue(features, "city=Mumbai") == 0 &&
            getFeatureValue(features, "city=Hyderabad") == 1) {
            return new PredictionResult(1, "Good_DU", 0.7174, 92, 16);
        } else if (getFeatureValue(features, "pickUpHourOfDay=VERYLATE") == 0 &&
            getFeatureValue(features, "zone_demand_popularity=POPULARITY_INDEX_5") == 0 &&
            getFeatureValue(features, "pickUpHourOfDay=LATENIGHT") == 0 &&
            getFeatureValue(features, "zone=221") == 1 &&
            getFeatureValue(features, "booking_type=one_way_trip") == 1) {
            return new PredictionResult(1, "Good_DU", 0.6111, 90, 17);
        } else if (getFeatureValue(features, "pickUpHourOfDay=VERYLATE") == 0 &&
            getFeatureValue(features, "zone_demand_popularity=POPULARITY_INDEX_5") == 1 &&
            getFeatureValue(features, "pickUpHourOfDay=LATENIGHT") == 0 &&
            getFeatureValue(features, "city=Pune") == 1 &&
            getFeatureValue(features, "booking_type=outstation") == 0 &&
            getFeatureValue(features, "pickUpHourOfDay=MORNING") == 1) {
            return new PredictionResult(1, "Good_DU", 0.8111, 90, 18);
        } else if (getFeatureValue(features, "pickUpHourOfDay=VERYLATE") == 1 &&
            getFeatureValue(features, "city=Delhi NCR") == 0 &&
            getFeatureValue(features, "dayType=WEEKEND") == 0 &&
            getFeatureValue(features, "zone_demand_popularity=POPULARITY_INDEX_5") == 0 &&
            getFeatureValue(features, "city=Hyderabad") == 1) {
            return new PredictionResult(1, "Good_DU", 0.7444, 90, 19);
        } else if (getFeatureValue(features, "pickUpHourOfDay=VERYLATE") == 0 &&
            getFeatureValue(features, "zone_demand_popularity=POPULARITY_INDEX_5") == 1 &&
            getFeatureValue(features, "pickUpHourOfDay=LATENIGHT") == 1 &&
            getFeatureValue(features, "city=Mumbai") == 0) {
            return new PredictionResult(1, "Good_DU", 0.5059, 85, 20);
        } else if (getFeatureValue(features, "pickUpHourOfDay=VERYLATE") == 1 &&
            getFeatureValue(features, "city=Delhi NCR") == 0 &&
            getFeatureValue(features, "dayType=WEEKEND") == 1 &&
            getFeatureValue(features, "city=Chennai") == 0 &&
            getFeatureValue(features, "zone_demand_popularity=POPULARITY_INDEX_4") == 0 &&
            getFeatureValue(features, "zone=216") == 1) {
            return new PredictionResult(1, "Good_DU", 0.9277, 83, 21);
        } else if (getFeatureValue(features, "pickUpHourOfDay=VERYLATE") == 1 &&
            getFeatureValue(features, "city=Delhi NCR") == 0 &&
            getFeatureValue(features, "dayType=WEEKEND") == 1 &&
            getFeatureValue(features, "city=Chennai") == 0 &&
            getFeatureValue(features, "zone_demand_popularity=POPULARITY_INDEX_4") == 1 &&
            getFeatureValue(features, "city=Mumbai") == 1) {
            return new PredictionResult(1, "Good_DU", 0.5181, 83, 22);
        } else if (getFeatureValue(features, "pickUpHourOfDay=VERYLATE") == 0 &&
            getFeatureValue(features, "zone_demand_popularity=POPULARITY_INDEX_5") == 0 &&
            getFeatureValue(features, "pickUpHourOfDay=LATENIGHT") == 0 &&
            getFeatureValue(features, "zone=221") == 0 &&
            getFeatureValue(features, "zone=194") == 1) {
            return new PredictionResult(1, "Good_DU", 0.6087, 69, 23);
        } else if (getFeatureValue(features, "pickUpHourOfDay=VERYLATE") == 1 &&
            getFeatureValue(features, "city=Delhi NCR") == 0 &&
            getFeatureValue(features, "dayType=WEEKEND") == 1 &&
            getFeatureValue(features, "city=Chennai") == 0 &&
            getFeatureValue(features, "zone_demand_popularity=POPULARITY_INDEX_4") == 1 &&
            getFeatureValue(features, "city=Mumbai") == 0) {
            return new PredictionResult(1, "Good_DU", 0.6061, 66, 24);
        } else if (getFeatureValue(features, "pickUpHourOfDay=VERYLATE") == 1 &&
            getFeatureValue(features, "city=Delhi NCR") == 0 &&
            getFeatureValue(features, "dayType=WEEKEND") == 1 &&
            getFeatureValue(features, "city=Chennai") == 1) {
            return new PredictionResult(1, "Good_DU", 0.9545, 66, 25);
        } else if (getFeatureValue(features, "pickUpHourOfDay=VERYLATE") == 0 &&
            getFeatureValue(features, "zone_demand_popularity=POPULARITY_INDEX_5") == 0 &&
            getFeatureValue(features, "pickUpHourOfDay=LATENIGHT") == 1 &&
            getFeatureValue(features, "dayType=NORMAL_WEEKDAY") == 0 &&
            getFeatureValue(features, "zone=217") == 1) {
            return new PredictionResult(1, "Good_DU", 0.9677, 62, 26);
        } else if (getFeatureValue(features, "pickUpHourOfDay=VERYLATE") == 0 &&
            getFeatureValue(features, "zone_demand_popularity=POPULARITY_INDEX_5") == 1 &&
            getFeatureValue(features, "pickUpHourOfDay=LATENIGHT") == 0 &&
            getFeatureValue(features, "city=Pune") == 1 &&
            getFeatureValue(features, "booking_type=outstation") == 1) {
            return new PredictionResult(1, "Good_DU", 0.9032, 62, 27);
        } else if (getFeatureValue(features, "pickUpHourOfDay=VERYLATE") == 0 &&
            getFeatureValue(features, "zone_demand_popularity=POPULARITY_INDEX_5") == 0 &&
            getFeatureValue(features, "pickUpHourOfDay=LATENIGHT") == 0 &&
            getFeatureValue(features, "zone=221") == 1 &&
            getFeatureValue(features, "booking_type=one_way_trip") == 0 &&
            getFeatureValue(features, "estimated_usage_bins=GT_3_LTE_4_HOURS") == 1) {
            return new PredictionResult(1, "Good_DU", 0.7705, 61, 28);
        } else if (getFeatureValue(features, "pickUpHourOfDay=VERYLATE") == 1 &&
            getFeatureValue(features, "city=Delhi NCR") == 1 &&
            getFeatureValue(features, "zone_demand_popularity=POPULARITY_INDEX_2") == 0 &&
            getFeatureValue(features, "zone_demand_popularity=POPULARITY_INDEX_4") == 0) {
            return new PredictionResult(0, "Bad_DU", 0.6333, 60, 29);
        } else if (getFeatureValue(features, "pickUpHourOfDay=VERYLATE") == 1 &&
            getFeatureValue(features, "city=Delhi NCR") == 0 &&
            getFeatureValue(features, "dayType=WEEKEND") == 0 &&
            getFeatureValue(features, "zone_demand_popularity=POPULARITY_INDEX_5") == 1) {
            return new PredictionResult(1, "Good_DU", 0.6842, 57, 30);
        } else if (getFeatureValue(features, "pickUpHourOfDay=VERYLATE") == 1 &&
            getFeatureValue(features, "city=Delhi NCR") == 1 &&
            getFeatureValue(features, "zone_demand_popularity=POPULARITY_INDEX_2") == 1) {
            return new PredictionResult(1, "Good_DU", 0.5263, 57, 31);
        } else if (getFeatureValue(features, "pickUpHourOfDay=VERYLATE") == 0 &&
            getFeatureValue(features, "zone_demand_popularity=POPULARITY_INDEX_5") == 1 &&
            getFeatureValue(features, "pickUpHourOfDay=LATENIGHT") == 1 &&
            getFeatureValue(features, "city=Mumbai") == 1) {
            return new PredictionResult(1, "Good_DU", 0.7037, 54, 32);
        } else if (getFeatureValue(features, "pickUpHourOfDay=VERYLATE") == 1 &&
            getFeatureValue(features, "city=Delhi NCR") == 1 &&
            getFeatureValue(features, "zone_demand_popularity=POPULARITY_INDEX_2") == 0 &&
            getFeatureValue(features, "zone_demand_popularity=POPULARITY_INDEX_4") == 1) {
            return new PredictionResult(0, "Bad_DU", 0.5098, 51, 33);
        } else {
            // Default case
            return new PredictionResult(1, "Good_DU", 0.872, 0, -1);
        }
    }

    private static int getFeatureValue(Map<String, Object> features, String featureName) {
        Object value = features.get(featureName);
        if (value instanceof Number) {
            return ((Number) value).intValue();
        }
        return 0;
    }

    public static void main(String[] args) {
        Map<String, Object> sampleFeatures = new HashMap<>();
        sampleFeatures.put("pickUpHourOfDay=VERYLATE", 0);
        sampleFeatures.put("zone_demand_popularity=POPULARITY_INDEX_5", 0);
        sampleFeatures.put("pickUpHourOfDay=LATENIGHT", 0);
        sampleFeatures.put("zone=221", 0);
        sampleFeatures.put("zone=194", 0);
        sampleFeatures.put("sla=Immediate", 0);

        PredictionResult result = predictDUQuality(sampleFeatures);
        System.out.println("Prediction: " + result.predictionLabel);
        System.out.println("Confidence: " + result.confidence);
        System.out.println("Samples: " + result.samples);
    }
}
