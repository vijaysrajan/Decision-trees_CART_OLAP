# Generated CART-OLAP Decision Rules Summary
**Source Model**: CART-OLAP_test_model

## Rule Statistics
- **Total Rules**: 34
- **Positive Predictions**: 22 (64.7%)
- **Negative Predictions**: 12 (35.3%)
- **Average Conditions per Rule**: 5.4
- **Maximum Conditions**: 6
- **High Confidence Rules** (>80%): 20 (58.8%)

## Model Statistics
- **Total Training Samples**: 20,343
- **Average Rule Confidence**: 0.835
- **Feature Count**: 354
- **Classes**: [0, 1]

## Top 5 Rules by Sample Count
| Rule | Prediction | Confidence | Samples | Good/Bad | Conditions |
|------|------------|------------|---------|----------|------------|
| 1 | POSITIVE | 0.904 | 13808 | 12476/1332 | 3 conditions |
| 2 | POSITIVE | 0.887 | 1471 | 1305/166 | 6 conditions |
| 3 | POSITIVE | 0.728 | 1127 | 821/306 | 6 conditions |
| 4 | POSITIVE | 0.915 | 754 | 690/64 | 6 conditions |
| 5 | POSITIVE | 0.920 | 690 | 635/55 | 6 conditions |

## Usage Instructions

See generated code files for usage examples in Python, Java, and C++.

## Feature Information
Total features: 354

Example features:
- source=B2B Portal
- source=Phone
- source=android
- source=ios
- source=msite
- source=website
- estimated_usage_bins=GT_1_LTE_2_HOURS
- estimated_usage_bins=GT_2_LTE_3_HOURS
- estimated_usage_bins=GT_3_LTE_4_HOURS
- estimated_usage_bins=GT_4_LTE_6_HOURS
- ... and 344 more features