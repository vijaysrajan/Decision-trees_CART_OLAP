# API Reference

## AggregateCART

The main classifier class for building CART decision trees from aggregate OLAP data.

### Class: `AggregateCART`

```python
class AggregateCART(
    max_depth=None,
    min_samples_leaf=1,
    min_impurity_decrease=0.0,
    random_state=None
)
```

#### Parameters

- **max_depth** : int or None, default=None
  - Maximum depth of the tree
  - If None, nodes are expanded until all leaves are pure or contain less than min_samples_leaf samples

- **min_samples_leaf** : int, default=1
  - Minimum number of samples required to be at a leaf node
  - Counts are based on sum of good_count + bad_count

- **min_impurity_decrease** : float, default=0.0
  - Minimum impurity decrease required for a split to happen
  - A split will only be made if it results in impurity decrease >= this threshold

- **random_state** : int or None, default=None
  - Random seed for reproducible results (reserved for future use)

#### Attributes

- **tree_** : TreeNode or LeafNode
  - The root node of the fitted tree

- **feature_names_** : list
  - Names of features used during fitting

- **n_features_** : int
  - Number of features used during fitting

- **classes_** : array
  - Class labels (always [0, 1] for binary classification)

#### Methods

##### `fit(X, feature_cols, good_col, bad_col, total_col=None)`

Build decision tree from aggregate data.

**Parameters:**
- **X** : DataFrame - Input aggregate data
- **feature_cols** : list of str - Feature column names for splitting
- **good_col** : str - Column name containing good class counts
- **bad_col** : str - Column name containing bad class counts
- **total_col** : str, optional - Column name containing total counts for validation

**Returns:**
- **self** : AggregateCART - Fitted classifier

**Example:**
```python
cart = AggregateCART(max_depth=5)
cart.fit(df, ['feature1', 'feature2'], 'good_count', 'bad_count')
```

##### `predict(X)`

Predict classes for samples.

**Parameters:**
- **X** : DataFrame - Input samples with feature columns

**Returns:**
- **predictions** : array of shape (n_samples,) - Predicted class labels (0 or 1)

**Example:**
```python
predictions = cart.predict(test_df)
```

##### `predict_proba(X)`

Predict class probabilities for samples.

**Parameters:**
- **X** : DataFrame - Input samples with feature columns

**Returns:**
- **probabilities** : array of shape (n_samples, 2) - Predicted class probabilities

**Example:**
```python
probabilities = cart.predict_proba(test_df)
# Column 0 = P(bad class), Column 1 = P(good class)
```

##### `print_tree()`

Print the tree structure for debugging and visualization.

**Example:**
```python
cart.print_tree()
```

##### `get_depth()`

Get the depth of the fitted tree.

**Returns:**
- **depth** : int - Maximum depth of the tree

##### `get_n_leaves()`

Get the number of leaves in the fitted tree.

**Returns:**
- **n_leaves** : int - Number of leaf nodes

---

## Tree Nodes

### Class: `TreeNode`

Internal tree node representing a decision point.

#### Attributes

- **feature** : str - Feature name to split on
- **split_value** : Any - Value used for binary split (feature == split_value)
- **left** : TreeNode or LeafNode - Left child (feature != split_value)
- **right** : TreeNode or LeafNode - Right child (feature == split_value)
- **samples** : int - Total number of samples in this node
- **impurity** : float - Gini impurity of this node
- **good_count** : int - Good class samples in this node
- **bad_count** : int - Bad class samples in this node
- **depth** : int - Depth of this node in the tree

#### Methods

##### `predict_sample(sample)`

Predict class for a single sample by traversing the tree.

##### `predict_proba_sample(sample)`

Predict class probabilities for a single sample.

##### `get_info()`

Get node information dictionary for debugging.

### Class: `LeafNode`

Leaf tree node representing a final prediction.

#### Attributes

- **prediction** : int - Predicted class (0 or 1)
- **class_probabilities** : tuple - (prob_bad, prob_good)
- **samples** : int - Total samples in this leaf
- **impurity** : float - Gini impurity of this leaf
- **good_count** : int - Good class samples in this leaf
- **bad_count** : int - Bad class samples in this leaf
- **depth** : int - Depth of this leaf

#### Methods

Similar to TreeNode but returns leaf prediction/probabilities.

---

## Utility Functions

### `compute_gini_impurity(good_count, bad_count)`

Compute Gini impurity from good and bad counts.

**Returns:** float - Gini impurity (0.0 to 0.5)

### `information_gain(parent_good, parent_bad, left_good, left_bad, right_good, right_bad)`

Compute information gain from a split.

**Returns:** float - Information gain (higher is better)

### `validate_aggregate_data(df, feature_cols, good_col, bad_col, total_col=None)`

Validate aggregate data format and contents.

**Raises:** ValueError if data is invalid

---

## Data Format Requirements

### Input Data Format

The algorithm expects a pandas DataFrame with:

```csv
feature1,feature2,...,good_count,bad_count
value1,valueA,...,150,50
value2,valueB,...,80,120
```

### Constraints

- **Feature columns**: Must contain categorical values (no missing values)
- **Count columns**: Must be non-negative integers
- **Validation**: If total_col provided, must equal good_count + bad_count
- **No zero rows**: Rows with good_count + bad_count = 0 are not allowed

### Prediction Data Format

For prediction, provide DataFrame with only feature columns:

```csv
feature1,feature2,...
value1,valueA,...
value2,valueB,...
```

---

## Examples

### Basic Usage

```python
import pandas as pd
from cart_olap import AggregateCART

# Load aggregate data
df = pd.read_csv('aggregate_data.csv')

# Initialize classifier
cart = AggregateCART(max_depth=5, min_samples_leaf=10)

# Train
feature_cols = ['city', 'dayType', 'source']
cart.fit(df, feature_cols, 'good_count', 'bad_count')

# Predict
new_data = pd.DataFrame({
    'city': ['Delhi'],
    'dayType': ['WEEKEND'],
    'source': ['ios']
})

prediction = cart.predict(new_data)
probabilities = cart.predict_proba(new_data)
```

### Model Analysis

```python
# Print tree structure
cart.print_tree()

# Get model statistics
print(f"Tree depth: {cart.get_depth()}")
print(f"Number of leaves: {cart.get_n_leaves()}")
print(f"Features used: {cart.feature_names_}")
```

### Hyperparameter Tuning

```python
# Conservative model (fewer splits)
conservative = AggregateCART(
    max_depth=3,
    min_samples_leaf=50,
    min_impurity_decrease=0.01
)

# Aggressive model (more splits)
aggressive = AggregateCART(
    max_depth=15,
    min_samples_leaf=5,
    min_impurity_decrease=0.0
)
```