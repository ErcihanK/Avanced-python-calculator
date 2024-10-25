# calc/repl.py
import sys
import logging
import os
from dotenv import load_dotenv
from calc.commands import add, subtract, multiply, divide
from calc.history import HistoryManager

# Load environment variables
load_dotenv()

# Set up logging configuration
log_level = os.getenv('LOG_LEVEL', 'INFO').upper()
logging.basicConfig(level=log_level, format='%(asctime)s - %(levelname)s - %(message)s')

# Initialize history manager
history_manager = HistoryManager()

def repl():
    logging.info("Starting REPL...")
    print("Welcome to the Advanced Python Calculator!")
    print("Available commands: add, subtract, multiply, divide, history, clear_history")
    print("Enter 'exit' to quit.")
    
    while True:
        user_input = input("calc> ").strip().lower()
        
        if user_input == 'exit':
            logging.info("Exiting REPL...")
            print("Goodbye!")
            sys.exit()

        if user_input == 'history':
            history_manager.display_history()
            continue
        
        if user_input == 'clear_history':
            history_manager.clear_history()
            print("History cleared.")
            continue

        parts = user_input.split()
        if len(parts) != 3:
            logging.error(f"Invalid input: {user_input}")
            print("Invalid input. Please use the format: command number1 number2")
            continue
        
        command, num1_str, num2_str = parts
        try:
            num1 = float(num1_str)
            num2 = float(num2_str)
        except ValueError:
            logging.error(f"Invalid number input: {num1_str}, {num2_str}")
            print("Please enter valid numbers.")
            continue
        
        if command == 'add':
            result = add(num1, num2)
        elif command == 'subtract':
            result = subtract(num1, num2)
        elif command == 'multiply':
            result = multiply(num1, num2)
        elif command == 'divide':
            result = divide(num1, num2)
        else:
            logging.warning(f"Unknown command: {command}")
            print("Unknown command.")
            continue
        
        logging.info(f"Executed {command} with {num1} and {num2}, result: {result}")
        print(f"Result: {result}")
        
        # Save to history
        history_manager.save_history(command, num1, num2, result)

if __name__ == "__main__":
    repl()
