#!/usr/bin/env python3
"""
Command line script to run all tests for the CART OLAP project.

Usage:
    python run_tests.py [options]

Options:
    -v, --verbose     Run tests with verbose output
    -c, --coverage    Run tests with coverage reporting
    --basic          Run only basic functionality tests
    --all            Run all tests (default)
"""

import sys
import subprocess
import argparse
from pathlib import Path

def run_command(cmd, description):
    """Run a command and handle errors"""
    print(f"\n🔄 {description}...")
    print(f"Running: {' '.join(cmd)}")

    try:
        result = subprocess.run(cmd, check=True, capture_output=True, text=True)
        print(f"✅ {description} completed successfully")
        if result.stdout:
            print(result.stdout)
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ {description} failed")
        print(f"Error: {e}")
        if e.stdout:
            print(f"STDOUT:\n{e.stdout}")
        if e.stderr:
            print(f"STDERR:\n{e.stderr}")
        return False

def main():
    parser = argparse.ArgumentParser(description='Run CART OLAP tests')
    parser.add_argument('-v', '--verbose', action='store_true',
                       help='Run tests with verbose output')
    parser.add_argument('-c', '--coverage', action='store_true',
                       help='Run tests with coverage reporting')
    parser.add_argument('--basic', action='store_true',
                       help='Run only basic functionality tests')
    parser.add_argument('--all', action='store_true', default=True,
                       help='Run all tests (default)')

    args = parser.parse_args()

    # Check if we're in a virtual environment
    if not hasattr(sys, 'real_prefix') and not (hasattr(sys, 'base_prefix') and sys.base_prefix != sys.prefix):
        print("⚠️  Warning: Not running in a virtual environment")
        print("   Recommended: source venv/bin/activate")
        print()

    project_root = Path(__file__).parent
    print(f"🏠 Project root: {project_root}")

    # Test commands to run
    test_commands = []

    if args.basic:
        # Run basic test file
        cmd = ['python', '-m', 'pytest', 'test_basic.py']
        if args.verbose:
            cmd.append('-v')
        test_commands.append((cmd, "Basic functionality tests"))
    else:
        # Run all tests in tests/ directory
        if Path('tests').exists():
            cmd = ['python', '-m', 'pytest', 'tests/']
            if args.verbose:
                cmd.append('-v')
            if args.coverage:
                cmd.extend(['--cov=cart_olap', '--cov-report=html', '--cov-report=term'])
            test_commands.append((cmd, "All unit tests"))

        # Run basic test file if it exists
        if Path('test_basic.py').exists():
            cmd = ['python', '-m', 'pytest', 'test_basic.py']
            if args.verbose:
                cmd.append('-v')
            test_commands.append((cmd, "Basic functionality tests"))

    if not test_commands:
        print("❌ No test files found!")
        print("   Expected: tests/ directory or test_basic.py")
        return 1

    # Run all test commands
    failed_tests = []
    for cmd, description in test_commands:
        if not run_command(cmd, description):
            failed_tests.append(description)

    # Summary
    print("\n" + "="*50)
    print("📊 TEST SUMMARY")
    print("="*50)

    if failed_tests:
        print(f"❌ {len(failed_tests)} test suite(s) failed:")
        for test in failed_tests:
            print(f"   • {test}")
        return 1
    else:
        print("✅ All tests passed successfully!")

        if args.coverage and Path('htmlcov').exists():
            print("\n📈 Coverage report generated: htmlcov/index.html")

        return 0

if __name__ == "__main__":
    sys.exit(main())