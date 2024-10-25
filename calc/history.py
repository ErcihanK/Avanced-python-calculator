# calc/history.py
import pandas as pd
import os

class HistoryManager:
    def __init__(self, file_path='history.csv'):
        self.file_path = file_path

    def load_history(self):
        """Load the calculation history from a CSV file."""
        if os.path.exists(self.file_path):
            try:
                return pd.read_csv(self.file_path)
            except pd.errors.EmptyDataError:
                # Return an empty DataFrame if the CSV is empty
                return pd.DataFrame(columns=['command', 'num1', 'num2', 'result'])
        else:
            # Return an empty DataFrame if the file does not exist
            return pd.DataFrame(columns=['command', 'num1', 'num2', 'result'])

    def save_history(self, command, num1, num2, result):
        """Save a new calculation to the history."""
        history_df = self.load_history()
        new_record = pd.DataFrame([{'command': command, 'num1': num1, 'num2': num2, 'result': result}])
        
        if history_df.empty:
            # If history is empty, use new_record directly
            history_df = new_record
        else:
            # Concatenate only when history is not empty
            history_df = pd.concat([history_df, new_record], ignore_index=True)
        
        history_df.to_csv(self.file_path, index=False)

    def clear_history(self):
        """Clear the calculation history by writing an empty DataFrame to the file."""
        # Write an empty DataFrame with the correct columns to the CSV file
        pd.DataFrame(columns=['command', 'num1', 'num2', 'result']).to_csv(self.file_path, index=False)

    def display_history(self):
        """Display the calculation history."""
        history_df = self.load_history()
        if history_df.empty:
            print("No history available.")
        else:
            print(history_df)
