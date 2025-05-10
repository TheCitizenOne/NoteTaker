#!/usr/bin/env python3
"""
-- Note Taker Entry Point --

This file will init main.py in the notetaker directory.
Please don't alter this file for normal use.
"""

import sys
import os

# Add the src directory to the Python path
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), 'src'))  # E402

# Import the main function from the package
from main import main

if __name__ == "__main__":
    main()
