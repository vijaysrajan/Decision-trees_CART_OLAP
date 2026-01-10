-- Decision Tree Rules as SQL Queries
-- Generated from: output/du_model_log_loss_enhanced.json
-- Total rules: 1

-- Rule 0: All samples (no conditions)
-- Prediction: Good_DU (confidence: 0.872)
-- Samples: 20343
SELECT 'Good_DU' as prediction, 0.8718 as confidence
FROM dataset WHERE 1=1;

