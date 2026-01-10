# Decision Tree Model Report

**Source Model**: `du_model_cli.json`  
**Generated**: 2026-01-10 13:54:14  

## Model Statistics

- **Total Rules**: 34
- **Total Training Samples**: 20,343
- **Average Confidence**: 0.873
- **Maximum Rule Depth**: 6

### Rule Complexity Distribution

| Depth | Rules | Percentage |
|-------|-------|------------|
| 3 | 1 | 2.9% |
| 4 | 6 | 17.6% |
| 5 | 5 | 14.7% |
| 6 | 22 | 64.7% |

## Generated Code Files

The model has been converted to the following executable formats:

- **Python**: High-level implementation with statistical metadata
- **Java**: Enterprise-ready implementation with type safety
- **C++**: High-performance implementation for production systems

## Usage Example

```python
from du_model_cli_predictor import predict_du_quality

features = {
    "pickUpHourOfDay=VERYLATE": 0,
    "zone_demand_popularity=POPULARITY_INDEX_5": 0,
    "pickUpHourOfDay=LATENIGHT": 0,
}

result = predict_du_quality(features)
print(f"Prediction: {result[\"prediction_label\"]} ({result[\"confidence\"]:.3f})")
```
