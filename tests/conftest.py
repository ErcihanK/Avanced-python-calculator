"""
Configuration for pytest to include the root directory in sys.path for module imports.
"""

import sys
import os

# Ensure the root project directory is in sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
