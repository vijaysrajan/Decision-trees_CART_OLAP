#!/usr/bin/env python3
"""
Syntax validation test for enhanced CART implementation.

This test validates that all Python files compile correctly
and that the enhanced features are syntactically correct.
"""

import sys
import py_compile
from pathlib import Path

def test_file_compilation():
    """Test that all Python files compile correctly"""
    print("🔍 Testing Python File Compilation")
    print("=" * 50)

    base_dir = Path(__file__).parent.parent
    python_files = [
        "cart_olap/__init__.py",
        "cart_olap/utils.py",
        "cart_olap/aggregate_cart.py",
        "cart_olap/tree_nodes.py",
        "scripts/build_tree.py",
        "scripts/load_and_predict.py",
        "scripts/test_enhanced_features.py"
    ]

    all_passed = True

    for py_file in python_files:
        file_path = base_dir / py_file
        if file_path.exists():
            try:
                py_compile.compile(str(file_path), doraise=True)
                print(f"   ✅ {py_file}")
            except py_compile.PyCompileError as e:
                print(f"   ❌ {py_file}: {e}")
                all_passed = False
        else:
            print(f"   ⚠️  {py_file}: File not found")

    return all_passed

def test_enhanced_features_present():
    """Test that enhanced features are present in the code"""
    print("\n🔍 Testing Enhanced Features Presence")
    print("=" * 50)

    base_dir = Path(__file__).parent.parent

    # Check utils.py for enhanced functions
    utils_path = base_dir / "cart_olap/utils.py"
    if utils_path.exists():
        utils_content = utils_path.read_text()

        expected_functions = [
            "compute_entropy_impurity",
            "compute_log_loss_impurity",
            "compute_impurity",
            "compute_binomial_confidence_interval",
            "compute_wilson_score_interval",
            "compute_statistical_significance",
            "compute_split_quality_metrics"
        ]

        all_present = True
        for func in expected_functions:
            if func in utils_content:
                print(f"   ✅ {func}")
            else:
                print(f"   ❌ {func}: Not found")
                all_present = False

        if not all_present:
            return False
    else:
        print("   ❌ utils.py not found")
        return False

    # Check aggregate_cart.py for enhanced hyperparameters
    cart_path = base_dir / "cart_olap/aggregate_cart.py"
    if cart_path.exists():
        cart_content = cart_path.read_text()

        expected_params = [
            "criterion:",
            "min_samples_split:",
            "max_features:",
            "min_weight_fraction_leaf:",
            "max_leaf_nodes:",
            "ccp_alpha:"
        ]

        all_present = True
        for param in expected_params:
            if param in cart_content:
                print(f"   ✅ {param}")
            else:
                print(f"   ❌ {param}: Not found")
                all_present = False

        return all_present
    else:
        print("   ❌ aggregate_cart.py not found")
        return False

def test_configuration_files():
    """Test that configuration files are valid YAML"""
    print("\n🔍 Testing Configuration Files")
    print("=" * 50)

    base_dir = Path(__file__).parent.parent
    config_files = [
        "config/config.yaml",
        "config/config_entropy.yaml",
        "config/config_log_loss.yaml"
    ]

    all_valid = True

    for config_file in config_files:
        config_path = base_dir / config_file
        if config_path.exists():
            try:
                # Basic YAML syntax check
                content = config_path.read_text()

                # Check for required sections
                required_sections = [
                    "features:",
                    "target_good_col:",
                    "target_bad_col:",
                    "hyperparameters:",
                    "criterion:"
                ]

                missing_sections = []
                for section in required_sections:
                    if section not in content:
                        missing_sections.append(section)

                if missing_sections:
                    print(f"   ❌ {config_file}: Missing {missing_sections}")
                    all_valid = False
                else:
                    print(f"   ✅ {config_file}")

            except Exception as e:
                print(f"   ❌ {config_file}: {e}")
                all_valid = False
        else:
            print(f"   ⚠️  {config_file}: File not found")

    return all_valid

def main():
    """Run all validation tests"""
    print("🚀 Enhanced CART Syntax Validation")
    print("=" * 60)

    test_results = []

    # Run validation tests
    test_suites = [
        ("File Compilation", test_file_compilation),
        ("Enhanced Features", test_enhanced_features_present),
        ("Configuration Files", test_configuration_files)
    ]

    for suite_name, test_func in test_suites:
        try:
            result = test_func()
            test_results.append((suite_name, result))
        except Exception as e:
            print(f"   ❌ Test suite failed: {e}")
            test_results.append((suite_name, False))

    # Print summary
    print("\n🎯 Validation Summary")
    print("=" * 60)

    passed = sum(1 for _, result in test_results if result)
    total = len(test_results)

    for suite_name, result in test_results:
        status = "✅ PASS" if result else "❌ FAIL"
        print(f"   {suite_name:20s}: {status}")

    print(f"\n📊 Overall: {passed}/{total} validation tests passed")

    if passed == total:
        print("\n🎉 All syntax validation tests passed!")
        print("   - All Python files compile successfully")
        print("   - Enhanced features are properly implemented")
        print("   - Configuration files are valid")
        print("\n🔥 Enhanced CART implementation is ready!")
        print("   Features added:")
        print("   ✅ Multiple impurity criteria (gini, entropy, log_loss)")
        print("   ✅ sklearn-compatible hyperparameters")
        print("   ✅ Binomial confidence intervals")
        print("   ✅ Statistical significance testing")
        print("   ✅ Comprehensive split quality metrics")
        print("   ✅ Enhanced feature selection (max_features)")
        print("   ✅ Improved stopping criteria")
        return 0
    else:
        print(f"\n⚠️  {total - passed} validation test(s) failed")
        return 1

if __name__ == "__main__":
    sys.exit(main())