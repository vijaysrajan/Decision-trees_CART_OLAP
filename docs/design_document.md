# Design Document: CART for Aggregate OLAP Data

## Overview

This document describes the design and implementation of a CART (Classification and Regression Trees) decision tree classifier that works directly with pre-aggregated OLAP cube data containing good/bad counts.

## Motivation

Traditional decision tree algorithms like sklearn's DecisionTreeClassifier require access to individual data records. However, in many real-world scenarios:

1. **Privacy concerns** prevent sharing raw individual records
2. **Data warehouses** store only aggregate data in OLAP cubes
3. **Performance requirements** demand training on summarized data
4. **Memory constraints** limit processing of large raw datasets

This implementation addresses these challenges by computing decision tree splits directly from aggregate counts, eliminating the need for raw data access.

## Key Design Principles

### 1. Sklearn Compatibility

The API closely follows sklearn's DecisionTreeClassifier:
- `fit(X, feature_cols, good_col, bad_col)` for training
- `predict(X)` and `predict_proba(X)` for inference
- Standard attributes like `tree_`, `feature_names_`, etc.

### 2. Direct Aggregate Processing

All CART metrics are computed directly from aggregate counts:
- **Gini Impurity**: `1 - (p_good² + p_bad²)` where `p_good = good_count/total`
- **Information Gain**: `parent_impurity - weighted_child_impurity`
- **Split Evaluation**: Group by feature values and sum counts

### 3. Exact Results

Unlike approximation methods (e.g., theta sketches), this approach provides exact results within the boundaries of the pre-aggregation.

### 4. Future-Proof Design

Architecture designed for easy extension to:
- Spark distributed processing
- Metric Decomposition Trees
- Multi-class classification
- Regression problems

## Architecture

### Core Components

```
cart_olap/
├── aggregate_cart.py      # Main CART implementation
├── tree_nodes.py          # Node data structures
├── utils.py               # Utility functions
└── __init__.py           # Package interface
```

### Class Hierarchy

```
AggregateCART
├── tree_: TreeNode | LeafNode
├── feature_names_: List[str]
├── n_features_: int
└── classes_: np.array

TreeNode
├── feature: str
├── split_value: Any
├── left: TreeNode | LeafNode
├── right: TreeNode | LeafNode
└── statistics (samples, impurity, counts)

LeafNode
├── prediction: int
├── class_probabilities: Tuple[float, float]
└── statistics (samples, impurity, counts)
```

## Algorithm Details

### Training Phase

1. **Data Validation**
   - Check required columns exist
   - Validate non-negative counts
   - Verify total count consistency (if provided)
   - Handle missing values

2. **Tree Building** (Recursive)
   - **Stopping Criteria Check**:
     - Maximum depth reached
     - Minimum samples threshold
     - Pure node (impurity = 0)
     - No informative splits available

   - **Best Split Finding**:
     - For each feature and each unique value:
       - Group aggregate rows by feature == value
       - Sum good/bad counts for each group
       - Calculate information gain
     - Select split with maximum information gain

   - **Node Creation**:
     - If good split found: create TreeNode with children
     - Otherwise: create LeafNode with majority class

3. **Split Evaluation Formula**
   ```
   For split feature=F, value=V:
   - Left child:  rows where F != V
   - Right child: rows where F == V

   Information Gain = Parent_Impurity - Weighted_Child_Impurity
   where:
   - Parent_Impurity = gini(parent_good, parent_bad)
   - Child_Impurity = (left_size/total) * gini(left_good, left_bad) +
                      (right_size/total) * gini(right_good, right_bad)
   ```

### Prediction Phase

1. **Tree Traversal**
   - Start at root node
   - For each internal node: check `feature == split_value`
   - Go right if true, left if false
   - Return leaf prediction/probabilities

2. **Batch Prediction**
   - Convert each DataFrame row to dictionary
   - Apply tree traversal to each sample
   - Return numpy array of predictions/probabilities

## Data Format Specification

### Training Data

```csv
feature1,feature2,feature3,good_count,bad_count,total_count
A,X,1,150,50,200
A,Y,0,80,20,100
B,X,1,70,30,100
```

**Requirements:**
- Feature columns: Categorical values (strings/numbers)
- Count columns: Non-negative integers
- No missing values in feature columns
- Optional total_count for validation

### Prediction Data

```csv
feature1,feature2,feature3
A,X,1
B,Y,0
```

**Requirements:**
- Same feature columns as training
- No count columns needed
- No missing values

## Performance Characteristics

### Time Complexity

- **Training**: O(R × F × V) where:
  - R = number of aggregate rows
  - F = number of features
  - V = average unique values per feature

- **Prediction**: O(D) where D = tree depth

### Memory Complexity

- **Training**: O(R) for storing aggregate data
- **Model**: O(N) where N = number of tree nodes
- **Prediction**: O(1) per sample

### Scalability

Compared to raw data approaches:
- **Memory**: O(aggregate_rows) vs O(raw_rows)
- **Training Time**: Proportional to aggregate size, not raw size
- **Accuracy**: Exact within aggregation boundaries

## Comparison with Related Approaches

### vs. Traditional CART

| Aspect | Traditional CART | Aggregate CART |
|--------|------------------|----------------|
| Input | Raw individual records | Pre-aggregated counts |
| Memory | O(raw_data_size) | O(aggregate_size) |
| Privacy | Requires raw access | Works with aggregates |
| Accuracy | Exact | Exact (within aggregation) |
| Performance | Slower on large data | Faster with good aggregation |

### vs. Theta Sketch Approach

| Aspect | Theta Sketches | Aggregate CART |
|--------|---------------|----------------|
| Accuracy | Approximate | Exact |
| Complexity | High (statistical) | Low (direct computation) |
| Memory | Bounded by sketch size | Bounded by aggregate size |
| Use Case | Streaming data | Pre-aggregated cubes |

### vs. Frequent Itemsets

| Aspect | Frequent Itemsets | Aggregate CART |
|--------|------------------|----------------|
| Goal | Find associations | Build classifier |
| Metric | Support counting | Impurity reduction |
| Output | Itemset rules | Decision tree |
| Complexity | Combinatorial growth | Greedy tree building |

## Implementation Decisions

### 1. Binary Splits Only

- **Decision**: Only binary splits (feature == value vs feature != value)
- **Rationale**: Simplifies implementation, works well with categorical data
- **Alternative**: Multi-way splits for categorical features
- **Future**: Could be extended for multi-way splits

### 2. Gini Impurity Only

- **Decision**: Use Gini impurity as splitting criterion
- **Rationale**: Simple to compute, good performance for binary classification
- **Alternative**: Entropy, classification error
- **Future**: Could add criterion parameter

### 3. No Bootstrap/Bagging

- **Decision**: Single tree, no ensemble methods
- **Rationale**: Focus on core CART algorithm first
- **Alternative**: Random Forest equivalent
- **Future**: Could add ensemble wrapper

### 4. Categorical Features Only

- **Decision**: Assume all features are categorical
- **Rationale**: Matches typical OLAP cube structure
- **Alternative**: Support continuous features with binning
- **Future**: Add continuous feature support

## Testing Strategy

### Unit Tests Coverage

1. **Utility Functions** (`test_utils.py`)
   - Gini impurity calculations
   - Information gain computations
   - Data validation logic

2. **Tree Nodes** (`test_tree_nodes.py`)
   - Node creation and properties
   - Prediction traversal
   - Information retrieval

3. **Main Classifier** (`test_aggregate_cart.py`)
   - Fitting with various data formats
   - Prediction accuracy
   - Hyperparameter effects
   - Edge cases and error handling

### Test Data

- **Simple synthetic data**: For unit testing
- **Complex realistic data**: DUAggregateData.csv for integration testing
- **Edge cases**: Pure nodes, identical features, empty splits

## Extension Points

### 1. Metric Decomposition Trees

Future implementation for explaining metric variance:

```python
class MetricDecompositionTree(AggregateTreeBase):
    def fit(self, df, feature_cols, metric_col, count_col=None):
        # Build tree to maximize explained variance
        # Instead of minimizing impurity
```

### 2. Spark Integration

Design for distributed processing:

```python
# Aggregate operations are naturally distributed
def _find_best_split_spark(self, data_rdd, features):
    # Group by feature values across partitions
    # Collect and sum counts
    # Select best split
```

### 3. Multi-class Support

Extension to multiple classes:

```python
# Instead of good_col, bad_col
def fit(self, df, feature_cols, count_cols):
    # count_cols = ['class0_count', 'class1_count', 'class2_count']
    # Generalize Gini impurity to multiple classes
```

## Limitations and Trade-offs

### Current Limitations

1. **Categorical features only**: No continuous feature support
2. **Binary classification only**: No multi-class or regression
3. **No feature importance**: Limited interpretability features
4. **No pruning**: Only pre-pruning via stopping criteria
5. **No ensemble methods**: Single tree only

### Trade-offs Made

1. **Simplicity vs. Flexibility**: Chose simple, focused implementation
2. **Performance vs. Features**: Optimized for core use case
3. **Exact vs. Approximate**: Chose exact results within aggregation
4. **Memory vs. Speed**: Optimized for aggregate data size

### Known Issues

1. **Identical feature combinations**: Limited splitting opportunities
2. **High cardinality features**: May create very deep trees
3. **Imbalanced aggregates**: Some splits may create very small children
4. **No random state**: Deterministic but not reproducible with ties

## Future Roadmap

### Phase 1 (Current)
- ✅ Core CART implementation
- ✅ Comprehensive testing
- ✅ Documentation and examples

### Phase 2 (Near term)
- [ ] Continuous feature support
- [ ] Multi-class classification
- [ ] Feature importance calculation
- [ ] Tree visualization

### Phase 3 (Medium term)
- [ ] Metric Decomposition Trees
- [ ] Spark distributed implementation
- [ ] Ensemble methods (Random Forest equivalent)
- [ ] Post-pruning algorithms

### Phase 4 (Long term)
- [ ] Regression support
- [ ] Advanced splitting criteria
- [ ] Online learning capabilities
- [ ] Integration with MLOps pipelines

## Conclusion

This implementation provides a clean, efficient solution for building decision trees from aggregate OLAP data. The design balances simplicity with extensibility, providing immediate value while laying the foundation for future enhancements.

The key innovation is computing CART metrics directly from aggregate counts, enabling privacy-preserving machine learning on data warehouse cubes without sacrificing accuracy or performance.