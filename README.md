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

- **Multiple Split Criteria**: Supports gini, entropy, and log_loss criteria
- **One-Hot Encoding**: Converts categorical features to binary (`feature=value` format)
- **Sklearn Compatible**: `.fit()`, `.predict()`, `.predict_proba()` methods
- **JSON Persistence**: Complete save/load functionality
- **Binary Logic**: True/False splits (`feature=value` == True vs False)
- **Aggregate Data**: Works directly on OLAP cube data (good/bad counts)
- **Professional CLI**: Command line tools for common workflows

## 🔀 Split Criteria

CART-OLAP supports three split criteria for optimal tree construction:

### Gini Impurity (Default)
- **Use case**: General-purpose, fast computation
- **Formula**: `1 - Σ(p_i²)` where p_i is probability of class i
- **Best for**: Balanced datasets, when speed is important

### Entropy (Information Gain)
- **Use case**: When you want to maximize information gain
- **Formula**: `-Σ(p_i * log₂(p_i))`
- **Best for**: Feature selection, interpretable splits

### Log Loss (Cross-entropy)
- **Use case**: When optimizing for probability calibration
- **Formula**: `-Σ(p_i * ln(p_i))`
- **Best for**: When prediction probabilities are crucial

### Building Models with Different Criteria

```bash
# Build with gini (default)
python build_du_model_cli.py

# Build with entropy
python build_du_model_cli.py --criterion entropy

# Build with log_loss
python build_du_model_cli.py --criterion log_loss

# Build all criteria for comparison
python build_du_model_cli.py --all
```

## 📖 Usage Examples

### Python API - Different Criteria

```python
from cart_olap import AggregateCART
import pandas as pd

# Load data
df = pd.read_csv('output/DUAggregateData.csv')
features = ['source', 'city', 'pickUpHourOfDay']

# Train models with different criteria
models = {}

for criterion in ['gini', 'entropy', 'log_loss']:
    print(f"Training {criterion} model...")
    cart = AggregateCART(
        criterion=criterion,
        max_depth=6,
        min_samples_leaf=20,
        random_state=42
    )
    cart.fit(df, features, 'DU_good_cnt', 'DU_Bad_Count')
    models[criterion] = cart

# Compare model structures
for criterion, model in models.items():
    print(f"{criterion.upper()} Model:")
    print(f"  - Tree depth: {model.get_depth()}")
    print(f"  - Number of leaves: {model.get_n_leaves()}")

# Make predictions with different models
sample = pd.DataFrame([{
    'source': 'ios',
    'city': 'Bangalore',
    'pickUpHourOfDay': 'VERYLATE'
}])

print("\nPrediction Comparison:")
for criterion, model in models.items():
    prediction = model.predict(sample)[0]  # 0 or 1
    probabilities = model.predict_proba(sample)[0]  # [bad_prob, good_prob]

    print(f"{criterion.upper()}:")
    print(f"  - Prediction: {prediction}")
    print(f"  - Probabilities: [Bad: {probabilities[0]:.3f}, Good: {probabilities[1]:.3f}]")

# Save models with criterion-specific names
for criterion, model in models.items():
    filename = f'output/du_model_{criterion}.json'
    model.save_json(filename)
    print(f"Saved {criterion} model to {filename}")

# Load specific model
entropy_model = AggregateCART.load_json('output/du_model_entropy.json')
print(f"Loaded entropy model criterion: {entropy_model.criterion}")
```

### Command Line - Multiple Criteria
```bash
# Build models with different criteria
python build_du_model_cli.py --criterion gini
python build_du_model_cli.py --criterion entropy
python build_du_model_cli.py --criterion log_loss

# Build all criteria at once
python build_du_model_cli.py --all

# Test specific criterion models
python scripts/load_and_predict.py output/du_model_cli_entropy.json
python scripts/load_and_predict.py output/du_model_cli_log_loss.json

# Run comprehensive tests including criteria tests
python run_tests.py --coverage
```

## 📊 Criteria Comparison Results

Using the DU dataset, different criteria produce models with varying characteristics:

| Criterion | Tree Depth | Leaves | File Size | Use Case |
|-----------|------------|--------|-----------|----------|
| **Gini** | 6 | 34 | 45,722 bytes | General purpose, fastest |
| **Entropy** | 6 | 29 | 40,871 bytes | Feature selection, interpretable |
| **Log Loss** | 6 | 29 | 40,880 bytes | Probability optimization |

### When to Use Each Criterion

**Choose Gini when:**
- You need fast training and prediction
- Working with balanced datasets
- General-purpose classification is sufficient
- Default choice for most applications

**Choose Entropy when:**
- You want maximum information gain at each split
- Feature selection and interpretability are important
- You need to understand which features drive decisions
- Building explanatory models

**Choose Log Loss when:**
- Prediction probabilities must be well-calibrated
- You're using the model for risk assessment
- Probability estimates are fed into other systems
- Working with cost-sensitive applications

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