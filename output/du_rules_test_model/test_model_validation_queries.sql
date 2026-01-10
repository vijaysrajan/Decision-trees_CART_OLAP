-- CART-OLAP Decision Tree Validation Queries
-- Generated from: output/test_model.json
-- Total rules: 34
-- Table: DU_raw
-- Target column: target


-- Rule 1: pickUpHourOfDay=VERYLATE is FALSE AND zone_demand_popularity=POPULARITY_INDEX_5 is FALSE AND pickUpHourOfDay=LATENIGHT is FALSE
SELECT
    COUNT(*) as actual_samples,
    13808 as expected_samples,
    ROUND(AVG(CASE WHEN target = 1 THEN 1.0 ELSE 0.0 END), 4) as actual_positive_rate,
    0.9035 as expected_positive_rate,
    'Positive' as expected_prediction
FROM DU_raw
WHERE `pickUpHourOfDay=VERYLATE` = 0 AND `zone_demand_popularity=POPULARITY_INDEX_5` = 0 AND `pickUpHourOfDay=LATENIGHT` = 0;


--------------------------------------------------------------------------------


-- Rule 2: pickUpHourOfDay=VERYLATE is FALSE AND zone_demand_popularity=POPULARITY_INDEX_5 is FALSE AND pickUpHourOfDay=LATENIGHT is TRUE AND dayType=NORMAL_WEEKDAY is FALSE AND zone=217 is FALSE AND city=Mumbai is FALSE
SELECT
    COUNT(*) as actual_samples,
    644 as expected_samples,
    ROUND(AVG(CASE WHEN target = 1 THEN 1.0 ELSE 0.0 END), 4) as actual_positive_rate,
    0.7205 as expected_positive_rate,
    'Positive' as expected_prediction
FROM DU_raw
WHERE `pickUpHourOfDay=VERYLATE` = 0 AND `zone_demand_popularity=POPULARITY_INDEX_5` = 0 AND `pickUpHourOfDay=LATENIGHT` = 1 AND `dayType=NORMAL_WEEKDAY` = 0 AND `zone=217` = 0 AND `city=Mumbai` = 0;


--------------------------------------------------------------------------------


-- Rule 3: pickUpHourOfDay=VERYLATE is FALSE AND zone_demand_popularity=POPULARITY_INDEX_5 is FALSE AND pickUpHourOfDay=LATENIGHT is TRUE AND dayType=NORMAL_WEEKDAY is FALSE AND zone=217 is FALSE AND city=Mumbai is TRUE
SELECT
    COUNT(*) as actual_samples,
    230 as expected_samples,
    ROUND(AVG(CASE WHEN target = 1 THEN 1.0 ELSE 0.0 END), 4) as actual_positive_rate,
    0.8391 as expected_positive_rate,
    'Positive' as expected_prediction
FROM DU_raw
WHERE `pickUpHourOfDay=VERYLATE` = 0 AND `zone_demand_popularity=POPULARITY_INDEX_5` = 0 AND `pickUpHourOfDay=LATENIGHT` = 1 AND `dayType=NORMAL_WEEKDAY` = 0 AND `zone=217` = 0 AND `city=Mumbai` = 1;


--------------------------------------------------------------------------------


-- Rule 4: pickUpHourOfDay=VERYLATE is FALSE AND zone_demand_popularity=POPULARITY_INDEX_5 is FALSE AND pickUpHourOfDay=LATENIGHT is TRUE AND dayType=NORMAL_WEEKDAY is FALSE AND zone=217 is TRUE AND dayType=FRIDAY is FALSE
SELECT
    COUNT(*) as actual_samples,
    38 as expected_samples,
    ROUND(AVG(CASE WHEN target = 1 THEN 1.0 ELSE 0.0 END), 4) as actual_positive_rate,
    1.0 as expected_positive_rate,
    'Positive' as expected_prediction
FROM DU_raw
WHERE `pickUpHourOfDay=VERYLATE` = 0 AND `zone_demand_popularity=POPULARITY_INDEX_5` = 0 AND `pickUpHourOfDay=LATENIGHT` = 1 AND `dayType=NORMAL_WEEKDAY` = 0 AND `zone=217` = 1 AND `dayType=FRIDAY` = 0;


--------------------------------------------------------------------------------


-- Rule 5: pickUpHourOfDay=VERYLATE is FALSE AND zone_demand_popularity=POPULARITY_INDEX_5 is FALSE AND pickUpHourOfDay=LATENIGHT is TRUE AND dayType=NORMAL_WEEKDAY is FALSE AND zone=217 is TRUE AND dayType=FRIDAY is TRUE
SELECT
    COUNT(*) as actual_samples,
    24 as expected_samples,
    ROUND(AVG(CASE WHEN target = 1 THEN 1.0 ELSE 0.0 END), 4) as actual_positive_rate,
    0.9167 as expected_positive_rate,
    'Positive' as expected_prediction
FROM DU_raw
WHERE `pickUpHourOfDay=VERYLATE` = 0 AND `zone_demand_popularity=POPULARITY_INDEX_5` = 0 AND `pickUpHourOfDay=LATENIGHT` = 1 AND `dayType=NORMAL_WEEKDAY` = 0 AND `zone=217` = 1 AND `dayType=FRIDAY` = 1;


--------------------------------------------------------------------------------


-- Rule 6: pickUpHourOfDay=VERYLATE is FALSE AND zone_demand_popularity=POPULARITY_INDEX_5 is FALSE AND pickUpHourOfDay=LATENIGHT is TRUE AND dayType=NORMAL_WEEKDAY is TRUE AND zone=500 is FALSE AND zone=75 is FALSE
SELECT
    COUNT(*) as actual_samples,
    690 as expected_samples,
    ROUND(AVG(CASE WHEN target = 1 THEN 1.0 ELSE 0.0 END), 4) as actual_positive_rate,
    0.9203 as expected_positive_rate,
    'Positive' as expected_prediction
FROM DU_raw
WHERE `pickUpHourOfDay=VERYLATE` = 0 AND `zone_demand_popularity=POPULARITY_INDEX_5` = 0 AND `pickUpHourOfDay=LATENIGHT` = 1 AND `dayType=NORMAL_WEEKDAY` = 1 AND `zone=500` = 0 AND `zone=75` = 0;


--------------------------------------------------------------------------------


-- Rule 7: pickUpHourOfDay=VERYLATE is FALSE AND zone_demand_popularity=POPULARITY_INDEX_5 is FALSE AND pickUpHourOfDay=LATENIGHT is TRUE AND dayType=NORMAL_WEEKDAY is TRUE AND zone=500 is FALSE AND zone=75 is TRUE
SELECT
    COUNT(*) as actual_samples,
    4 as expected_samples,
    ROUND(AVG(CASE WHEN target = 1 THEN 1.0 ELSE 0.0 END), 4) as actual_positive_rate,
    0.0 as expected_positive_rate,
    'Negative' as expected_prediction
FROM DU_raw
WHERE `pickUpHourOfDay=VERYLATE` = 0 AND `zone_demand_popularity=POPULARITY_INDEX_5` = 0 AND `pickUpHourOfDay=LATENIGHT` = 1 AND `dayType=NORMAL_WEEKDAY` = 1 AND `zone=500` = 0 AND `zone=75` = 1;


--------------------------------------------------------------------------------


-- Rule 8: pickUpHourOfDay=VERYLATE is FALSE AND zone_demand_popularity=POPULARITY_INDEX_5 is FALSE AND pickUpHourOfDay=LATENIGHT is TRUE AND dayType=NORMAL_WEEKDAY is TRUE AND zone=500 is TRUE
SELECT
    COUNT(*) as actual_samples,
    8 as expected_samples,
    ROUND(AVG(CASE WHEN target = 1 THEN 1.0 ELSE 0.0 END), 4) as actual_positive_rate,
    0.125 as expected_positive_rate,
    'Negative' as expected_prediction
FROM DU_raw
WHERE `pickUpHourOfDay=VERYLATE` = 0 AND `zone_demand_popularity=POPULARITY_INDEX_5` = 0 AND `pickUpHourOfDay=LATENIGHT` = 1 AND `dayType=NORMAL_WEEKDAY` = 1 AND `zone=500` = 1;


--------------------------------------------------------------------------------


-- Rule 9: pickUpHourOfDay=VERYLATE is FALSE AND zone_demand_popularity=POPULARITY_INDEX_5 is TRUE AND pickUpHourOfDay=LATENIGHT is FALSE AND city=Pune is FALSE AND zone=67 is FALSE AND city=Mumbai is FALSE
SELECT
    COUNT(*) as actual_samples,
    1471 as expected_samples,
    ROUND(AVG(CASE WHEN target = 1 THEN 1.0 ELSE 0.0 END), 4) as actual_positive_rate,
    0.8872 as expected_positive_rate,
    'Positive' as expected_prediction
FROM DU_raw
WHERE `pickUpHourOfDay=VERYLATE` = 0 AND `zone_demand_popularity=POPULARITY_INDEX_5` = 1 AND `pickUpHourOfDay=LATENIGHT` = 0 AND `city=Pune` = 0 AND `zone=67` = 0 AND `city=Mumbai` = 0;


--------------------------------------------------------------------------------


-- Rule 10: pickUpHourOfDay=VERYLATE is FALSE AND zone_demand_popularity=POPULARITY_INDEX_5 is TRUE AND pickUpHourOfDay=LATENIGHT is FALSE AND city=Pune is FALSE AND zone=67 is FALSE AND city=Mumbai is TRUE
SELECT
    COUNT(*) as actual_samples,
    586 as expected_samples,
    ROUND(AVG(CASE WHEN target = 1 THEN 1.0 ELSE 0.0 END), 4) as actual_positive_rate,
    0.7765 as expected_positive_rate,
    'Positive' as expected_prediction
FROM DU_raw
WHERE `pickUpHourOfDay=VERYLATE` = 0 AND `zone_demand_popularity=POPULARITY_INDEX_5` = 1 AND `pickUpHourOfDay=LATENIGHT` = 0 AND `city=Pune` = 0 AND `zone=67` = 0 AND `city=Mumbai` = 1;


--------------------------------------------------------------------------------


-- Rule 11: pickUpHourOfDay=VERYLATE is FALSE AND zone_demand_popularity=POPULARITY_INDEX_5 is TRUE AND pickUpHourOfDay=LATENIGHT is FALSE AND city=Pune is FALSE AND zone=67 is TRUE
SELECT
    COUNT(*) as actual_samples,
    18 as expected_samples,
    ROUND(AVG(CASE WHEN target = 1 THEN 1.0 ELSE 0.0 END), 4) as actual_positive_rate,
    0.2778 as expected_positive_rate,
    'Negative' as expected_prediction
FROM DU_raw
WHERE `pickUpHourOfDay=VERYLATE` = 0 AND `zone_demand_popularity=POPULARITY_INDEX_5` = 1 AND `pickUpHourOfDay=LATENIGHT` = 0 AND `city=Pune` = 0 AND `zone=67` = 1;


--------------------------------------------------------------------------------


-- Rule 12: pickUpHourOfDay=VERYLATE is FALSE AND zone_demand_popularity=POPULARITY_INDEX_5 is TRUE AND pickUpHourOfDay=LATENIGHT is FALSE AND city=Pune is TRUE AND zone=329 is FALSE AND booking_type=outstation is FALSE
SELECT
    COUNT(*) as actual_samples,
    284 as expected_samples,
    ROUND(AVG(CASE WHEN target = 1 THEN 1.0 ELSE 0.0 END), 4) as actual_positive_rate,
    0.6901 as expected_positive_rate,
    'Positive' as expected_prediction
FROM DU_raw
WHERE `pickUpHourOfDay=VERYLATE` = 0 AND `zone_demand_popularity=POPULARITY_INDEX_5` = 1 AND `pickUpHourOfDay=LATENIGHT` = 0 AND `city=Pune` = 1 AND `zone=329` = 0 AND `booking_type=outstation` = 0;


--------------------------------------------------------------------------------


-- Rule 13: pickUpHourOfDay=VERYLATE is FALSE AND zone_demand_popularity=POPULARITY_INDEX_5 is TRUE AND pickUpHourOfDay=LATENIGHT is FALSE AND city=Pune is TRUE AND zone=329 is FALSE AND booking_type=outstation is TRUE
SELECT
    COUNT(*) as actual_samples,
    56 as expected_samples,
    ROUND(AVG(CASE WHEN target = 1 THEN 1.0 ELSE 0.0 END), 4) as actual_positive_rate,
    0.9464 as expected_positive_rate,
    'Positive' as expected_prediction
FROM DU_raw
WHERE `pickUpHourOfDay=VERYLATE` = 0 AND `zone_demand_popularity=POPULARITY_INDEX_5` = 1 AND `pickUpHourOfDay=LATENIGHT` = 0 AND `city=Pune` = 1 AND `zone=329` = 0 AND `booking_type=outstation` = 1;


--------------------------------------------------------------------------------


-- Rule 14: pickUpHourOfDay=VERYLATE is FALSE AND zone_demand_popularity=POPULARITY_INDEX_5 is TRUE AND pickUpHourOfDay=LATENIGHT is FALSE AND city=Pune is TRUE AND zone=329 is TRUE
SELECT
    COUNT(*) as actual_samples,
    13 as expected_samples,
    ROUND(AVG(CASE WHEN target = 1 THEN 1.0 ELSE 0.0 END), 4) as actual_positive_rate,
    0.2308 as expected_positive_rate,
    'Negative' as expected_prediction
FROM DU_raw
WHERE `pickUpHourOfDay=VERYLATE` = 0 AND `zone_demand_popularity=POPULARITY_INDEX_5` = 1 AND `pickUpHourOfDay=LATENIGHT` = 0 AND `city=Pune` = 1 AND `zone=329` = 1;


--------------------------------------------------------------------------------


-- Rule 15: pickUpHourOfDay=VERYLATE is FALSE AND zone_demand_popularity=POPULARITY_INDEX_5 is TRUE AND pickUpHourOfDay=LATENIGHT is TRUE AND city=Mumbai is FALSE AND zone=339 is FALSE AND dayType=WEEKEND is FALSE
SELECT
    COUNT(*) as actual_samples,
    55 as expected_samples,
    ROUND(AVG(CASE WHEN target = 1 THEN 1.0 ELSE 0.0 END), 4) as actual_positive_rate,
    0.5273 as expected_positive_rate,
    'Positive' as expected_prediction
FROM DU_raw
WHERE `pickUpHourOfDay=VERYLATE` = 0 AND `zone_demand_popularity=POPULARITY_INDEX_5` = 1 AND `pickUpHourOfDay=LATENIGHT` = 1 AND `city=Mumbai` = 0 AND `zone=339` = 0 AND `dayType=WEEKEND` = 0;


--------------------------------------------------------------------------------


-- Rule 16: pickUpHourOfDay=VERYLATE is FALSE AND zone_demand_popularity=POPULARITY_INDEX_5 is TRUE AND pickUpHourOfDay=LATENIGHT is TRUE AND city=Mumbai is FALSE AND zone=339 is FALSE AND dayType=WEEKEND is TRUE
SELECT
    COUNT(*) as actual_samples,
    24 as expected_samples,
    ROUND(AVG(CASE WHEN target = 1 THEN 1.0 ELSE 0.0 END), 4) as actual_positive_rate,
    0.3333 as expected_positive_rate,
    'Negative' as expected_prediction
FROM DU_raw
WHERE `pickUpHourOfDay=VERYLATE` = 0 AND `zone_demand_popularity=POPULARITY_INDEX_5` = 1 AND `pickUpHourOfDay=LATENIGHT` = 1 AND `city=Mumbai` = 0 AND `zone=339` = 0 AND `dayType=WEEKEND` = 1;


--------------------------------------------------------------------------------


-- Rule 17: pickUpHourOfDay=VERYLATE is FALSE AND zone_demand_popularity=POPULARITY_INDEX_5 is TRUE AND pickUpHourOfDay=LATENIGHT is TRUE AND city=Mumbai is FALSE AND zone=339 is TRUE
SELECT
    COUNT(*) as actual_samples,
    6 as expected_samples,
    ROUND(AVG(CASE WHEN target = 1 THEN 1.0 ELSE 0.0 END), 4) as actual_positive_rate,
    1.0 as expected_positive_rate,
    'Positive' as expected_prediction
FROM DU_raw
WHERE `pickUpHourOfDay=VERYLATE` = 0 AND `zone_demand_popularity=POPULARITY_INDEX_5` = 1 AND `pickUpHourOfDay=LATENIGHT` = 1 AND `city=Mumbai` = 0 AND `zone=339` = 1;


--------------------------------------------------------------------------------


-- Rule 18: pickUpHourOfDay=VERYLATE is FALSE AND zone_demand_popularity=POPULARITY_INDEX_5 is TRUE AND pickUpHourOfDay=LATENIGHT is TRUE AND city=Mumbai is TRUE AND zone=401 is FALSE AND zone=467 is FALSE
SELECT
    COUNT(*) as actual_samples,
    50 as expected_samples,
    ROUND(AVG(CASE WHEN target = 1 THEN 1.0 ELSE 0.0 END), 4) as actual_positive_rate,
    0.76 as expected_positive_rate,
    'Positive' as expected_prediction
FROM DU_raw
WHERE `pickUpHourOfDay=VERYLATE` = 0 AND `zone_demand_popularity=POPULARITY_INDEX_5` = 1 AND `pickUpHourOfDay=LATENIGHT` = 1 AND `city=Mumbai` = 1 AND `zone=401` = 0 AND `zone=467` = 0;


--------------------------------------------------------------------------------


-- Rule 19: pickUpHourOfDay=VERYLATE is FALSE AND zone_demand_popularity=POPULARITY_INDEX_5 is TRUE AND pickUpHourOfDay=LATENIGHT is TRUE AND city=Mumbai is TRUE AND zone=401 is FALSE AND zone=467 is TRUE
SELECT
    COUNT(*) as actual_samples,
    2 as expected_samples,
    ROUND(AVG(CASE WHEN target = 1 THEN 1.0 ELSE 0.0 END), 4) as actual_positive_rate,
    0.0 as expected_positive_rate,
    'Negative' as expected_prediction
FROM DU_raw
WHERE `pickUpHourOfDay=VERYLATE` = 0 AND `zone_demand_popularity=POPULARITY_INDEX_5` = 1 AND `pickUpHourOfDay=LATENIGHT` = 1 AND `city=Mumbai` = 1 AND `zone=401` = 0 AND `zone=467` = 1;


--------------------------------------------------------------------------------


-- Rule 20: pickUpHourOfDay=VERYLATE is FALSE AND zone_demand_popularity=POPULARITY_INDEX_5 is TRUE AND pickUpHourOfDay=LATENIGHT is TRUE AND city=Mumbai is TRUE AND zone=401 is TRUE
SELECT
    COUNT(*) as actual_samples,
    2 as expected_samples,
    ROUND(AVG(CASE WHEN target = 1 THEN 1.0 ELSE 0.0 END), 4) as actual_positive_rate,
    0.0 as expected_positive_rate,
    'Negative' as expected_prediction
FROM DU_raw
WHERE `pickUpHourOfDay=VERYLATE` = 0 AND `zone_demand_popularity=POPULARITY_INDEX_5` = 1 AND `pickUpHourOfDay=LATENIGHT` = 1 AND `city=Mumbai` = 1 AND `zone=401` = 1;


--------------------------------------------------------------------------------


-- Rule 21: pickUpHourOfDay=VERYLATE is TRUE AND city=Delhi NCR is FALSE AND dayType=WEEKEND is FALSE AND city=Pune is FALSE AND zone=399 is FALSE AND city=Hyderabad is FALSE
SELECT
    COUNT(*) as actual_samples,
    754 as expected_samples,
    ROUND(AVG(CASE WHEN target = 1 THEN 1.0 ELSE 0.0 END), 4) as actual_positive_rate,
    0.9151 as expected_positive_rate,
    'Positive' as expected_prediction
FROM DU_raw
WHERE `pickUpHourOfDay=VERYLATE` = 1 AND `city=Delhi NCR` = 0 AND `dayType=WEEKEND` = 0 AND `city=Pune` = 0 AND `zone=399` = 0 AND `city=Hyderabad` = 0;


--------------------------------------------------------------------------------


-- Rule 22: pickUpHourOfDay=VERYLATE is TRUE AND city=Delhi NCR is FALSE AND dayType=WEEKEND is FALSE AND city=Pune is FALSE AND zone=399 is FALSE AND city=Hyderabad is TRUE
SELECT
    COUNT(*) as actual_samples,
    93 as expected_samples,
    ROUND(AVG(CASE WHEN target = 1 THEN 1.0 ELSE 0.0 END), 4) as actual_positive_rate,
    0.7527 as expected_positive_rate,
    'Positive' as expected_prediction
FROM DU_raw
WHERE `pickUpHourOfDay=VERYLATE` = 1 AND `city=Delhi NCR` = 0 AND `dayType=WEEKEND` = 0 AND `city=Pune` = 0 AND `zone=399` = 0 AND `city=Hyderabad` = 1;


--------------------------------------------------------------------------------


-- Rule 23: pickUpHourOfDay=VERYLATE is TRUE AND city=Delhi NCR is FALSE AND dayType=WEEKEND is FALSE AND city=Pune is FALSE AND zone=399 is TRUE
SELECT
    COUNT(*) as actual_samples,
    7 as expected_samples,
    ROUND(AVG(CASE WHEN target = 1 THEN 1.0 ELSE 0.0 END), 4) as actual_positive_rate,
    0.2857 as expected_positive_rate,
    'Negative' as expected_prediction
FROM DU_raw
WHERE `pickUpHourOfDay=VERYLATE` = 1 AND `city=Delhi NCR` = 0 AND `dayType=WEEKEND` = 0 AND `city=Pune` = 0 AND `zone=399` = 1;


--------------------------------------------------------------------------------


-- Rule 24: pickUpHourOfDay=VERYLATE is TRUE AND city=Delhi NCR is FALSE AND dayType=WEEKEND is FALSE AND city=Pune is TRUE
SELECT
    COUNT(*) as actual_samples,
    14 as expected_samples,
    ROUND(AVG(CASE WHEN target = 1 THEN 1.0 ELSE 0.0 END), 4) as actual_positive_rate,
    0.3571 as expected_positive_rate,
    'Negative' as expected_prediction
FROM DU_raw
WHERE `pickUpHourOfDay=VERYLATE` = 1 AND `city=Delhi NCR` = 0 AND `dayType=WEEKEND` = 0 AND `city=Pune` = 1;


--------------------------------------------------------------------------------


-- Rule 25: pickUpHourOfDay=VERYLATE is TRUE AND city=Delhi NCR is FALSE AND dayType=WEEKEND is TRUE AND zone=399 is FALSE AND city=Chennai is FALSE AND zone=216 is FALSE
SELECT
    COUNT(*) as actual_samples,
    1127 as expected_samples,
    ROUND(AVG(CASE WHEN target = 1 THEN 1.0 ELSE 0.0 END), 4) as actual_positive_rate,
    0.7285 as expected_positive_rate,
    'Positive' as expected_prediction
FROM DU_raw
WHERE `pickUpHourOfDay=VERYLATE` = 1 AND `city=Delhi NCR` = 0 AND `dayType=WEEKEND` = 1 AND `zone=399` = 0 AND `city=Chennai` = 0 AND `zone=216` = 0;


--------------------------------------------------------------------------------


-- Rule 26: pickUpHourOfDay=VERYLATE is TRUE AND city=Delhi NCR is FALSE AND dayType=WEEKEND is TRUE AND zone=399 is FALSE AND city=Chennai is FALSE AND zone=216 is TRUE
SELECT
    COUNT(*) as actual_samples,
    83 as expected_samples,
    ROUND(AVG(CASE WHEN target = 1 THEN 1.0 ELSE 0.0 END), 4) as actual_positive_rate,
    0.9277 as expected_positive_rate,
    'Positive' as expected_prediction
FROM DU_raw
WHERE `pickUpHourOfDay=VERYLATE` = 1 AND `city=Delhi NCR` = 0 AND `dayType=WEEKEND` = 1 AND `zone=399` = 0 AND `city=Chennai` = 0 AND `zone=216` = 1;


--------------------------------------------------------------------------------


-- Rule 27: pickUpHourOfDay=VERYLATE is TRUE AND city=Delhi NCR is FALSE AND dayType=WEEKEND is TRUE AND zone=399 is FALSE AND city=Chennai is TRUE AND zone=482 is FALSE
SELECT
    COUNT(*) as actual_samples,
    64 as expected_samples,
    ROUND(AVG(CASE WHEN target = 1 THEN 1.0 ELSE 0.0 END), 4) as actual_positive_rate,
    0.9688 as expected_positive_rate,
    'Positive' as expected_prediction
FROM DU_raw
WHERE `pickUpHourOfDay=VERYLATE` = 1 AND `city=Delhi NCR` = 0 AND `dayType=WEEKEND` = 1 AND `zone=399` = 0 AND `city=Chennai` = 1 AND `zone=482` = 0;


--------------------------------------------------------------------------------


-- Rule 28: pickUpHourOfDay=VERYLATE is TRUE AND city=Delhi NCR is FALSE AND dayType=WEEKEND is TRUE AND zone=399 is FALSE AND city=Chennai is TRUE AND zone=482 is TRUE
SELECT
    COUNT(*) as actual_samples,
    2 as expected_samples,
    ROUND(AVG(CASE WHEN target = 1 THEN 1.0 ELSE 0.0 END), 4) as actual_positive_rate,
    0.5 as expected_positive_rate,
    'Positive' as expected_prediction
FROM DU_raw
WHERE `pickUpHourOfDay=VERYLATE` = 1 AND `city=Delhi NCR` = 0 AND `dayType=WEEKEND` = 1 AND `zone=399` = 0 AND `city=Chennai` = 1 AND `zone=482` = 1;


--------------------------------------------------------------------------------


-- Rule 29: pickUpHourOfDay=VERYLATE is TRUE AND city=Delhi NCR is FALSE AND dayType=WEEKEND is TRUE AND zone=399 is TRUE
SELECT
    COUNT(*) as actual_samples,
    18 as expected_samples,
    ROUND(AVG(CASE WHEN target = 1 THEN 1.0 ELSE 0.0 END), 4) as actual_positive_rate,
    0.1667 as expected_positive_rate,
    'Negative' as expected_prediction
FROM DU_raw
WHERE `pickUpHourOfDay=VERYLATE` = 1 AND `city=Delhi NCR` = 0 AND `dayType=WEEKEND` = 1 AND `zone=399` = 1;


--------------------------------------------------------------------------------


-- Rule 30: pickUpHourOfDay=VERYLATE is TRUE AND city=Delhi NCR is TRUE AND sla=Immediate is FALSE AND zone=346 is FALSE AND zone=360 is FALSE AND zone=75 is FALSE
SELECT
    COUNT(*) as actual_samples,
    141 as expected_samples,
    ROUND(AVG(CASE WHEN target = 1 THEN 1.0 ELSE 0.0 END), 4) as actual_positive_rate,
    0.4255 as expected_positive_rate,
    'Negative' as expected_prediction
FROM DU_raw
WHERE `pickUpHourOfDay=VERYLATE` = 1 AND `city=Delhi NCR` = 1 AND `sla=Immediate` = 0 AND `zone=346` = 0 AND `zone=360` = 0 AND `zone=75` = 0;


--------------------------------------------------------------------------------


-- Rule 31: pickUpHourOfDay=VERYLATE is TRUE AND city=Delhi NCR is TRUE AND sla=Immediate is FALSE AND zone=346 is FALSE AND zone=360 is FALSE AND zone=75 is TRUE
SELECT
    COUNT(*) as actual_samples,
    11 as expected_samples,
    ROUND(AVG(CASE WHEN target = 1 THEN 1.0 ELSE 0.0 END), 4) as actual_positive_rate,
    0.0909 as expected_positive_rate,
    'Negative' as expected_prediction
FROM DU_raw
WHERE `pickUpHourOfDay=VERYLATE` = 1 AND `city=Delhi NCR` = 1 AND `sla=Immediate` = 0 AND `zone=346` = 0 AND `zone=360` = 0 AND `zone=75` = 1;


--------------------------------------------------------------------------------


-- Rule 32: pickUpHourOfDay=VERYLATE is TRUE AND city=Delhi NCR is TRUE AND sla=Immediate is FALSE AND zone=346 is FALSE AND zone=360 is TRUE
SELECT
    COUNT(*) as actual_samples,
    4 as expected_samples,
    ROUND(AVG(CASE WHEN target = 1 THEN 1.0 ELSE 0.0 END), 4) as actual_positive_rate,
    1.0 as expected_positive_rate,
    'Positive' as expected_prediction
FROM DU_raw
WHERE `pickUpHourOfDay=VERYLATE` = 1 AND `city=Delhi NCR` = 1 AND `sla=Immediate` = 0 AND `zone=346` = 0 AND `zone=360` = 1;


--------------------------------------------------------------------------------


-- Rule 33: pickUpHourOfDay=VERYLATE is TRUE AND city=Delhi NCR is TRUE AND sla=Immediate is FALSE AND zone=346 is TRUE
SELECT
    COUNT(*) as actual_samples,
    5 as expected_samples,
    ROUND(AVG(CASE WHEN target = 1 THEN 1.0 ELSE 0.0 END), 4) as actual_positive_rate,
    1.0 as expected_positive_rate,
    'Positive' as expected_prediction
FROM DU_raw
WHERE `pickUpHourOfDay=VERYLATE` = 1 AND `city=Delhi NCR` = 1 AND `sla=Immediate` = 0 AND `zone=346` = 1;


--------------------------------------------------------------------------------


-- Rule 34: pickUpHourOfDay=VERYLATE is TRUE AND city=Delhi NCR is TRUE AND sla=Immediate is TRUE
SELECT
    COUNT(*) as actual_samples,
    7 as expected_samples,
    ROUND(AVG(CASE WHEN target = 1 THEN 1.0 ELSE 0.0 END), 4) as actual_positive_rate,
    1.0 as expected_positive_rate,
    'Positive' as expected_prediction
FROM DU_raw
WHERE `pickUpHourOfDay=VERYLATE` = 1 AND `city=Delhi NCR` = 1 AND `sla=Immediate` = 1;

