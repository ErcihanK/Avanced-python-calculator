# Avanced-python-calculator
This is an advanced command-line calculator that supports basic arithmetic operations, history management, dynamic plugin loading, and configuration via environment variables. The calculator operates in a REPL (Read-Eval-Print Loop) interface and is built with a modular design to facilitate easy extension.

Setup Instructions

Prerequisites
Python 3.12.2 (ensure it's added to your PATH)
Git (for cloning the repository)

Installation
Clone the Repository

Open a terminal or command prompt and clone this repository:
git clone [<repository-url>](https://github.com/ErcihanK/Avanced-python-calculator.git)

Navigate to the Project Directory

cd advanced-calc

Create a Virtual Environment
python -m venv venv

Activate the Virtual Environment
venv\Scripts\activate

Install Dependencies
pip install -r requirements.txt

Run the Calculator
Start the calculator's REPL interface:
python calc/repl.py

Usage
Available Commands
Arithmetic Operations: Perform basic calculations

add <num1> <num2> - Adds two numbers
subtract <num1> <num2> - Subtracts the second number from the first
multiply <num1> <num2> - Multiplies two numbers
divide <num1> <num2> - Divides the first number by the second (handles division by zero)

History Management:

history - Displays a list of past calculations
clear_history - Clears the entire calculation history

Plugins:
The calculator dynamically loads plugins from the plugins folder, enabling new commands without modifying the core code. Any .py file in the plugins folder with a register_commands function will be loaded as a command.

Utility Commands:
menu - Lists all available commands (including plugins)
exit - Exits the REPL interface

Example Usage

Welcome to the Advanced Python Calculator!
Available commands: add, subtract, multiply, divide, history, clear_history
Enter 'menu' to see all commands.
Enter 'exit' to quit.

calc> add 5 3
Result: 8.0

calc> divide 10 0
Error: Division by zero is not allowed.

calc> history
add        5.0    3.0    8.0
divide    10.0    0.0    Error: Division by zero is not allowed.

calc> clear_history
History cleared.

calc> exit
Goodbye!
Configuration via Environment Variables
This project uses a .env file to manage configuration variables. You can customize the logging level and other settings by adding them to .env in the project root.

Example .env file:

LOG_LEVEL=DEBUG

Run Tests
Tests are located in the tests folder, covering various functionalities, including arithmetic operations, history management, and plugin loading.

To run all tests:
pytest

To run tests with Pylint and Coverage:
pytest --pylint --cov

The project aims to maintain high code coverage. After running pytest --cov, a coverage report will be displayed, showing the coverage percentage for each module.

Design Patterns
The calculator uses several design patterns to ensure a scalable and flexible structure:

Command Pattern: Used to handle REPL commands.
Facade Pattern: Utilized for handling complex data management (history).

This project uses a professional logging setup to capture important events, errors, and debug information. Logs are configured through environment variables and can be customized as needed.

logging.info - Logs standard operation messages
logging.error - Logs errors such as invalid input and command execution issues
Logs are saved in a logs directory (created automatically) and contain detailed information about application behavior.

Additional Information
Version Control, Documentation, and Workflow
This project uses Git for version control and includes a .gitignore file to prevent unnecessary files from being committed.

GitHub Actions can be set up to automate testing and ensure code quality on every push or pull request.