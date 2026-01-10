# Decision Tree Model Report

**Source Model**: `du_model_log_loss_enhanced.json`  
**Generated**: 2026-01-10 13:54:04  

## Model Statistics

- **Total Rules**: 1
- **Total Training Samples**: 20,343
- **Average Confidence**: 0.872
- **Maximum Rule Depth**: 0

### Rule Complexity Distribution

| Depth | Rules | Percentage |
|-------|-------|------------|
| 0 | 1 | 100.0% |

## Generated Code Files

The model has been converted to the following executable formats:

- **Python**: High-level implementation with statistical metadata
- **Java**: Enterprise-ready implementation with type safety
- **C++**: High-performance implementation for production systems

## Usage Example

```python
from du_model_log_loss_enhanced_predictor import predict_du_quality

features = {
}

result = predict_du_quality(features)
print(f"Prediction: {result[\"prediction_label\"]} ({result[\"confidence\"]:.3f})")
```
