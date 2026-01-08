# CART Decision Tree for Aggregate OLAP Data

A professional implementation of CART (Classification and Regression Trees) algorithm designed specifically for aggregate OLAP cube data with binary classification.

## Overview

This library provides a sklearn-compatible decision tree classifier that works directly with pre-aggregated data containing good/bad counts, eliminating the need to access raw individual records. This approach is ideal for:

- Privacy-preserving machine learning on aggregate data
- Building models from OLAP cubes and data warehouses
- High-performance training on pre-summarized datasets
- Distributed processing scenarios (Spark-ready design)

## Key Features

- **Direct Aggregate Processing**: Train on count data without raw records
- **Sklearn-like Interface**: Standard `fit()`, `predict()`, `predict_proba()` interface (mimics sklearn without using it)
- **High Performance**: O(aggregate_rows) complexity instead of O(raw_data_rows)
- **Exact Results**: No approximation within aggregation boundaries
- **Flexible Input**: Works with any categorical features and count columns

## Input Data Format

The algorithm expects CSV data with:
- **Feature columns**: Categorical features (any number)
- **Good count column**: Count of positive class instances
- **Bad count column**: Count of negative class instances

Example:
```csv
source,city,zone,dayType,DU_Bad_Count,DU_good_cnt,total_cnt
ios,Bangalore,219,WEEKEND,43,71,114
android,Mumbai,399,NORMAL_WEEKDAY,19,50,69
```

## Quick Start

```python
import pandas as pd
from cart_olap import AggregateCART

# Load aggregate data
df = pd.read_csv('your_aggregate_data.csv')

# Initialize classifier
cart = AggregateCART(
    max_depth=10,
    min_samples_leaf=5,
    min_impurity_decrease=0.01
)

# Train on aggregate data
feature_cols = ['source', 'city', 'zone', 'dayType']
cart.fit(df, feature_cols, 'DU_good_cnt', 'DU_Bad_Count')

# Predict on individual samples
new_sample = pd.DataFrame({
    'source': ['ios'],
    'city': ['Delhi'],
    'zone': ['123'],
    'dayType': ['WEEKEND']
})

prediction = cart.predict(new_sample)
probabilities = cart.predict_proba(new_sample)
```

## Installation

```bash
git clone <repository-url>
cd cart-olap
pip install -r requirements.txt
pip install -e .
```

## Project Structure

```
cart-olap/
├── cart_olap/
│   ├── __init__.py
│   ├── aggregate_cart.py      # Main CART implementation
│   ├── tree_nodes.py          # Tree node data structures
│   └── utils.py               # Utility functions
├── tests/
│   ├── test_aggregate_cart.py
│   ├── test_tree_nodes.py
│   └── test_data/
├── examples/
│   ├── basic_usage.py
│   └── DUAggregateData.csv
├── docs/
│   ├── api_reference.md
│   └── design_document.md
├── requirements.txt
├── setup.py
└── README.md
```

## Requirements

- Python 3.8+
- pandas >= 1.3.0
- numpy >= 1.20.0

## License

MIT License

## Contributing

1. Fork the repository
2. Create a feature branch
3. Add comprehensive tests
4. Submit a pull request

## Acknowledgments

This implementation is inspired by:
- Scikit-learn's DecisionTreeClassifier interface (but implemented from scratch)
- Research on privacy-preserving machine learning with aggregate data
- OLAP cube processing techniques
- Pure Python implementation with no sklearn dependencies