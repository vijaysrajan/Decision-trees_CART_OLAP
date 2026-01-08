# Installation and Quick Start Guide

## Prerequisites

- Python 3.8 or higher
- Git (for cloning repository)

## Installation

### Option 1: Development Installation (Recommended)

```bash
# Clone or navigate to the project directory
cd Decision-trees_CART_OLAP

# Create virtual environment (recommended)
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Install package in development mode
pip install -e .
```

### Option 2: Direct Dependencies

If you just want to use the code without pip installation:

```bash
# Install required packages
pip install pandas>=1.3.0 numpy>=1.20.0 scikit-learn>=1.0.0
```

## Verification

### 1. Basic Functionality Test

Run the basic test without external dependencies:

```bash
python3 test_basic.py
```

You should see:
```
Running basic functionality tests...
==================================================
✓ Gini impurity calculations correct
✓ Information gain calculation correct
✓ Split evaluation logic correct
✓ Prediction logic correct
==================================================
✅ All basic tests passed!
```

### 2. Full Test Suite

After installing pandas/numpy:

```bash
# Run all unit tests
pytest tests/ -v

# Run with coverage
pip install pytest-cov
pytest tests/ --cov=cart_olap --cov-report=html
```

### 3. Example Usage

```bash
# Run the comprehensive example
python examples/basic_usage.py
```

## Quick Start

### Minimal Example

```python
import pandas as pd
from cart_olap import AggregateCART

# Create sample aggregate data
data = pd.DataFrame({
    'city': ['NYC', 'NYC', 'SF', 'SF'],
    'source': ['ios', 'android', 'ios', 'android'],
    'good_count': [100, 80, 60, 40],
    'bad_count': [20, 40, 30, 50]
})

# Train classifier
cart = AggregateCART(max_depth=3, min_samples_leaf=5)
cart.fit(data, ['city', 'source'], 'good_count', 'bad_count')

# Make predictions
new_samples = pd.DataFrame({
    'city': ['NYC', 'SF'],
    'source': ['ios', 'android']
})

predictions = cart.predict(new_samples)
probabilities = cart.predict_proba(new_samples)

print(f"Predictions: {predictions}")
print(f"Probabilities: {probabilities}")
```

## Project Structure

```
cart-olap/
├── cart_olap/              # Main package
│   ├── __init__.py
│   ├── aggregate_cart.py   # Main CART implementation
│   ├── tree_nodes.py       # Tree node classes
│   └── utils.py            # Utility functions
├── tests/                  # Unit tests
│   ├── test_aggregate_cart.py
│   ├── test_tree_nodes.py
│   ├── test_utils.py
│   └── test_data/
├── examples/               # Usage examples
│   ├── basic_usage.py
│   └── DUAggregateData.csv
├── docs/                   # Documentation
│   ├── api_reference.md
│   └── design_document.md
├── requirements.txt        # Dependencies
├── setup.py               # Package setup
├── README.md              # Project overview
└── INSTALLATION.md        # This file
```

## Common Issues

### ImportError: No module named 'pandas'

```bash
pip install pandas numpy
```

### ImportError: No module named 'cart_olap'

Either:
1. Install in development mode: `pip install -e .`
2. Add to Python path: `export PYTHONPATH="${PYTHONPATH}:$(pwd)"`

### Test failures

Ensure all dependencies are installed:
```bash
pip install -r requirements.txt
```

### Permission errors

Use virtual environment or install with `--user` flag:
```bash
pip install --user -r requirements.txt
```

## Development Setup

For contributing to the project:

```bash
# Install development dependencies
pip install -r requirements.txt
pip install -e .[dev]

# Set up pre-commit hooks
pip install pre-commit
pre-commit install

# Run code formatting
black cart_olap/ tests/ examples/
flake8 cart_olap/ tests/

# Type checking
mypy cart_olap/
```

## Performance Tips

1. **Data Size**: Works best with moderate-sized aggregate tables (< 1M rows)
2. **Feature Cardinality**: High cardinality features may create deep trees
3. **Memory**: Peak memory usage ≈ 2-3x aggregate data size
4. **Speed**: Training time scales with O(rows × features × unique_values)

## Next Steps

1. **Read the docs**: Check `docs/api_reference.md` for detailed API
2. **Try examples**: Run `python examples/basic_usage.py`
3. **Experiment**: Use your own aggregate data
4. **Contribute**: See design document for extension points

## Support

- **Issues**: Check common issues above
- **Documentation**: See `docs/` directory
- **Examples**: See `examples/` directory
- **Tests**: Run `pytest tests/ -v` for validation