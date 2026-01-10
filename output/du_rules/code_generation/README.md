# Generated CART-OLAP Decision Rules Summary
**Source Model**: CART-OLAP_du_model_cli

## Rule Statistics
- **Total Rules**: 34
- **Positive Predictions**: 32 (94.1%)
- **Negative Predictions**: 2 (5.9%)
- **Average Conditions per Rule**: 5.4
- **Maximum Conditions**: 6
- **High Confidence Rules** (>80%): 17 (50.0%)

## Model Statistics
- **Total Training Samples**: 20,343
- **Average Rule Confidence**: 0.773
- **Feature Count**: 354
- **Classes**: [0, 1]

## Top 5 Rules by Sample Count
| Rule | Prediction | Confidence | Samples | Good/Bad | Conditions |
|------|------------|------------|---------|----------|------------|
| 1 | POSITIVE | 0.904 | 12794 | 11560/1234 | 6 conditions |
| 2 | POSITIVE | 0.890 | 1397 | 1244/153 | 6 conditions |
| 3 | POSITIVE | 0.744 | 996 | 741/255 | 6 conditions |
| 4 | POSITIVE | 0.990 | 697 | 690/7 | 6 conditions |
| 5 | POSITIVE | 0.720 | 644 | 464/180 | 6 conditions |

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