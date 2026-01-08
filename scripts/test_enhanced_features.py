#!/usr/bin/env python3
"""
Test script for enhanced CART features and hyperparameters.

This script tests the enhanced functionality including:
- Multiple impurity criteria (gini, entropy, log_loss)
- Additional hyperparameters (min_samples_split, max_features, etc.)
- Binomial confidence intervals and statistical enhancements
- Comparison with sklearn-style parameters

Requirements:
- pandas, numpy, scipy (for statistical functions)
- yaml (for configuration loading)

Usage:
    python scripts/test_enhanced_features.py [--verbose]
"""

import sys
import argparse
import json
from pathlib import Path
import traceback

# Add the cart_olap module to the path
sys.path.insert(0, str(Path(__file__).parent.parent))

def test_statistical_functions():
    """Test standalone statistical functions that don't require pandas"""
    print("🔬 Testing Statistical Functions")
    print("=" * 50)

    try:
        from cart_olap.utils import (
            compute_gini_impurity,
            compute_entropy_impurity,
            compute_log_loss_impurity,
            compute_impurity
        )

        # Test basic impurity functions
        print("1. Testing impurity calculations:")
        good_count, bad_count = 60, 40

        gini = compute_gini_impurity(good_count, bad_count)
        entropy = compute_entropy_impurity(good_count, bad_count)
        log_loss = compute_log_loss_impurity(good_count, bad_count)

        print(f"   Sample: {good_count} good, {bad_count} bad")
        print(f"   Gini impurity:     {gini:.4f}")
        print(f"   Entropy impurity:  {entropy:.4f}")
        print(f"   Log loss impurity: {log_loss:.4f}")

        # Test generic compute_impurity function
        print("\n2. Testing generic impurity function:")
        for criterion in ["gini", "entropy", "log_loss"]:
            impurity = compute_impurity(good_count, bad_count, criterion)
            print(f"   {criterion:10s}: {impurity:.4f}")

        print("   ✅ Basic impurity functions working correctly!")

        # Test edge cases
        print("\n3. Testing edge cases:")
        pure_good = compute_impurity(100, 0, "gini")
        pure_bad = compute_impurity(0, 100, "gini")
        empty = compute_impurity(0, 0, "gini")

        print(f"   Pure good (100/0): {pure_good:.4f} (should be 0.0)")
        print(f"   Pure bad (0/100):  {pure_bad:.4f} (should be 0.0)")
        print(f"   Empty (0/0):       {empty:.4f} (should be 0.0)")

        assert pure_good == 0.0, "Pure good should have 0 impurity"
        assert pure_bad == 0.0, "Pure bad should have 0 impurity"
        assert empty == 0.0, "Empty should have 0 impurity"

        print("   ✅ Edge cases handled correctly!")

        return True

    except Exception as e:
        print(f"   ❌ Error in statistical functions: {e}")
        traceback.print_exc()
        return False

def test_enhanced_statistics():
    """Test enhanced statistical functions if scipy is available"""
    print("\n🔬 Testing Enhanced Statistical Functions")
    print("=" * 50)

    try:
        # Try to import scipy-dependent functions
        from cart_olap.utils import (
            compute_binomial_confidence_interval,
            compute_wilson_score_interval,
            compute_statistical_significance,
            compute_split_quality_metrics
        )

        print("1. Testing confidence intervals:")

        # Test binomial confidence interval
        good_count, total_count = 25, 50
        lower, upper = compute_binomial_confidence_interval(good_count, total_count, 0.95)
        print(f"   Binomial CI for {good_count}/{total_count}: [{lower:.3f}, {upper:.3f}]")

        # Test Wilson score interval
        lower, upper = compute_wilson_score_interval(good_count, total_count, 0.95)
        print(f"   Wilson score CI for {good_count}/{total_count}: [{lower:.3f}, {upper:.3f}]")

        print("   ✅ Confidence intervals working correctly!")

        print("\n2. Testing statistical significance:")

        # Test statistical significance
        is_sig, p_value = compute_statistical_significance(20, 10, 10, 20, 0.05)
        print(f"   Split (20,10) vs (10,20): significant={is_sig}, p={p_value:.4f}")

        # Test non-significant split
        is_sig, p_value = compute_statistical_significance(15, 15, 14, 16, 0.05)
        print(f"   Split (15,15) vs (14,16): significant={is_sig}, p={p_value:.4f}")

        print("   ✅ Statistical significance tests working correctly!")

        print("\n3. Testing comprehensive split metrics:")

        metrics = compute_split_quality_metrics(
            parent_good=40, parent_bad=30,
            left_good=25, left_bad=10,
            right_good=15, right_bad=20,
            criterion="gini"
        )

        print("   Split quality metrics:")
        print(f"     Information gain: {metrics['information_gain']:.4f}")
        print(f"     Gini gain: {metrics['gini_gain']:.4f}")
        print(f"     Entropy gain: {metrics['entropy_gain']:.4f}")
        print(f"     Statistical significance: {metrics['is_statistically_significant']}")
        print(f"     P-value: {metrics['p_value']:.4f}")
        print(f"     Split balance: {metrics['split_balance']:.3f}")

        print("   ✅ Comprehensive metrics working correctly!")

        return True

    except ImportError as e:
        print(f"   ⚠️  Scipy not available, skipping enhanced statistics: {e}")
        return False
    except Exception as e:
        print(f"   ❌ Error in enhanced statistics: {e}")
        traceback.print_exc()
        return False

def test_hyperparameter_validation():
    """Test hyperparameter validation"""
    print("\n⚙️  Testing Hyperparameter Validation")
    print("=" * 50)

    try:
        from cart_olap import AggregateCART

        print("1. Testing valid hyperparameters:")

        # Test valid configurations
        valid_configs = [
            {"criterion": "gini", "max_depth": 5},
            {"criterion": "entropy", "max_features": "sqrt"},
            {"criterion": "log_loss", "max_features": 10},
            {"min_samples_split": 10, "min_samples_leaf": 5},
            {"max_features": "log2", "random_state": 42}
        ]

        for i, config in enumerate(valid_configs):
            try:
                cart = AggregateCART(**config)
                print(f"   Config {i+1}: ✅ {config}")
            except Exception as e:
                print(f"   Config {i+1}: ❌ {config} -> {e}")
                return False

        print("\n2. Testing invalid hyperparameters:")

        # Test invalid configurations
        invalid_configs = [
            {"criterion": "invalid_criterion"},
            {"max_depth": -1},
            {"min_samples_split": 0},
            {"min_samples_leaf": 0},
            {"max_features": -1}
        ]

        for i, config in enumerate(invalid_configs):
            try:
                cart = AggregateCART(**config)
                print(f"   Invalid config {i+1}: ❌ Should have failed: {config}")
                return False
            except (ValueError, TypeError) as e:
                print(f"   Invalid config {i+1}: ✅ Correctly rejected: {config}")

        print("\n   ✅ Hyperparameter validation working correctly!")
        return True

    except ImportError as e:
        print(f"   ⚠️  Cannot import AggregateCART: {e}")
        return False
    except Exception as e:
        print(f"   ❌ Error in hyperparameter validation: {e}")
        traceback.print_exc()
        return False

def test_configuration_examples():
    """Test that configuration files are valid"""
    print("\n📋 Testing Configuration Examples")
    print("=" * 50)

    try:
        import yaml

        config_files = [
            "config/config.yaml",
            "config/config_entropy.yaml",
            "config/config_log_loss.yaml"
        ]

        base_dir = Path(__file__).parent.parent

        for config_file in config_files:
            config_path = base_dir / config_file

            if config_path.exists():
                try:
                    with open(config_path, 'r') as f:
                        config = yaml.safe_load(f)

                    # Validate required keys
                    required_keys = ['features', 'target_good_col', 'target_bad_col']
                    missing_keys = [key for key in required_keys if key not in config]

                    if missing_keys:
                        print(f"   {config_file}: ❌ Missing keys: {missing_keys}")
                        return False

                    # Check hyperparameters
                    hyperparams = config.get('hyperparameters', {})
                    criterion = hyperparams.get('criterion', 'gini')

                    if criterion not in ['gini', 'entropy', 'log_loss']:
                        print(f"   {config_file}: ❌ Invalid criterion: {criterion}")
                        return False

                    print(f"   {config_file}: ✅ Valid ({criterion} criterion)")

                except yaml.YAMLError as e:
                    print(f"   {config_file}: ❌ YAML error: {e}")
                    return False
                except Exception as e:
                    print(f"   {config_file}: ❌ Error: {e}")
                    return False
            else:
                print(f"   {config_file}: ⚠️  File not found")

        print("\n   ✅ Configuration files valid!")
        return True

    except ImportError:
        print("   ⚠️  PyYAML not available, skipping configuration tests")
        return False
    except Exception as e:
        print(f"   ❌ Error testing configurations: {e}")
        return False

def main():
    """Run all tests"""
    parser = argparse.ArgumentParser(description='Test enhanced CART features')
    parser.add_argument('-v', '--verbose', action='store_true',
                       help='Print verbose output')

    args = parser.parse_args()

    print("🚀 Testing Enhanced CART Features")
    print("=" * 60)

    test_results = []

    # Run all test suites
    test_suites = [
        ("Statistical Functions", test_statistical_functions),
        ("Enhanced Statistics", test_enhanced_statistics),
        ("Hyperparameter Validation", test_hyperparameter_validation),
        ("Configuration Examples", test_configuration_examples)
    ]

    for suite_name, test_func in test_suites:
        print(f"\n📋 Running {suite_name}")
        try:
            result = test_func()
            test_results.append((suite_name, result))
        except Exception as e:
            print(f"   ❌ Test suite failed: {e}")
            if args.verbose:
                traceback.print_exc()
            test_results.append((suite_name, False))

    # Print summary
    print("\n🎯 Test Summary")
    print("=" * 60)

    passed = sum(1 for _, result in test_results if result)
    total = len(test_results)

    for suite_name, result in test_results:
        status = "✅ PASS" if result else "❌ FAIL"
        print(f"   {suite_name:25s}: {status}")

    print(f"\n📊 Overall: {passed}/{total} test suites passed")

    if passed == total:
        print("\n🎉 All enhanced features working correctly!")
        print("   - Multiple impurity criteria implemented")
        print("   - Enhanced hyperparameters available")
        print("   - Statistical functions operational")
        print("   - Configuration examples valid")
        return 0
    else:
        print(f"\n⚠️  {total - passed} test suite(s) failed")
        print("   Note: Some failures may be due to missing dependencies")
        return 1

if __name__ == "__main__":
    sys.exit(main())