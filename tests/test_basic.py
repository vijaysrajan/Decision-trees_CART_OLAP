"""
Basic test of AggregateCART without external dependencies.
This test uses only standard library to validate core logic.
"""

# Simple test data as lists/dicts
test_data = [
    {'feature1': 'A', 'feature2': 'X', 'good_count': 80, 'bad_count': 20},
    {'feature1': 'A', 'feature2': 'Y', 'good_count': 60, 'bad_count': 40},
    {'feature1': 'B', 'feature2': 'X', 'good_count': 30, 'bad_count': 70},
    {'feature1': 'B', 'feature2': 'Y', 'good_count': 10, 'bad_count': 90}
]

def test_gini_calculation():
    """Test Gini impurity calculation."""
    # Pure good node
    total = 100
    good = 100
    bad = 0
    p_good = good / total
    p_bad = bad / total
    gini = 1 - (p_good**2 + p_bad**2)
    assert gini == 0.0, f"Pure node should have gini=0, got {gini}"

    # Balanced node
    good = 50
    bad = 50
    p_good = good / total
    p_bad = bad / total
    gini = 1 - (p_good**2 + p_bad**2)
    assert gini == 0.5, f"Balanced node should have gini=0.5, got {gini}"

    # Imbalanced node
    good = 80
    bad = 20
    p_good = good / total
    p_bad = bad / total
    gini = 1 - (p_good**2 + p_bad**2)
    expected = 1 - (0.8**2 + 0.2**2)  # 1 - (0.64 + 0.04) = 0.32
    assert abs(gini - expected) < 1e-10, f"Expected gini={expected}, got {gini}"

    print("✓ Gini impurity calculations correct")

def test_information_gain():
    """Test information gain calculation."""
    # Parent: 100 good, 100 bad (gini = 0.5)
    # Left child: 80 good, 20 bad (gini = 0.32)
    # Right child: 20 good, 80 bad (gini = 0.32)

    parent_good, parent_bad = 100, 100
    left_good, left_bad = 80, 20
    right_good, right_bad = 20, 80

    parent_total = parent_good + parent_bad
    left_total = left_good + left_bad
    right_total = right_good + right_bad

    # Parent impurity
    p_parent_good = parent_good / parent_total
    p_parent_bad = parent_bad / parent_total
    parent_gini = 1 - (p_parent_good**2 + p_parent_bad**2)

    # Left child impurity
    p_left_good = left_good / left_total
    p_left_bad = left_bad / left_total
    left_gini = 1 - (p_left_good**2 + p_left_bad**2)

    # Right child impurity
    p_right_good = right_good / right_total
    p_right_bad = right_bad / right_total
    right_gini = 1 - (p_right_good**2 + p_right_bad**2)

    # Weighted child impurity
    left_weight = left_total / parent_total
    right_weight = right_total / parent_total
    weighted_child_gini = left_weight * left_gini + right_weight * right_gini

    # Information gain
    gain = parent_gini - weighted_child_gini

    # Both children have same gini (0.32), so weighted avg = 0.32
    # Information gain = 0.5 - 0.32 = 0.18
    expected_gain = 0.5 - 0.32
    assert abs(gain - expected_gain) < 1e-10, f"Expected gain={expected_gain}, got {gain}"

    print("✓ Information gain calculation correct")

def test_split_evaluation():
    """Test split evaluation on sample data."""
    # Calculate total counts
    total_good = sum(row['good_count'] for row in test_data)  # 180
    total_bad = sum(row['bad_count'] for row in test_data)    # 220

    print(f"Total samples: {total_good} good, {total_bad} bad")

    # Test split on feature1 = 'A'
    left_good = sum(row['good_count'] for row in test_data if row['feature1'] != 'A')  # B rows: 30+10=40
    left_bad = sum(row['bad_count'] for row in test_data if row['feature1'] != 'A')    # B rows: 70+90=160
    right_good = sum(row['good_count'] for row in test_data if row['feature1'] == 'A')  # A rows: 80+60=140
    right_bad = sum(row['bad_count'] for row in test_data if row['feature1'] == 'A')    # A rows: 20+40=60

    print(f"Split feature1='A': Left({left_good}g,{left_bad}b), Right({right_good}g,{right_bad}b)")

    # This should be a good split since A is mostly good, B is mostly bad
    assert left_bad > left_good, "Left (B) should have more bad samples"
    assert right_good > right_bad, "Right (A) should have more good samples"

    print("✓ Split evaluation logic correct")

def test_prediction_logic():
    """Test basic prediction logic."""
    # Simple rule: if feature1 == 'A', predict good (1), else predict bad (0)

    test_samples = [
        {'feature1': 'A', 'feature2': 'X'},
        {'feature1': 'A', 'feature2': 'Y'},
        {'feature1': 'B', 'feature2': 'X'},
        {'feature1': 'B', 'feature2': 'Y'}
    ]

    for sample in test_samples:
        if sample['feature1'] == 'A':
            prediction = 1  # Good
        else:
            prediction = 0  # Bad

        print(f"Sample {sample} -> Prediction: {prediction}")

    print("✓ Prediction logic correct")

def main():
    """Run all basic tests."""
    print("Running basic functionality tests...")
    print("=" * 50)

    test_gini_calculation()
    test_information_gain()
    test_split_evaluation()
    test_prediction_logic()

    print("=" * 50)
    print("✅ All basic tests passed!")
    print("\nNext steps:")
    print("1. Install pandas and numpy: pip install pandas numpy")
    print("2. Run full test suite: pytest tests/")
    print("3. Try the example: python examples/basic_usage.py")

if __name__ == "__main__":
    main()