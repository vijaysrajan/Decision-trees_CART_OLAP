# CART Decision Tree for OLAP Aggregate Data

A professional-grade CART (Classification and Regression Trees) implementation for binary classification using aggregate OLAP cube data. Features one-hot encoding, sklearn-compatible interface, and JSON model persistence.

## 📁 Project Structure

```
Decision-trees_CART_OLAP/
├── cart_olap/              # Main code package
│   ├── __init__.py
│   ├── aggregate_cart.py   # Main CART implementation
│   ├── tree_nodes.py      # Tree node classes
│   ├── utils.py           # Utility functions
│   └── setup.py           # Package setup
├── config/                 # Configuration files
│   └── config.yaml        # Default configuration for DUAggregateData.csv
├── output/                 # Model outputs and data
│   ├── DUAggregateData.csv
│   ├── du_model_final.json
│   └── *.json             # Other model outputs
├── scripts/               # Command line scripts
│   ├── build_tree.py      # Build models from CSV + config
│   ├── load_and_predict.py # Load models and make predictions
│   └── compare_trees.py   # Compare with theta sketches
├── tests/                 # Test suite
│   ├── test_*.py          # Unit tests
│   └── test_basic.py      # Basic functionality tests
├── docs/                  # Documentation
│   ├── *.md               # Various documentation files
│   └── examples/          # Usage examples
├── venv/                  # Virtual environment
├── run_tests.py           # Test runner script
└── requirements.txt       # Dependencies
```

## 🚀 Quick Start

### 1. Setup Environment
```bash
# Create and activate virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

### 2. Run Tests
```bash
# Run all tests
python run_tests.py

# Run with verbose output and coverage
python run_tests.py --verbose --coverage
```

### 3. Build a Model
```bash
# Build model from CSV with configuration
python scripts/build_tree.py output/DUAggregateData.csv config/config.yaml

# With custom output file and verbose mode
python scripts/build_tree.py output/DUAggregateData.csv config/config.yaml -o output/my_model.json --verbose

# Print tree structure to console
python scripts/build_tree.py output/DUAggregateData.csv config/config.yaml --print-tree
```

### 4. Load and Use Model
```bash
# Demo loading and prediction
python scripts/load_and_predict.py output/du_model_final.json

# Load specific model
python scripts/load_and_predict.py output/my_model.json
```

## 📊 Configuration

Edit `config/config.yaml` to customize:
- **Features**: List of categorical features to use
- **Target columns**: Good/bad count column names
- **Hyperparameters**: max_depth, min_samples_leaf, etc.

Example configuration:
```yaml
# Features to use for training
features:
  - source                    # ios, android
  - city                      # Bangalore, Delhi NCR, etc.
  - pickUpHourOfDay          # VERYLATE, MORNING, etc.

# Target columns for binary classification
target_good_col: DU_good_cnt
target_bad_col: DU_Bad_Count

# Hyperparameters
hyperparameters:
  max_depth: 6
  min_samples_leaf: 20
  min_impurity_decrease: 0.001
  random_state: 42
```

## 🎯 Key Features

- **One-Hot Encoding**: Converts categorical features to binary (`feature=value` format)
- **Sklearn Compatible**: `.fit()`, `.predict()`, `.predict_proba()` methods
- **JSON Persistence**: Complete save/load functionality
- **Binary Logic**: True/False splits (`feature=value` == True vs False)
- **Aggregate Data**: Works directly on OLAP cube data (good/bad counts)
- **Professional CLI**: Command line tools for common workflows

## 📖 Usage Examples

### Python API
```python
from cart_olap import AggregateCART
import pandas as pd

# Load data
df = pd.read_csv('output/DUAggregateData.csv')
features = ['source', 'city', 'pickUpHourOfDay']

# Train model
cart = AggregateCART(max_depth=6, min_samples_leaf=20)
cart.fit(df, features, 'DU_good_cnt', 'DU_Bad_Count')

# Make predictions
sample = pd.DataFrame([{
    'source': 'ios',
    'city': 'Bangalore',
    'pickUpHourOfDay': 'VERYLATE'
}])

prediction = cart.predict(sample)[0]  # 0 or 1
probabilities = cart.predict_proba(sample)[0]  # [bad_prob, good_prob]

# Save model
cart.save_json('output/my_model.json')

# Load model
loaded_cart = AggregateCART.load_json('output/my_model.json')
```

### Command Line
```bash
# Build and test in one go
python scripts/build_tree.py output/DUAggregateData.csv config/config.yaml -o output/new_model.json --verbose
python scripts/load_and_predict.py output/new_model.json

# Run all tests
python run_tests.py --coverage
```

## 🔧 Development

### Adding New Features
1. Add feature columns to `config/config.yaml`
2. Ensure data includes good/bad count columns
3. Run build_tree.py with updated config

### Testing
- Unit tests: `tests/test_*.py`
- Basic functionality: `tests/test_basic.py`
- Coverage reports: `htmlcov/index.html`

### File Organization
- **Scripts**: `scripts/` directory for command line tools
- **Config**: `config/` directory for YAML configuration files
- **Output**: `output/` directory for models and data files
- **Docs**: `docs/` directory for documentation

## 🎉 Model Performance

The DU model achieves:
- **Tree Depth**: 6 levels
- **Features**: 354 binary features (after one-hot encoding)
- **Root Split**: `pickUpHourOfDay=VERYLATE` (matches theta sketches)
- **Sample Accuracy**:
  - Late night iOS trips: 72.8% confidence for Good DU
  - Morning Android trips: 90.4% confidence for Good DU
  - High demand zones: 77.6% confidence for Good DU

## 📚 Documentation

- `docs/PROJECT_COMPLETE.md` - Project overview and architecture
- `docs/TREE_COMPARISON.md` - Comparison with theta sketches implementation
- `docs/JSON_EXPORT_GUIDE.md` - Model persistence guide
- `docs/ONE_HOT_ENCODING_IMPLEMENTED.md` - One-hot encoding details
- `docs/BINARY_LOGIC_UPDATED.md` - Binary split logic explanation

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Add tests for new functionality
4. Run `python run_tests.py` to ensure all tests pass
5. Submit a pull request

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.