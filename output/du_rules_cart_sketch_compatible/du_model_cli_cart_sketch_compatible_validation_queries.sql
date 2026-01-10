-- CART-OLAP Decision Tree Validation Queries
-- Generated from: output/du_model_cli_cart_sketch_compatible.json
-- Total rules: 34
-- Table: DU_raw
-- Target column: target


-- Rule 1: pickUpHourOfDay=VERYLATE is FALSE AND zone_demand_popularity=POPULARITY_INDEX_5 is FALSE AND pickUpHourOfDay=LATENIGHT is FALSE AND zone=221 is FALSE AND zone=194 is FALSE AND sla=Immediate is FALSE
SELECT
    COUNT(*) as actual_samples,
    12794 as expected_samples,
    ROUND(AVG(CASE WHEN target = 1 THEN 1.0 ELSE 0.0 END), 4) as actual_positive_rate,
    0.9035 as expected_positive_rate,
    'Positive' as expected_prediction
FROM DU_raw
WHERE `pickUpHourOfDay=VERYLATE` = 0 AND `zone_demand_popularity=POPULARITY_INDEX_5` = 0 AND `pickUpHourOfDay=LATENIGHT` = 0 AND `zone=221` = 0 AND `zone=194` = 0 AND `sla=Immediate` = 0;


--------------------------------------------------------------------------------


-- Rule 2: pickUpHourOfDay=VERYLATE is FALSE AND zone_demand_popularity=POPULARITY_INDEX_5 is FALSE AND pickUpHourOfDay=LATENIGHT is FALSE AND zone=221 is FALSE AND zone=194 is FALSE AND sla=Immediate is TRUE
SELECT
    COUNT(*) as actual_samples,
    697 as expected_samples,
    ROUND(AVG(CASE WHEN target = 1 THEN 1.0 ELSE 0.0 END), 4) as actual_positive_rate,
    0.99 as expected_positive_rate,
    'Positive' as expected_prediction
FROM DU_raw
WHERE `pickUpHourOfDay=VERYLATE` = 0 AND `zone_demand_popularity=POPULARITY_INDEX_5` = 0 AND `pickUpHourOfDay=LATENIGHT` = 0 AND `zone=221` = 0 AND `zone=194` = 0 AND `sla=Immediate` = 1;


--------------------------------------------------------------------------------


-- Rule 3: pickUpHourOfDay=VERYLATE is FALSE AND zone_demand_popularity=POPULARITY_INDEX_5 is FALSE AND pickUpHourOfDay=LATENIGHT is FALSE AND zone=221 is FALSE AND zone=194 is TRUE
SELECT
    COUNT(*) as actual_samples,
    69 as expected_samples,
    ROUND(AVG(CASE WHEN target = 1 THEN 1.0 ELSE 0.0 END), 4) as actual_positive_rate,
    0.6087 as expected_positive_rate,
    'Positive' as expected_prediction
FROM DU_raw
WHERE `pickUpHourOfDay=VERYLATE` = 0 AND `zone_demand_popularity=POPULARITY_INDEX_5` = 0 AND `pickUpHourOfDay=LATENIGHT` = 0 AND `zone=221` = 0 AND `zone=194` = 1;


--------------------------------------------------------------------------------


-- Rule 4: pickUpHourOfDay=VERYLATE is FALSE AND zone_demand_popularity=POPULARITY_INDEX_5 is FALSE AND pickUpHourOfDay=LATENIGHT is FALSE AND zone=221 is TRUE AND booking_type=one_way_trip is FALSE AND estimated_usage_bins=GT_3_LTE_4_HOURS is FALSE
SELECT
    COUNT(*) as actual_samples,
    97 as expected_samples,
    ROUND(AVG(CASE WHEN target = 1 THEN 1.0 ELSE 0.0 END), 4) as actual_positive_rate,
    0.8454 as expected_positive_rate,
    'Positive' as expected_prediction
FROM DU_raw
WHERE `pickUpHourOfDay=VERYLATE` = 0 AND `zone_demand_popularity=POPULARITY_INDEX_5` = 0 AND `pickUpHourOfDay=LATENIGHT` = 0 AND `zone=221` = 1 AND `booking_type=one_way_trip` = 0 AND `estimated_usage_bins=GT_3_LTE_4_HOURS` = 0;


--------------------------------------------------------------------------------


-- Rule 5: pickUpHourOfDay=VERYLATE is FALSE AND zone_demand_popularity=POPULARITY_INDEX_5 is FALSE AND pickUpHourOfDay=LATENIGHT is FALSE AND zone=221 is TRUE AND booking_type=one_way_trip is FALSE AND estimated_usage_bins=GT_3_LTE_4_HOURS is TRUE
SELECT
    COUNT(*) as actual_samples,
    61 as expected_samples,
    ROUND(AVG(CASE WHEN target = 1 THEN 1.0 ELSE 0.0 END), 4) as actual_positive_rate,
    0.7705 as expected_positive_rate,
    'Positive' as expected_prediction
FROM DU_raw
WHERE `pickUpHourOfDay=VERYLATE` = 0 AND `zone_demand_popularity=POPULARITY_INDEX_5` = 0 AND `pickUpHourOfDay=LATENIGHT` = 0 AND `zone=221` = 1 AND `booking_type=one_way_trip` = 0 AND `estimated_usage_bins=GT_3_LTE_4_HOURS` = 1;


--------------------------------------------------------------------------------


-- Rule 6: pickUpHourOfDay=VERYLATE is FALSE AND zone_demand_popularity=POPULARITY_INDEX_5 is FALSE AND pickUpHourOfDay=LATENIGHT is FALSE AND zone=221 is TRUE AND booking_type=one_way_trip is TRUE
SELECT
    COUNT(*) as actual_samples,
    90 as expected_samples,
    ROUND(AVG(CASE WHEN target = 1 THEN 1.0 ELSE 0.0 END), 4) as actual_positive_rate,
    0.6111 as expected_positive_rate,
    'Positive' as expected_prediction
FROM DU_raw
WHERE `pickUpHourOfDay=VERYLATE` = 0 AND `zone_demand_popularity=POPULARITY_INDEX_5` = 0 AND `pickUpHourOfDay=LATENIGHT` = 0 AND `zone=221` = 1 AND `booking_type=one_way_trip` = 1;


--------------------------------------------------------------------------------


-- Rule 7: pickUpHourOfDay=VERYLATE is FALSE AND zone_demand_popularity=POPULARITY_INDEX_5 is FALSE AND pickUpHourOfDay=LATENIGHT is TRUE AND dayType=NORMAL_WEEKDAY is FALSE AND zone=217 is FALSE AND city=Mumbai is FALSE
SELECT
    COUNT(*) as actual_samples,
    644 as expected_samples,
    ROUND(AVG(CASE WHEN target = 1 THEN 1.0 ELSE 0.0 END), 4) as actual_positive_rate,
    0.7205 as expected_positive_rate,
    'Positive' as expected_prediction
FROM DU_raw
WHERE `pickUpHourOfDay=VERYLATE` = 0 AND `zone_demand_popularity=POPULARITY_INDEX_5` = 0 AND `pickUpHourOfDay=LATENIGHT` = 1 AND `dayType=NORMAL_WEEKDAY` = 0 AND `zone=217` = 0 AND `city=Mumbai` = 0;


--------------------------------------------------------------------------------


-- Rule 8: pickUpHourOfDay=VERYLATE is FALSE AND zone_demand_popularity=POPULARITY_INDEX_5 is FALSE AND pickUpHourOfDay=LATENIGHT is TRUE AND dayType=NORMAL_WEEKDAY is FALSE AND zone=217 is FALSE AND city=Mumbai is TRUE
SELECT
    COUNT(*) as actual_samples,
    230 as expected_samples,
    ROUND(AVG(CASE WHEN target = 1 THEN 1.0 ELSE 0.0 END), 4) as actual_positive_rate,
    0.8391 as expected_positive_rate,
    'Positive' as expected_prediction
FROM DU_raw
WHERE `pickUpHourOfDay=VERYLATE` = 0 AND `zone_demand_popularity=POPULARITY_INDEX_5` = 0 AND `pickUpHourOfDay=LATENIGHT` = 1 AND `dayType=NORMAL_WEEKDAY` = 0 AND `zone=217` = 0 AND `city=Mumbai` = 1;


--------------------------------------------------------------------------------


-- Rule 9: pickUpHourOfDay=VERYLATE is FALSE AND zone_demand_popularity=POPULARITY_INDEX_5 is FALSE AND pickUpHourOfDay=LATENIGHT is TRUE AND dayType=NORMAL_WEEKDAY is FALSE AND zone=217 is TRUE
SELECT
    COUNT(*) as actual_samples,
    62 as expected_samples,
    ROUND(AVG(CASE WHEN target = 1 THEN 1.0 ELSE 0.0 END), 4) as actual_positive_rate,
    0.9677 as expected_positive_rate,
    'Positive' as expected_prediction
FROM DU_raw
WHERE `pickUpHourOfDay=VERYLATE` = 0 AND `zone_demand_popularity=POPULARITY_INDEX_5` = 0 AND `pickUpHourOfDay=LATENIGHT` = 1 AND `dayType=NORMAL_WEEKDAY` = 0 AND `zone=217` = 1;


--------------------------------------------------------------------------------


-- Rule 10: pickUpHourOfDay=VERYLATE is FALSE AND zone_demand_popularity=POPULARITY_INDEX_5 is FALSE AND pickUpHourOfDay=LATENIGHT is TRUE AND dayType=NORMAL_WEEKDAY is TRUE AND zone_demand_popularity=POPULARITY_INDEX_1 is FALSE AND city=Mumbai is FALSE
SELECT
    COUNT(*) as actual_samples,
    249 as expected_samples,
    ROUND(AVG(CASE WHEN target = 1 THEN 1.0 ELSE 0.0 END), 4) as actual_positive_rate,
    0.8193 as expected_positive_rate,
    'Positive' as expected_prediction
FROM DU_raw
WHERE `pickUpHourOfDay=VERYLATE` = 0 AND `zone_demand_popularity=POPULARITY_INDEX_5` = 0 AND `pickUpHourOfDay=LATENIGHT` = 1 AND `dayType=NORMAL_WEEKDAY` = 1 AND `zone_demand_popularity=POPULARITY_INDEX_1` = 0 AND `city=Mumbai` = 0;


--------------------------------------------------------------------------------


-- Rule 11: pickUpHourOfDay=VERYLATE is FALSE AND zone_demand_popularity=POPULARITY_INDEX_5 is FALSE AND pickUpHourOfDay=LATENIGHT is TRUE AND dayType=NORMAL_WEEKDAY is TRUE AND zone_demand_popularity=POPULARITY_INDEX_1 is FALSE AND city=Mumbai is TRUE
SELECT
    COUNT(*) as actual_samples,
    116 as expected_samples,
    ROUND(AVG(CASE WHEN target = 1 THEN 1.0 ELSE 0.0 END), 4) as actual_positive_rate,
    0.9655 as expected_positive_rate,
    'Positive' as expected_prediction
FROM DU_raw
WHERE `pickUpHourOfDay=VERYLATE` = 0 AND `zone_demand_popularity=POPULARITY_INDEX_5` = 0 AND `pickUpHourOfDay=LATENIGHT` = 1 AND `dayType=NORMAL_WEEKDAY` = 1 AND `zone_demand_popularity=POPULARITY_INDEX_1` = 0 AND `city=Mumbai` = 1;


--------------------------------------------------------------------------------


-- Rule 12: pickUpHourOfDay=VERYLATE is FALSE AND zone_demand_popularity=POPULARITY_INDEX_5 is FALSE AND pickUpHourOfDay=LATENIGHT is TRUE AND dayType=NORMAL_WEEKDAY is TRUE AND zone_demand_popularity=POPULARITY_INDEX_1 is TRUE AND zone=219 is FALSE
SELECT
    COUNT(*) as actual_samples,
    241 as expected_samples,
    ROUND(AVG(CASE WHEN target = 1 THEN 1.0 ELSE 0.0 END), 4) as actual_positive_rate,
    0.9419 as expected_positive_rate,
    'Positive' as expected_prediction
FROM DU_raw
WHERE `pickUpHourOfDay=VERYLATE` = 0 AND `zone_demand_popularity=POPULARITY_INDEX_5` = 0 AND `pickUpHourOfDay=LATENIGHT` = 1 AND `dayType=NORMAL_WEEKDAY` = 1 AND `zone_demand_popularity=POPULARITY_INDEX_1` = 1 AND `zone=219` = 0;


--------------------------------------------------------------------------------


-- Rule 13: pickUpHourOfDay=VERYLATE is FALSE AND zone_demand_popularity=POPULARITY_INDEX_5 is FALSE AND pickUpHourOfDay=LATENIGHT is TRUE AND dayType=NORMAL_WEEKDAY is TRUE AND zone_demand_popularity=POPULARITY_INDEX_1 is TRUE AND zone=219 is TRUE
SELECT
    COUNT(*) as actual_samples,
    96 as expected_samples,
    ROUND(AVG(CASE WHEN target = 1 THEN 1.0 ELSE 0.0 END), 4) as actual_positive_rate,
    0.9688 as expected_positive_rate,
    'Positive' as expected_prediction
FROM DU_raw
WHERE `pickUpHourOfDay=VERYLATE` = 0 AND `zone_demand_popularity=POPULARITY_INDEX_5` = 0 AND `pickUpHourOfDay=LATENIGHT` = 1 AND `dayType=NORMAL_WEEKDAY` = 1 AND `zone_demand_popularity=POPULARITY_INDEX_1` = 1 AND `zone=219` = 1;


--------------------------------------------------------------------------------


-- Rule 14: pickUpHourOfDay=VERYLATE is FALSE AND zone_demand_popularity=POPULARITY_INDEX_5 is TRUE AND pickUpHourOfDay=LATENIGHT is FALSE AND city=Pune is FALSE AND city=Mumbai is FALSE AND city=Hyderabad is FALSE
SELECT
    COUNT(*) as actual_samples,
    1397 as expected_samples,
    ROUND(AVG(CASE WHEN target = 1 THEN 1.0 ELSE 0.0 END), 4) as actual_positive_rate,
    0.8905 as expected_positive_rate,
    'Positive' as expected_prediction
FROM DU_raw
WHERE `pickUpHourOfDay=VERYLATE` = 0 AND `zone_demand_popularity=POPULARITY_INDEX_5` = 1 AND `pickUpHourOfDay=LATENIGHT` = 0 AND `city=Pune` = 0 AND `city=Mumbai` = 0 AND `city=Hyderabad` = 0;


--------------------------------------------------------------------------------


-- Rule 15: pickUpHourOfDay=VERYLATE is FALSE AND zone_demand_popularity=POPULARITY_INDEX_5 is TRUE AND pickUpHourOfDay=LATENIGHT is FALSE AND city=Pune is FALSE AND city=Mumbai is FALSE AND city=Hyderabad is TRUE
SELECT
    COUNT(*) as actual_samples,
    92 as expected_samples,
    ROUND(AVG(CASE WHEN target = 1 THEN 1.0 ELSE 0.0 END), 4) as actual_positive_rate,
    0.7174 as expected_positive_rate,
    'Positive' as expected_prediction
FROM DU_raw
WHERE `pickUpHourOfDay=VERYLATE` = 0 AND `zone_demand_popularity=POPULARITY_INDEX_5` = 1 AND `pickUpHourOfDay=LATENIGHT` = 0 AND `city=Pune` = 0 AND `city=Mumbai` = 0 AND `city=Hyderabad` = 1;


--------------------------------------------------------------------------------


-- Rule 16: pickUpHourOfDay=VERYLATE is FALSE AND zone_demand_popularity=POPULARITY_INDEX_5 is TRUE AND pickUpHourOfDay=LATENIGHT is FALSE AND city=Pune is FALSE AND city=Mumbai is TRUE AND booking_type=round_trip is FALSE
SELECT
    COUNT(*) as actual_samples,
    397 as expected_samples,
    ROUND(AVG(CASE WHEN target = 1 THEN 1.0 ELSE 0.0 END), 4) as actual_positive_rate,
    0.8212 as expected_positive_rate,
    'Positive' as expected_prediction
FROM DU_raw
WHERE `pickUpHourOfDay=VERYLATE` = 0 AND `zone_demand_popularity=POPULARITY_INDEX_5` = 1 AND `pickUpHourOfDay=LATENIGHT` = 0 AND `city=Pune` = 0 AND `city=Mumbai` = 1 AND `booking_type=round_trip` = 0;


--------------------------------------------------------------------------------


-- Rule 17: pickUpHourOfDay=VERYLATE is FALSE AND zone_demand_popularity=POPULARITY_INDEX_5 is TRUE AND pickUpHourOfDay=LATENIGHT is FALSE AND city=Pune is FALSE AND city=Mumbai is TRUE AND booking_type=round_trip is TRUE
SELECT
    COUNT(*) as actual_samples,
    189 as expected_samples,
    ROUND(AVG(CASE WHEN target = 1 THEN 1.0 ELSE 0.0 END), 4) as actual_positive_rate,
    0.6825 as expected_positive_rate,
    'Positive' as expected_prediction
FROM DU_raw
WHERE `pickUpHourOfDay=VERYLATE` = 0 AND `zone_demand_popularity=POPULARITY_INDEX_5` = 1 AND `pickUpHourOfDay=LATENIGHT` = 0 AND `city=Pune` = 0 AND `city=Mumbai` = 1 AND `booking_type=round_trip` = 1;


--------------------------------------------------------------------------------


-- Rule 18: pickUpHourOfDay=VERYLATE is FALSE AND zone_demand_popularity=POPULARITY_INDEX_5 is TRUE AND pickUpHourOfDay=LATENIGHT is FALSE AND city=Pune is TRUE AND booking_type=outstation is FALSE AND pickUpHourOfDay=MORNING is FALSE
SELECT
    COUNT(*) as actual_samples,
    201 as expected_samples,
    ROUND(AVG(CASE WHEN target = 1 THEN 1.0 ELSE 0.0 END), 4) as actual_positive_rate,
    0.6119 as expected_positive_rate,
    'Positive' as expected_prediction
FROM DU_raw
WHERE `pickUpHourOfDay=VERYLATE` = 0 AND `zone_demand_popularity=POPULARITY_INDEX_5` = 1 AND `pickUpHourOfDay=LATENIGHT` = 0 AND `city=Pune` = 1 AND `booking_type=outstation` = 0 AND `pickUpHourOfDay=MORNING` = 0;


--------------------------------------------------------------------------------


-- Rule 19: pickUpHourOfDay=VERYLATE is FALSE AND zone_demand_popularity=POPULARITY_INDEX_5 is TRUE AND pickUpHourOfDay=LATENIGHT is FALSE AND city=Pune is TRUE AND booking_type=outstation is FALSE AND pickUpHourOfDay=MORNING is TRUE
SELECT
    COUNT(*) as actual_samples,
    90 as expected_samples,
    ROUND(AVG(CASE WHEN target = 1 THEN 1.0 ELSE 0.0 END), 4) as actual_positive_rate,
    0.8111 as expected_positive_rate,
    'Positive' as expected_prediction
FROM DU_raw
WHERE `pickUpHourOfDay=VERYLATE` = 0 AND `zone_demand_popularity=POPULARITY_INDEX_5` = 1 AND `pickUpHourOfDay=LATENIGHT` = 0 AND `city=Pune` = 1 AND `booking_type=outstation` = 0 AND `pickUpHourOfDay=MORNING` = 1;


--------------------------------------------------------------------------------


-- Rule 20: pickUpHourOfDay=VERYLATE is FALSE AND zone_demand_popularity=POPULARITY_INDEX_5 is TRUE AND pickUpHourOfDay=LATENIGHT is FALSE AND city=Pune is TRUE AND booking_type=outstation is TRUE
SELECT
    COUNT(*) as actual_samples,
    62 as expected_samples,
    ROUND(AVG(CASE WHEN target = 1 THEN 1.0 ELSE 0.0 END), 4) as actual_positive_rate,
    0.9032 as expected_positive_rate,
    'Positive' as expected_prediction
FROM DU_raw
WHERE `pickUpHourOfDay=VERYLATE` = 0 AND `zone_demand_popularity=POPULARITY_INDEX_5` = 1 AND `pickUpHourOfDay=LATENIGHT` = 0 AND `city=Pune` = 1 AND `booking_type=outstation` = 1;


--------------------------------------------------------------------------------


-- Rule 21: pickUpHourOfDay=VERYLATE is FALSE AND zone_demand_popularity=POPULARITY_INDEX_5 is TRUE AND pickUpHourOfDay=LATENIGHT is TRUE AND city=Mumbai is FALSE
SELECT
    COUNT(*) as actual_samples,
    85 as expected_samples,
    ROUND(AVG(CASE WHEN target = 1 THEN 1.0 ELSE 0.0 END), 4) as actual_positive_rate,
    0.5059 as expected_positive_rate,
    'Positive' as expected_prediction
FROM DU_raw
WHERE `pickUpHourOfDay=VERYLATE` = 0 AND `zone_demand_popularity=POPULARITY_INDEX_5` = 1 AND `pickUpHourOfDay=LATENIGHT` = 1 AND `city=Mumbai` = 0;


--------------------------------------------------------------------------------


-- Rule 22: pickUpHourOfDay=VERYLATE is FALSE AND zone_demand_popularity=POPULARITY_INDEX_5 is TRUE AND pickUpHourOfDay=LATENIGHT is TRUE AND city=Mumbai is TRUE
SELECT
    COUNT(*) as actual_samples,
    54 as expected_samples,
    ROUND(AVG(CASE WHEN target = 1 THEN 1.0 ELSE 0.0 END), 4) as actual_positive_rate,
    0.7037 as expected_positive_rate,
    'Positive' as expected_prediction
FROM DU_raw
WHERE `pickUpHourOfDay=VERYLATE` = 0 AND `zone_demand_popularity=POPULARITY_INDEX_5` = 1 AND `pickUpHourOfDay=LATENIGHT` = 1 AND `city=Mumbai` = 1;


--------------------------------------------------------------------------------


-- Rule 23: pickUpHourOfDay=VERYLATE is TRUE AND city=Delhi NCR is FALSE AND dayType=WEEKEND is FALSE AND zone_demand_popularity=POPULARITY_INDEX_5 is FALSE AND city=Hyderabad is FALSE AND zone_demand_popularity=POPULARITY_INDEX_1 is FALSE
SELECT
    COUNT(*) as actual_samples,
    395 as expected_samples,
    ROUND(AVG(CASE WHEN target = 1 THEN 1.0 ELSE 0.0 END), 4) as actual_positive_rate,
    0.8861 as expected_positive_rate,
    'Positive' as expected_prediction
FROM DU_raw
WHERE `pickUpHourOfDay=VERYLATE` = 1 AND `city=Delhi NCR` = 0 AND `dayType=WEEKEND` = 0 AND `zone_demand_popularity=POPULARITY_INDEX_5` = 0 AND `city=Hyderabad` = 0 AND `zone_demand_popularity=POPULARITY_INDEX_1` = 0;


--------------------------------------------------------------------------------


-- Rule 24: pickUpHourOfDay=VERYLATE is TRUE AND city=Delhi NCR is FALSE AND dayType=WEEKEND is FALSE AND zone_demand_popularity=POPULARITY_INDEX_5 is FALSE AND city=Hyderabad is FALSE AND zone_demand_popularity=POPULARITY_INDEX_1 is TRUE
SELECT
    COUNT(*) as actual_samples,
    326 as expected_samples,
    ROUND(AVG(CASE WHEN target = 1 THEN 1.0 ELSE 0.0 END), 4) as actual_positive_rate,
    0.954 as expected_positive_rate,
    'Positive' as expected_prediction
FROM DU_raw
WHERE `pickUpHourOfDay=VERYLATE` = 1 AND `city=Delhi NCR` = 0 AND `dayType=WEEKEND` = 0 AND `zone_demand_popularity=POPULARITY_INDEX_5` = 0 AND `city=Hyderabad` = 0 AND `zone_demand_popularity=POPULARITY_INDEX_1` = 1;


--------------------------------------------------------------------------------


-- Rule 25: pickUpHourOfDay=VERYLATE is TRUE AND city=Delhi NCR is FALSE AND dayType=WEEKEND is FALSE AND zone_demand_popularity=POPULARITY_INDEX_5 is FALSE AND city=Hyderabad is TRUE
SELECT
    COUNT(*) as actual_samples,
    90 as expected_samples,
    ROUND(AVG(CASE WHEN target = 1 THEN 1.0 ELSE 0.0 END), 4) as actual_positive_rate,
    0.7444 as expected_positive_rate,
    'Positive' as expected_prediction
FROM DU_raw
WHERE `pickUpHourOfDay=VERYLATE` = 1 AND `city=Delhi NCR` = 0 AND `dayType=WEEKEND` = 0 AND `zone_demand_popularity=POPULARITY_INDEX_5` = 0 AND `city=Hyderabad` = 1;


--------------------------------------------------------------------------------


-- Rule 26: pickUpHourOfDay=VERYLATE is TRUE AND city=Delhi NCR is FALSE AND dayType=WEEKEND is FALSE AND zone_demand_popularity=POPULARITY_INDEX_5 is TRUE
SELECT
    COUNT(*) as actual_samples,
    57 as expected_samples,
    ROUND(AVG(CASE WHEN target = 1 THEN 1.0 ELSE 0.0 END), 4) as actual_positive_rate,
    0.6842 as expected_positive_rate,
    'Positive' as expected_prediction
FROM DU_raw
WHERE `pickUpHourOfDay=VERYLATE` = 1 AND `city=Delhi NCR` = 0 AND `dayType=WEEKEND` = 0 AND `zone_demand_popularity=POPULARITY_INDEX_5` = 1;


--------------------------------------------------------------------------------


-- Rule 27: pickUpHourOfDay=VERYLATE is TRUE AND city=Delhi NCR is FALSE AND dayType=WEEKEND is TRUE AND city=Chennai is FALSE AND zone_demand_popularity=POPULARITY_INDEX_4 is FALSE AND zone=216 is FALSE
SELECT
    COUNT(*) as actual_samples,
    996 as expected_samples,
    ROUND(AVG(CASE WHEN target = 1 THEN 1.0 ELSE 0.0 END), 4) as actual_positive_rate,
    0.744 as expected_positive_rate,
    'Positive' as expected_prediction
FROM DU_raw
WHERE `pickUpHourOfDay=VERYLATE` = 1 AND `city=Delhi NCR` = 0 AND `dayType=WEEKEND` = 1 AND `city=Chennai` = 0 AND `zone_demand_popularity=POPULARITY_INDEX_4` = 0 AND `zone=216` = 0;


--------------------------------------------------------------------------------


-- Rule 28: pickUpHourOfDay=VERYLATE is TRUE AND city=Delhi NCR is FALSE AND dayType=WEEKEND is TRUE AND city=Chennai is FALSE AND zone_demand_popularity=POPULARITY_INDEX_4 is FALSE AND zone=216 is TRUE
SELECT
    COUNT(*) as actual_samples,
    83 as expected_samples,
    ROUND(AVG(CASE WHEN target = 1 THEN 1.0 ELSE 0.0 END), 4) as actual_positive_rate,
    0.9277 as expected_positive_rate,
    'Positive' as expected_prediction
FROM DU_raw
WHERE `pickUpHourOfDay=VERYLATE` = 1 AND `city=Delhi NCR` = 0 AND `dayType=WEEKEND` = 1 AND `city=Chennai` = 0 AND `zone_demand_popularity=POPULARITY_INDEX_4` = 0 AND `zone=216` = 1;


--------------------------------------------------------------------------------


-- Rule 29: pickUpHourOfDay=VERYLATE is TRUE AND city=Delhi NCR is FALSE AND dayType=WEEKEND is TRUE AND city=Chennai is FALSE AND zone_demand_popularity=POPULARITY_INDEX_4 is TRUE AND city=Mumbai is FALSE
SELECT
    COUNT(*) as actual_samples,
    66 as expected_samples,
    ROUND(AVG(CASE WHEN target = 1 THEN 1.0 ELSE 0.0 END), 4) as actual_positive_rate,
    0.6061 as expected_positive_rate,
    'Positive' as expected_prediction
FROM DU_raw
WHERE `pickUpHourOfDay=VERYLATE` = 1 AND `city=Delhi NCR` = 0 AND `dayType=WEEKEND` = 1 AND `city=Chennai` = 0 AND `zone_demand_popularity=POPULARITY_INDEX_4` = 1 AND `city=Mumbai` = 0;


--------------------------------------------------------------------------------


-- Rule 30: pickUpHourOfDay=VERYLATE is TRUE AND city=Delhi NCR is FALSE AND dayType=WEEKEND is TRUE AND city=Chennai is FALSE AND zone_demand_popularity=POPULARITY_INDEX_4 is TRUE AND city=Mumbai is TRUE
SELECT
    COUNT(*) as actual_samples,
    83 as expected_samples,
    ROUND(AVG(CASE WHEN target = 1 THEN 1.0 ELSE 0.0 END), 4) as actual_positive_rate,
    0.5181 as expected_positive_rate,
    'Positive' as expected_prediction
FROM DU_raw
WHERE `pickUpHourOfDay=VERYLATE` = 1 AND `city=Delhi NCR` = 0 AND `dayType=WEEKEND` = 1 AND `city=Chennai` = 0 AND `zone_demand_popularity=POPULARITY_INDEX_4` = 1 AND `city=Mumbai` = 1;


--------------------------------------------------------------------------------


-- Rule 31: pickUpHourOfDay=VERYLATE is TRUE AND city=Delhi NCR is FALSE AND dayType=WEEKEND is TRUE AND city=Chennai is TRUE
SELECT
    COUNT(*) as actual_samples,
    66 as expected_samples,
    ROUND(AVG(CASE WHEN target = 1 THEN 1.0 ELSE 0.0 END), 4) as actual_positive_rate,
    0.9545 as expected_positive_rate,
    'Positive' as expected_prediction
FROM DU_raw
WHERE `pickUpHourOfDay=VERYLATE` = 1 AND `city=Delhi NCR` = 0 AND `dayType=WEEKEND` = 1 AND `city=Chennai` = 1;


--------------------------------------------------------------------------------


-- Rule 32: pickUpHourOfDay=VERYLATE is TRUE AND city=Delhi NCR is TRUE AND zone_demand_popularity=POPULARITY_INDEX_2 is FALSE AND zone_demand_popularity=POPULARITY_INDEX_4 is FALSE
SELECT
    COUNT(*) as actual_samples,
    60 as expected_samples,
    ROUND(AVG(CASE WHEN target = 1 THEN 1.0 ELSE 0.0 END), 4) as actual_positive_rate,
    0.3667 as expected_positive_rate,
    'Negative' as expected_prediction
FROM DU_raw
WHERE `pickUpHourOfDay=VERYLATE` = 1 AND `city=Delhi NCR` = 1 AND `zone_demand_popularity=POPULARITY_INDEX_2` = 0 AND `zone_demand_popularity=POPULARITY_INDEX_4` = 0;


--------------------------------------------------------------------------------


-- Rule 33: pickUpHourOfDay=VERYLATE is TRUE AND city=Delhi NCR is TRUE AND zone_demand_popularity=POPULARITY_INDEX_2 is FALSE AND zone_demand_popularity=POPULARITY_INDEX_4 is TRUE
SELECT
    COUNT(*) as actual_samples,
    51 as expected_samples,
    ROUND(AVG(CASE WHEN target = 1 THEN 1.0 ELSE 0.0 END), 4) as actual_positive_rate,
    0.4902 as expected_positive_rate,
    'Negative' as expected_prediction
FROM DU_raw
WHERE `pickUpHourOfDay=VERYLATE` = 1 AND `city=Delhi NCR` = 1 AND `zone_demand_popularity=POPULARITY_INDEX_2` = 0 AND `zone_demand_popularity=POPULARITY_INDEX_4` = 1;


--------------------------------------------------------------------------------


-- Rule 34: pickUpHourOfDay=VERYLATE is TRUE AND city=Delhi NCR is TRUE AND zone_demand_popularity=POPULARITY_INDEX_2 is TRUE
SELECT
    COUNT(*) as actual_samples,
    57 as expected_samples,
    ROUND(AVG(CASE WHEN target = 1 THEN 1.0 ELSE 0.0 END), 4) as actual_positive_rate,
    0.5263 as expected_positive_rate,
    'Positive' as expected_prediction
FROM DU_raw
WHERE `pickUpHourOfDay=VERYLATE` = 1 AND `city=Delhi NCR` = 1 AND `zone_demand_popularity=POPULARITY_INDEX_2` = 1;

