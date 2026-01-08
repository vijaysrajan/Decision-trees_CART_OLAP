# JSON Export/Import Guide

## Overview

The AggregateCART implementation now includes full JSON export/import functionality for model persistence and sharing.

## File Locations

### **DUAggregateData.csv**
Available in two locations:
- **Root directory**: `./DUAggregateData.csv`
- **Examples directory**: `./examples/DUAggregateData.csv`

Both contain the same ride-hailing demand-utilization dataset (12,589 rows, 9 categorical features).

### **JSON Export Functionality**
Added to `cart_olap/aggregate_cart.py` with these methods:
- `to_json()` - Export tree to JSON string
- `save_json()` - Save tree to JSON file
- `from_json()` - Load tree from JSON string
- `load_json()` - Load tree from JSON file

## Usage Examples

### **Basic JSON Export**
```python
from cart_olap import AggregateCART
import pandas as pd

# Train model
df = pd.read_csv('DUAggregateData.csv')
cart = AggregateCART(max_depth=6, min_samples_leaf=20)
cart.fit(df, feature_cols, 'DU_good_cnt', 'DU_Bad_Count')

# Export to JSON string
json_str = cart.to_json(indent=2)
print(f"JSON length: {len(json_str)} characters")

# Save to file
cart.save_json('my_tree_model.json')
```

### **Loading from JSON**
```python
# Load from file
loaded_cart = AggregateCART.load_json('my_tree_model.json')

# Verify it works
test_data = pd.DataFrame({
    'source': ['ios'],
    'city': ['Bangalore'],
    'dayType': ['WEEKEND']
    # ... other features
})

predictions = loaded_cart.predict(test_data)
probabilities = loaded_cart.predict_proba(test_data)
```

### **JSON Structure**
```json
{
  "model_info": {
    "type": "AggregateCART",
    "max_depth": 6,
    "min_samples_leaf": 20,
    "min_impurity_decrease": 0.001,
    "n_features": 8,
    "feature_names": ["source", "city", "dayType", ...],
    "classes": [0, 1],
    "tree_depth": 5,
    "n_leaves": 12
  },
  "tree": {
    "type": "internal",
    "feature": "source",
    "split_value": "ios",
    "samples": 50000,
    "impurity": 0.485,
    "good_count": 25000,
    "bad_count": 25000,
    "depth": 0,
    "left": { ... },
    "right": { ... }
  }
}
```

## Example Scripts

### **1. Simple JSON Demo**
Run: `python examples/json_export_example.py`
- Creates sample data
- Trains tree
- Exports to JSON
- Loads and verifies predictions match

### **2. DU Dataset Export**
Run: `python examples/export_du_tree.py`
- Loads DUAggregateData.csv
- Trains optimized tree
- Exports to `DU_tree_model.json`
- Shows JSON structure preview

## JSON Features

### **Complete Model Persistence**
- All hyperparameters saved
- Full tree structure preserved
- Feature names and metadata included
- Exact reconstruction guaranteed

### **Cross-Platform Compatibility**
- Standard JSON format
- Works across Python versions
- Can be loaded in other languages
- Human-readable structure

### **Performance**
- Efficient serialization
- Compact representation
- Fast loading
- Memory efficient

## File Sizes

Typical JSON file sizes for DU dataset:
- **Shallow tree** (depth=3): ~2-5 KB
- **Medium tree** (depth=6): ~10-50 KB
- **Deep tree** (depth=10): ~50-200 KB

Size depends on:
- Tree depth
- Number of features used
- Data complexity
- JSON indentation

## Use Cases

### **Model Deployment**
```python
# Train once
cart.fit(training_data, features, 'good_col', 'bad_col')
cart.save_json('production_model.json')

# Deploy anywhere
production_cart = AggregateCART.load_json('production_model.json')
```

### **Model Sharing**
- Share trained models as JSON files
- Version control model artifacts
- Reproduce exact results
- Compare different model versions

### **A/B Testing**
```python
# Load different model versions
model_a = AggregateCART.load_json('model_v1.json')
model_b = AggregateCART.load_json('model_v2.json')

# Compare predictions
pred_a = model_a.predict(test_data)
pred_b = model_b.predict(test_data)
```

### **Model Analysis**
- Inspect tree structure programmatically
- Extract feature usage statistics
- Analyze decision paths
- Generate model documentation

## Installation & Setup

```bash
# Setup environment
python3 -m venv venv
source venv/bin/activate
pip install pandas numpy

# Run examples
python examples/json_export_example.py
python examples/export_du_tree.py
```

## Best Practices

1. **Version Control**: Include model hyperparameters in filename
   ```
   DU_model_depth6_minleaf20_v1.json
   ```

2. **Validation**: Always test loaded models
   ```python
   # Verify predictions match
   assert (original.predict(test) == loaded.predict(test)).all()
   ```

3. **Documentation**: Include model metadata in JSON
   ```python
   # Add training info to filename or separate metadata file
   ```

4. **Compression**: For large models, compress JSON files
   ```bash
   gzip DU_tree_model.json
   ```

## Troubleshooting

### **Import Errors**
```python
# Ensure cart_olap is installed/importable
import sys
sys.path.append('/path/to/cart-olap')
from cart_olap import AggregateCART
```

### **JSON Validation**
```python
import json
# Validate JSON is well-formed
with open('model.json', 'r') as f:
    data = json.load(f)  # Will raise error if invalid
```

### **Prediction Mismatches**
- Check feature names match exactly
- Verify data types are consistent
- Ensure same feature order

---

The JSON export functionality provides complete model persistence while maintaining the simplicity and performance of the core AggregateCART implementation.