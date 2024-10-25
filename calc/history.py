"""
This module manages the history of calculations.
"""

import os
import pandas as pd

class HistoryManager:
    """Manages saving, loading, and clearing of calculation history."""

    def __init__(self, file_path="history.csv"):
        """Initializes the history manager with a given file path."""
        self.file_path = file_path

    def save_history(self, command, num1, num2, result):
        """Saves a calculation to history."""
        data = {'command': [command], 'num1': [num1], 'num2': [num2], 'result': [result]}
        df = pd.DataFrame(data)
        if os.path.exists(self.file_path):
            df.to_csv(self.file_path, mode='a', header=False, index=False)
        else:
            df.to_csv(self.file_path, index=False)

    def load_history(self):
        """Loads and returns the calculation history from file."""
        if os.path.exists(self.file_path):
            return pd.read_csv(self.file_path)
        return pd.DataFrame(columns=['command', 'num1', 'num2', 'result'])

    def clear_history(self):
        """Clears the calculation history."""
        if os.path.exists(self.file_path):
            os.remove(self.file_path)

    def display_history(self):
        """Displays the calculation history."""
        history = self.load_history()
        if history.empty:
            print("No history available.")
        else:
            print(history.to_string(index=False))
