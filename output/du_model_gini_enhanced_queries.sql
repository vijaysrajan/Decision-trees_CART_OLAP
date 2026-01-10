-- Decision Tree Rules as SQL Queries
-- Generated from: output/du_model_gini_enhanced.json
-- Total rules: 34

-- Rule 0: AND NONE(pickUpHourOfDay=VERYLATE, zone_demand_popularity=POPULARITY_INDEX_5, pickUpHourOfDay=LATENIGHT, zone=221, zone=194, sla=Immediate)
-- Prediction: Good_DU (confidence: 0.903)
-- Samples: 12794
SELECT 'Good_DU' as prediction, 0.9035 as confidence
FROM dataset WHERE ([pickUpHourOfDay_VERYLATE] = 0 OR [pickUpHourOfDay_VERYLATE] IS NULL) AND ([zone_demand_popularity_POPULARITY_INDEX_5] = 0 OR [zone_demand_popularity_POPULARITY_INDEX_5] IS NULL) AND ([pickUpHourOfDay_LATENIGHT] = 0 OR [pickUpHourOfDay_LATENIGHT] IS NULL) AND ([zone_221] = 0 OR [zone_221] IS NULL) AND ([zone_194] = 0 OR [zone_194] IS NULL) AND ([sla_Immediate] = 0 OR [sla_Immediate] IS NULL);

-- Rule 1: WHEN zone_demand_popularity=POPULARITY_INDEX_5 AND NONE(pickUpHourOfDay=VERYLATE, pickUpHourOfDay=LATENIGHT, city=Pune, city=Mumbai, city=Hyderabad)
-- Prediction: Good_DU (confidence: 0.890)
-- Samples: 1397
SELECT 'Good_DU' as prediction, 0.8905 as confidence
FROM dataset WHERE ([pickUpHourOfDay_VERYLATE] = 0 OR [pickUpHourOfDay_VERYLATE] IS NULL) AND [zone_demand_popularity_POPULARITY_INDEX_5] = 1 AND ([pickUpHourOfDay_LATENIGHT] = 0 OR [pickUpHourOfDay_LATENIGHT] IS NULL) AND ([city_Pune] = 0 OR [city_Pune] IS NULL) AND ([city_Mumbai] = 0 OR [city_Mumbai] IS NULL) AND ([city_Hyderabad] = 0 OR [city_Hyderabad] IS NULL);

-- Rule 2: WHEN ALL(pickUpHourOfDay=VERYLATE, dayType=WEEKEND) AND NONE(city=Delhi NCR, city=Chennai, zone_demand_popularity=POPULARITY_INDEX_4, zone=216)
-- Prediction: Good_DU (confidence: 0.744)
-- Samples: 996
SELECT 'Good_DU' as prediction, 0.7440 as confidence
FROM dataset WHERE [pickUpHourOfDay_VERYLATE] = 1 AND ([city_Delhi_NCR] = 0 OR [city_Delhi_NCR] IS NULL) AND [dayType_WEEKEND] = 1 AND ([city_Chennai] = 0 OR [city_Chennai] IS NULL) AND ([zone_demand_popularity_POPULARITY_INDEX_4] = 0 OR [zone_demand_popularity_POPULARITY_INDEX_4] IS NULL) AND ([zone_216] = 0 OR [zone_216] IS NULL);

-- Rule 3: WHEN sla=Immediate AND NONE(pickUpHourOfDay=VERYLATE, zone_demand_popularity=POPULARITY_INDEX_5, pickUpHourOfDay=LATENIGHT, zone=221, zone=194)
-- Prediction: Good_DU (confidence: 0.990)
-- Samples: 697
SELECT 'Good_DU' as prediction, 0.9900 as confidence
FROM dataset WHERE ([pickUpHourOfDay_VERYLATE] = 0 OR [pickUpHourOfDay_VERYLATE] IS NULL) AND ([zone_demand_popularity_POPULARITY_INDEX_5] = 0 OR [zone_demand_popularity_POPULARITY_INDEX_5] IS NULL) AND ([pickUpHourOfDay_LATENIGHT] = 0 OR [pickUpHourOfDay_LATENIGHT] IS NULL) AND ([zone_221] = 0 OR [zone_221] IS NULL) AND ([zone_194] = 0 OR [zone_194] IS NULL) AND [sla_Immediate] = 1;

-- Rule 4: WHEN pickUpHourOfDay=LATENIGHT AND NONE(pickUpHourOfDay=VERYLATE, zone_demand_popularity=POPULARITY_INDEX_5, dayType=NORMAL_WEEKDAY, zone=217, city=Mumbai)
-- Prediction: Good_DU (confidence: 0.721)
-- Samples: 644
SELECT 'Good_DU' as prediction, 0.7205 as confidence
FROM dataset WHERE ([pickUpHourOfDay_VERYLATE] = 0 OR [pickUpHourOfDay_VERYLATE] IS NULL) AND ([zone_demand_popularity_POPULARITY_INDEX_5] = 0 OR [zone_demand_popularity_POPULARITY_INDEX_5] IS NULL) AND [pickUpHourOfDay_LATENIGHT] = 1 AND ([dayType_NORMAL_WEEKDAY] = 0 OR [dayType_NORMAL_WEEKDAY] IS NULL) AND ([zone_217] = 0 OR [zone_217] IS NULL) AND ([city_Mumbai] = 0 OR [city_Mumbai] IS NULL);

-- Rule 5: WHEN ALL(zone_demand_popularity=POPULARITY_INDEX_5, city=Mumbai) AND NONE(pickUpHourOfDay=VERYLATE, pickUpHourOfDay=LATENIGHT, city=Pune, booking_type=round_trip)
-- Prediction: Good_DU (confidence: 0.821)
-- Samples: 397
SELECT 'Good_DU' as prediction, 0.8212 as confidence
FROM dataset WHERE ([pickUpHourOfDay_VERYLATE] = 0 OR [pickUpHourOfDay_VERYLATE] IS NULL) AND [zone_demand_popularity_POPULARITY_INDEX_5] = 1 AND ([pickUpHourOfDay_LATENIGHT] = 0 OR [pickUpHourOfDay_LATENIGHT] IS NULL) AND ([city_Pune] = 0 OR [city_Pune] IS NULL) AND [city_Mumbai] = 1 AND ([booking_type_round_trip] = 0 OR [booking_type_round_trip] IS NULL);

-- Rule 6: WHEN pickUpHourOfDay=VERYLATE AND NONE(city=Delhi NCR, dayType=WEEKEND, zone_demand_popularity=POPULARITY_INDEX_5, city=Hyderabad, zone_demand_popularity=POPULARITY_INDEX_1)
-- Prediction: Good_DU (confidence: 0.886)
-- Samples: 395
SELECT 'Good_DU' as prediction, 0.8861 as confidence
FROM dataset WHERE [pickUpHourOfDay_VERYLATE] = 1 AND ([city_Delhi_NCR] = 0 OR [city_Delhi_NCR] IS NULL) AND ([dayType_WEEKEND] = 0 OR [dayType_WEEKEND] IS NULL) AND ([zone_demand_popularity_POPULARITY_INDEX_5] = 0 OR [zone_demand_popularity_POPULARITY_INDEX_5] IS NULL) AND ([city_Hyderabad] = 0 OR [city_Hyderabad] IS NULL) AND ([zone_demand_popularity_POPULARITY_INDEX_1] = 0 OR [zone_demand_popularity_POPULARITY_INDEX_1] IS NULL);

-- Rule 7: WHEN ALL(pickUpHourOfDay=VERYLATE, zone_demand_popularity=POPULARITY_INDEX_1) AND NONE(city=Delhi NCR, dayType=WEEKEND, zone_demand_popularity=POPULARITY_INDEX_5, city=Hyderabad)
-- Prediction: Good_DU (confidence: 0.954)
-- Samples: 326
SELECT 'Good_DU' as prediction, 0.9540 as confidence
FROM dataset WHERE [pickUpHourOfDay_VERYLATE] = 1 AND ([city_Delhi_NCR] = 0 OR [city_Delhi_NCR] IS NULL) AND ([dayType_WEEKEND] = 0 OR [dayType_WEEKEND] IS NULL) AND ([zone_demand_popularity_POPULARITY_INDEX_5] = 0 OR [zone_demand_popularity_POPULARITY_INDEX_5] IS NULL) AND ([city_Hyderabad] = 0 OR [city_Hyderabad] IS NULL) AND [zone_demand_popularity_POPULARITY_INDEX_1] = 1;

-- Rule 8: WHEN ALL(pickUpHourOfDay=LATENIGHT, dayType=NORMAL_WEEKDAY) AND NONE(pickUpHourOfDay=VERYLATE, zone_demand_popularity=POPULARITY_INDEX_5, zone_demand_popularity=POPULARITY_INDEX_1, city=Mumbai)
-- Prediction: Good_DU (confidence: 0.819)
-- Samples: 249
SELECT 'Good_DU' as prediction, 0.8193 as confidence
FROM dataset WHERE ([pickUpHourOfDay_VERYLATE] = 0 OR [pickUpHourOfDay_VERYLATE] IS NULL) AND ([zone_demand_popularity_POPULARITY_INDEX_5] = 0 OR [zone_demand_popularity_POPULARITY_INDEX_5] IS NULL) AND [pickUpHourOfDay_LATENIGHT] = 1 AND [dayType_NORMAL_WEEKDAY] = 1 AND ([zone_demand_popularity_POPULARITY_INDEX_1] = 0 OR [zone_demand_popularity_POPULARITY_INDEX_1] IS NULL) AND ([city_Mumbai] = 0 OR [city_Mumbai] IS NULL);

-- Rule 9: WHEN ALL(pickUpHourOfDay=LATENIGHT, dayType=NORMAL_WEEKDAY, zone_demand_popularity=POPULARITY_INDEX_1) AND NONE(pickUpHourOfDay=VERYLATE, zone_demand_popularity=POPULARITY_INDEX_5, zone=219)
-- Prediction: Good_DU (confidence: 0.942)
-- Samples: 241
SELECT 'Good_DU' as prediction, 0.9419 as confidence
FROM dataset WHERE ([pickUpHourOfDay_VERYLATE] = 0 OR [pickUpHourOfDay_VERYLATE] IS NULL) AND ([zone_demand_popularity_POPULARITY_INDEX_5] = 0 OR [zone_demand_popularity_POPULARITY_INDEX_5] IS NULL) AND [pickUpHourOfDay_LATENIGHT] = 1 AND [dayType_NORMAL_WEEKDAY] = 1 AND [zone_demand_popularity_POPULARITY_INDEX_1] = 1 AND ([zone_219] = 0 OR [zone_219] IS NULL);

-- Rule 10: WHEN ALL(pickUpHourOfDay=LATENIGHT, city=Mumbai) AND NONE(pickUpHourOfDay=VERYLATE, zone_demand_popularity=POPULARITY_INDEX_5, dayType=NORMAL_WEEKDAY, zone=217)
-- Prediction: Good_DU (confidence: 0.839)
-- Samples: 230
SELECT 'Good_DU' as prediction, 0.8391 as confidence
FROM dataset WHERE ([pickUpHourOfDay_VERYLATE] = 0 OR [pickUpHourOfDay_VERYLATE] IS NULL) AND ([zone_demand_popularity_POPULARITY_INDEX_5] = 0 OR [zone_demand_popularity_POPULARITY_INDEX_5] IS NULL) AND [pickUpHourOfDay_LATENIGHT] = 1 AND ([dayType_NORMAL_WEEKDAY] = 0 OR [dayType_NORMAL_WEEKDAY] IS NULL) AND ([zone_217] = 0 OR [zone_217] IS NULL) AND [city_Mumbai] = 1;

-- Rule 11: WHEN ALL(zone_demand_popularity=POPULARITY_INDEX_5, city=Pune) AND NONE(pickUpHourOfDay=VERYLATE, pickUpHourOfDay=LATENIGHT, booking_type=outstation, pickUpHourOfDay=MORNING)
-- Prediction: Good_DU (confidence: 0.612)
-- Samples: 201
SELECT 'Good_DU' as prediction, 0.6119 as confidence
FROM dataset WHERE ([pickUpHourOfDay_VERYLATE] = 0 OR [pickUpHourOfDay_VERYLATE] IS NULL) AND [zone_demand_popularity_POPULARITY_INDEX_5] = 1 AND ([pickUpHourOfDay_LATENIGHT] = 0 OR [pickUpHourOfDay_LATENIGHT] IS NULL) AND [city_Pune] = 1 AND ([booking_type_outstation] = 0 OR [booking_type_outstation] IS NULL) AND ([pickUpHourOfDay_MORNING] = 0 OR [pickUpHourOfDay_MORNING] IS NULL);

-- Rule 12: WHEN ALL(zone_demand_popularity=POPULARITY_INDEX_5, city=Mumbai, booking_type=round_trip) AND NONE(pickUpHourOfDay=VERYLATE, pickUpHourOfDay=LATENIGHT, city=Pune)
-- Prediction: Good_DU (confidence: 0.682)
-- Samples: 189
SELECT 'Good_DU' as prediction, 0.6825 as confidence
FROM dataset WHERE ([pickUpHourOfDay_VERYLATE] = 0 OR [pickUpHourOfDay_VERYLATE] IS NULL) AND [zone_demand_popularity_POPULARITY_INDEX_5] = 1 AND ([pickUpHourOfDay_LATENIGHT] = 0 OR [pickUpHourOfDay_LATENIGHT] IS NULL) AND ([city_Pune] = 0 OR [city_Pune] IS NULL) AND [city_Mumbai] = 1 AND [booking_type_round_trip] = 1;

-- Rule 13: WHEN ALL(pickUpHourOfDay=LATENIGHT, dayType=NORMAL_WEEKDAY, city=Mumbai) AND NONE(pickUpHourOfDay=VERYLATE, zone_demand_popularity=POPULARITY_INDEX_5, zone_demand_popularity=POPULARITY_INDEX_1)
-- Prediction: Good_DU (confidence: 0.966)
-- Samples: 116
SELECT 'Good_DU' as prediction, 0.9655 as confidence
FROM dataset WHERE ([pickUpHourOfDay_VERYLATE] = 0 OR [pickUpHourOfDay_VERYLATE] IS NULL) AND ([zone_demand_popularity_POPULARITY_INDEX_5] = 0 OR [zone_demand_popularity_POPULARITY_INDEX_5] IS NULL) AND [pickUpHourOfDay_LATENIGHT] = 1 AND [dayType_NORMAL_WEEKDAY] = 1 AND ([zone_demand_popularity_POPULARITY_INDEX_1] = 0 OR [zone_demand_popularity_POPULARITY_INDEX_1] IS NULL) AND [city_Mumbai] = 1;

-- Rule 14: WHEN zone=221 AND NONE(pickUpHourOfDay=VERYLATE, zone_demand_popularity=POPULARITY_INDEX_5, pickUpHourOfDay=LATENIGHT, booking_type=one_way_trip, estimated_usage_bins=GT_3_LTE_4_HOURS)
-- Prediction: Good_DU (confidence: 0.845)
-- Samples: 97
SELECT 'Good_DU' as prediction, 0.8454 as confidence
FROM dataset WHERE ([pickUpHourOfDay_VERYLATE] = 0 OR [pickUpHourOfDay_VERYLATE] IS NULL) AND ([zone_demand_popularity_POPULARITY_INDEX_5] = 0 OR [zone_demand_popularity_POPULARITY_INDEX_5] IS NULL) AND ([pickUpHourOfDay_LATENIGHT] = 0 OR [pickUpHourOfDay_LATENIGHT] IS NULL) AND [zone_221] = 1 AND ([booking_type_one_way_trip] = 0 OR [booking_type_one_way_trip] IS NULL) AND ([estimated_usage_bins_GT_3_LTE_4_HOURS] = 0 OR [estimated_usage_bins_GT_3_LTE_4_HOURS] IS NULL);

-- Rule 15: WHEN ALL(pickUpHourOfDay=LATENIGHT, dayType=NORMAL_WEEKDAY, zone_demand_popularity=POPULARITY_INDEX_1, zone=219) AND NONE(pickUpHourOfDay=VERYLATE, zone_demand_popularity=POPULARITY_INDEX_5)
-- Prediction: Good_DU (confidence: 0.969)
-- Samples: 96
SELECT 'Good_DU' as prediction, 0.9688 as confidence
FROM dataset WHERE ([pickUpHourOfDay_VERYLATE] = 0 OR [pickUpHourOfDay_VERYLATE] IS NULL) AND ([zone_demand_popularity_POPULARITY_INDEX_5] = 0 OR [zone_demand_popularity_POPULARITY_INDEX_5] IS NULL) AND [pickUpHourOfDay_LATENIGHT] = 1 AND [dayType_NORMAL_WEEKDAY] = 1 AND [zone_demand_popularity_POPULARITY_INDEX_1] = 1 AND [zone_219] = 1;

-- Rule 16: WHEN ALL(zone_demand_popularity=POPULARITY_INDEX_5, city=Hyderabad) AND NONE(pickUpHourOfDay=VERYLATE, pickUpHourOfDay=LATENIGHT, city=Pune, city=Mumbai)
-- Prediction: Good_DU (confidence: 0.717)
-- Samples: 92
SELECT 'Good_DU' as prediction, 0.7174 as confidence
FROM dataset WHERE ([pickUpHourOfDay_VERYLATE] = 0 OR [pickUpHourOfDay_VERYLATE] IS NULL) AND [zone_demand_popularity_POPULARITY_INDEX_5] = 1 AND ([pickUpHourOfDay_LATENIGHT] = 0 OR [pickUpHourOfDay_LATENIGHT] IS NULL) AND ([city_Pune] = 0 OR [city_Pune] IS NULL) AND ([city_Mumbai] = 0 OR [city_Mumbai] IS NULL) AND [city_Hyderabad] = 1;

-- Rule 17: WHEN ALL(zone=221, booking_type=one_way_trip) AND NONE(pickUpHourOfDay=VERYLATE, zone_demand_popularity=POPULARITY_INDEX_5, pickUpHourOfDay=LATENIGHT)
-- Prediction: Good_DU (confidence: 0.611)
-- Samples: 90
SELECT 'Good_DU' as prediction, 0.6111 as confidence
FROM dataset WHERE ([pickUpHourOfDay_VERYLATE] = 0 OR [pickUpHourOfDay_VERYLATE] IS NULL) AND ([zone_demand_popularity_POPULARITY_INDEX_5] = 0 OR [zone_demand_popularity_POPULARITY_INDEX_5] IS NULL) AND ([pickUpHourOfDay_LATENIGHT] = 0 OR [pickUpHourOfDay_LATENIGHT] IS NULL) AND [zone_221] = 1 AND [booking_type_one_way_trip] = 1;

-- Rule 18: WHEN ALL(zone_demand_popularity=POPULARITY_INDEX_5, city=Pune, pickUpHourOfDay=MORNING) AND NONE(pickUpHourOfDay=VERYLATE, pickUpHourOfDay=LATENIGHT, booking_type=outstation)
-- Prediction: Good_DU (confidence: 0.811)
-- Samples: 90
SELECT 'Good_DU' as prediction, 0.8111 as confidence
FROM dataset WHERE ([pickUpHourOfDay_VERYLATE] = 0 OR [pickUpHourOfDay_VERYLATE] IS NULL) AND [zone_demand_popularity_POPULARITY_INDEX_5] = 1 AND ([pickUpHourOfDay_LATENIGHT] = 0 OR [pickUpHourOfDay_LATENIGHT] IS NULL) AND [city_Pune] = 1 AND ([booking_type_outstation] = 0 OR [booking_type_outstation] IS NULL) AND [pickUpHourOfDay_MORNING] = 1;

-- Rule 19: WHEN ALL(pickUpHourOfDay=VERYLATE, city=Hyderabad) AND NONE(city=Delhi NCR, dayType=WEEKEND, zone_demand_popularity=POPULARITY_INDEX_5)
-- Prediction: Good_DU (confidence: 0.744)
-- Samples: 90
SELECT 'Good_DU' as prediction, 0.7444 as confidence
FROM dataset WHERE [pickUpHourOfDay_VERYLATE] = 1 AND ([city_Delhi_NCR] = 0 OR [city_Delhi_NCR] IS NULL) AND ([dayType_WEEKEND] = 0 OR [dayType_WEEKEND] IS NULL) AND ([zone_demand_popularity_POPULARITY_INDEX_5] = 0 OR [zone_demand_popularity_POPULARITY_INDEX_5] IS NULL) AND [city_Hyderabad] = 1;

-- Rule 20: WHEN ALL(zone_demand_popularity=POPULARITY_INDEX_5, pickUpHourOfDay=LATENIGHT) AND NONE(pickUpHourOfDay=VERYLATE, city=Mumbai)
-- Prediction: Good_DU (confidence: 0.506)
-- Samples: 85
SELECT 'Good_DU' as prediction, 0.5059 as confidence
FROM dataset WHERE ([pickUpHourOfDay_VERYLATE] = 0 OR [pickUpHourOfDay_VERYLATE] IS NULL) AND [zone_demand_popularity_POPULARITY_INDEX_5] = 1 AND [pickUpHourOfDay_LATENIGHT] = 1 AND ([city_Mumbai] = 0 OR [city_Mumbai] IS NULL);

-- Rule 21: WHEN ALL(pickUpHourOfDay=VERYLATE, dayType=WEEKEND, zone=216) AND NONE(city=Delhi NCR, city=Chennai, zone_demand_popularity=POPULARITY_INDEX_4)
-- Prediction: Good_DU (confidence: 0.928)
-- Samples: 83
SELECT 'Good_DU' as prediction, 0.9277 as confidence
FROM dataset WHERE [pickUpHourOfDay_VERYLATE] = 1 AND ([city_Delhi_NCR] = 0 OR [city_Delhi_NCR] IS NULL) AND [dayType_WEEKEND] = 1 AND ([city_Chennai] = 0 OR [city_Chennai] IS NULL) AND ([zone_demand_popularity_POPULARITY_INDEX_4] = 0 OR [zone_demand_popularity_POPULARITY_INDEX_4] IS NULL) AND [zone_216] = 1;

-- Rule 22: WHEN ALL(pickUpHourOfDay=VERYLATE, dayType=WEEKEND, zone_demand_popularity=POPULARITY_INDEX_4, city=Mumbai) AND NONE(city=Delhi NCR, city=Chennai)
-- Prediction: Good_DU (confidence: 0.518)
-- Samples: 83
SELECT 'Good_DU' as prediction, 0.5181 as confidence
FROM dataset WHERE [pickUpHourOfDay_VERYLATE] = 1 AND ([city_Delhi_NCR] = 0 OR [city_Delhi_NCR] IS NULL) AND [dayType_WEEKEND] = 1 AND ([city_Chennai] = 0 OR [city_Chennai] IS NULL) AND [zone_demand_popularity_POPULARITY_INDEX_4] = 1 AND [city_Mumbai] = 1;

-- Rule 23: WHEN zone=194 AND NONE(pickUpHourOfDay=VERYLATE, zone_demand_popularity=POPULARITY_INDEX_5, pickUpHourOfDay=LATENIGHT, zone=221)
-- Prediction: Good_DU (confidence: 0.609)
-- Samples: 69
SELECT 'Good_DU' as prediction, 0.6087 as confidence
FROM dataset WHERE ([pickUpHourOfDay_VERYLATE] = 0 OR [pickUpHourOfDay_VERYLATE] IS NULL) AND ([zone_demand_popularity_POPULARITY_INDEX_5] = 0 OR [zone_demand_popularity_POPULARITY_INDEX_5] IS NULL) AND ([pickUpHourOfDay_LATENIGHT] = 0 OR [pickUpHourOfDay_LATENIGHT] IS NULL) AND ([zone_221] = 0 OR [zone_221] IS NULL) AND [zone_194] = 1;

-- Rule 24: WHEN ALL(pickUpHourOfDay=VERYLATE, dayType=WEEKEND, zone_demand_popularity=POPULARITY_INDEX_4) AND NONE(city=Delhi NCR, city=Chennai, city=Mumbai)
-- Prediction: Good_DU (confidence: 0.606)
-- Samples: 66
SELECT 'Good_DU' as prediction, 0.6061 as confidence
FROM dataset WHERE [pickUpHourOfDay_VERYLATE] = 1 AND ([city_Delhi_NCR] = 0 OR [city_Delhi_NCR] IS NULL) AND [dayType_WEEKEND] = 1 AND ([city_Chennai] = 0 OR [city_Chennai] IS NULL) AND [zone_demand_popularity_POPULARITY_INDEX_4] = 1 AND ([city_Mumbai] = 0 OR [city_Mumbai] IS NULL);

-- Rule 25: WHEN ALL(pickUpHourOfDay=VERYLATE, dayType=WEEKEND, city=Chennai) AND NOT city=Delhi NCR
-- Prediction: Good_DU (confidence: 0.955)
-- Samples: 66
SELECT 'Good_DU' as prediction, 0.9545 as confidence
FROM dataset WHERE [pickUpHourOfDay_VERYLATE] = 1 AND ([city_Delhi_NCR] = 0 OR [city_Delhi_NCR] IS NULL) AND [dayType_WEEKEND] = 1 AND [city_Chennai] = 1;

-- Rule 26: WHEN ALL(pickUpHourOfDay=LATENIGHT, zone=217) AND NONE(pickUpHourOfDay=VERYLATE, zone_demand_popularity=POPULARITY_INDEX_5, dayType=NORMAL_WEEKDAY)
-- Prediction: Good_DU (confidence: 0.968)
-- Samples: 62
SELECT 'Good_DU' as prediction, 0.9677 as confidence
FROM dataset WHERE ([pickUpHourOfDay_VERYLATE] = 0 OR [pickUpHourOfDay_VERYLATE] IS NULL) AND ([zone_demand_popularity_POPULARITY_INDEX_5] = 0 OR [zone_demand_popularity_POPULARITY_INDEX_5] IS NULL) AND [pickUpHourOfDay_LATENIGHT] = 1 AND ([dayType_NORMAL_WEEKDAY] = 0 OR [dayType_NORMAL_WEEKDAY] IS NULL) AND [zone_217] = 1;

-- Rule 27: WHEN ALL(zone_demand_popularity=POPULARITY_INDEX_5, city=Pune, booking_type=outstation) AND NONE(pickUpHourOfDay=VERYLATE, pickUpHourOfDay=LATENIGHT)
-- Prediction: Good_DU (confidence: 0.903)
-- Samples: 62
SELECT 'Good_DU' as prediction, 0.9032 as confidence
FROM dataset WHERE ([pickUpHourOfDay_VERYLATE] = 0 OR [pickUpHourOfDay_VERYLATE] IS NULL) AND [zone_demand_popularity_POPULARITY_INDEX_5] = 1 AND ([pickUpHourOfDay_LATENIGHT] = 0 OR [pickUpHourOfDay_LATENIGHT] IS NULL) AND [city_Pune] = 1 AND [booking_type_outstation] = 1;

-- Rule 28: WHEN ALL(zone=221, estimated_usage_bins=GT_3_LTE_4_HOURS) AND NONE(pickUpHourOfDay=VERYLATE, zone_demand_popularity=POPULARITY_INDEX_5, pickUpHourOfDay=LATENIGHT, booking_type=one_way_trip)
-- Prediction: Good_DU (confidence: 0.770)
-- Samples: 61
SELECT 'Good_DU' as prediction, 0.7705 as confidence
FROM dataset WHERE ([pickUpHourOfDay_VERYLATE] = 0 OR [pickUpHourOfDay_VERYLATE] IS NULL) AND ([zone_demand_popularity_POPULARITY_INDEX_5] = 0 OR [zone_demand_popularity_POPULARITY_INDEX_5] IS NULL) AND ([pickUpHourOfDay_LATENIGHT] = 0 OR [pickUpHourOfDay_LATENIGHT] IS NULL) AND [zone_221] = 1 AND ([booking_type_one_way_trip] = 0 OR [booking_type_one_way_trip] IS NULL) AND [estimated_usage_bins_GT_3_LTE_4_HOURS] = 1;

-- Rule 29: WHEN ALL(pickUpHourOfDay=VERYLATE, city=Delhi NCR) AND NONE(zone_demand_popularity=POPULARITY_INDEX_2, zone_demand_popularity=POPULARITY_INDEX_4)
-- Prediction: Bad_DU (confidence: 0.633)
-- Samples: 60
SELECT 'Bad_DU' as prediction, 0.6333 as confidence
FROM dataset WHERE [pickUpHourOfDay_VERYLATE] = 1 AND [city_Delhi_NCR] = 1 AND ([zone_demand_popularity_POPULARITY_INDEX_2] = 0 OR [zone_demand_popularity_POPULARITY_INDEX_2] IS NULL) AND ([zone_demand_popularity_POPULARITY_INDEX_4] = 0 OR [zone_demand_popularity_POPULARITY_INDEX_4] IS NULL);

-- Rule 30: WHEN ALL(pickUpHourOfDay=VERYLATE, zone_demand_popularity=POPULARITY_INDEX_5) AND NONE(city=Delhi NCR, dayType=WEEKEND)
-- Prediction: Good_DU (confidence: 0.684)
-- Samples: 57
SELECT 'Good_DU' as prediction, 0.6842 as confidence
FROM dataset WHERE [pickUpHourOfDay_VERYLATE] = 1 AND ([city_Delhi_NCR] = 0 OR [city_Delhi_NCR] IS NULL) AND ([dayType_WEEKEND] = 0 OR [dayType_WEEKEND] IS NULL) AND [zone_demand_popularity_POPULARITY_INDEX_5] = 1;

-- Rule 31: WHEN ALL(pickUpHourOfDay=VERYLATE, city=Delhi NCR, zone_demand_popularity=POPULARITY_INDEX_2)
-- Prediction: Good_DU (confidence: 0.526)
-- Samples: 57
SELECT 'Good_DU' as prediction, 0.5263 as confidence
FROM dataset WHERE [pickUpHourOfDay_VERYLATE] = 1 AND [city_Delhi_NCR] = 1 AND [zone_demand_popularity_POPULARITY_INDEX_2] = 1;

-- Rule 32: WHEN ALL(zone_demand_popularity=POPULARITY_INDEX_5, pickUpHourOfDay=LATENIGHT, city=Mumbai) AND NOT pickUpHourOfDay=VERYLATE
-- Prediction: Good_DU (confidence: 0.704)
-- Samples: 54
SELECT 'Good_DU' as prediction, 0.7037 as confidence
FROM dataset WHERE ([pickUpHourOfDay_VERYLATE] = 0 OR [pickUpHourOfDay_VERYLATE] IS NULL) AND [zone_demand_popularity_POPULARITY_INDEX_5] = 1 AND [pickUpHourOfDay_LATENIGHT] = 1 AND [city_Mumbai] = 1;

-- Rule 33: WHEN ALL(pickUpHourOfDay=VERYLATE, city=Delhi NCR, zone_demand_popularity=POPULARITY_INDEX_4) AND NOT zone_demand_popularity=POPULARITY_INDEX_2
-- Prediction: Bad_DU (confidence: 0.510)
-- Samples: 51
SELECT 'Bad_DU' as prediction, 0.5098 as confidence
FROM dataset WHERE [pickUpHourOfDay_VERYLATE] = 1 AND [city_Delhi_NCR] = 1 AND ([zone_demand_popularity_POPULARITY_INDEX_2] = 0 OR [zone_demand_popularity_POPULARITY_INDEX_2] IS NULL) AND [zone_demand_popularity_POPULARITY_INDEX_4] = 1;

