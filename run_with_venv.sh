#!/bin/bash
# Script to run Python commands with virtual environment activated

# Change to the script's directory
cd "$(dirname "$0")"

# Activate virtual environment
source venv/bin/activate

# Run the command passed as arguments
"$@"