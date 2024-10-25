import sys
import logging
import os
import importlib
from dotenv import load_dotenv
from calc.commands import add, subtract, multiply, divide
from calc.history import HistoryManager

# Load environment variables
load_dotenv()

# Set up logging configuration
log_level = os.getenv('LOG_LEVEL', 'INFO').upper()
logging.basicConfig(level=log_level, format='%(asctime)s - %(levelname)s - %(message)s')

# Suppress logging for external libraries (like pandas)
for noisy_lib in ['pandas', 'matplotlib', 'numpy']:
    logging.getLogger(noisy_lib).setLevel(logging.ERROR)

# Initialize history manager
history_manager = HistoryManager()

# Command registry for dynamic commands (core and plugins)
commands = {
    'add': add,
    'subtract': subtract,
    'multiply': multiply,
    'divide': divide
}

# Function to dynamically load plugins
def load_plugins(plugin_dir='plugins'):
    try:
        for filename in os.listdir(plugin_dir):
            if filename.endswith('.py'):
                module_name = filename[:-3]
                module = importlib.import_module(f'{plugin_dir}.{module_name}')
                if hasattr(module, 'register_commands'):
                    module.register_commands(commands)
                    logging.info(f'Loaded plugin: {module_name}')
    except Exception as e:
        logging.error(f"Error loading plugins: {e}")

# REPL function
def repl():
    logging.info("Starting REPL...")
    print("Welcome to the Advanced Python Calculator!")
    print("Available commands: add, subtract, multiply, divide, history, clear_history")
    print("Enter 'menu' to see all commands.")
    print("Enter 'exit' to quit.")

    # Load plugins at the start of the REPL
    load_plugins()

    while True:
        user_input = input("calc> ").strip().lower()

        if user_input == 'exit':
            logging.info("Exiting REPL...")
            print("Goodbye!")
            sys.exit()

        if user_input == 'menu':
            print("Available commands:")
            for cmd in commands:
                print(cmd)
            continue

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

        # Division by zero check
        if command == 'divide' and num2 == 0:
            logging.error("Attempted to divide by zero.")
            print("Error: Division by zero is not allowed.")
            continue

        if command in commands:
            result = commands[command](num1, num2)
            logging.info(f"Executed {command} with {num1} and {num2}, result: {result}")
            print(f"Result: {result}")

            # Save to history
            history_manager.save_history(command, num1, num2, result)
        else:
            logging.warning(f"Unknown command: {command}")
            print("Unknown command.")

if __name__ == "__main__":
    repl()
