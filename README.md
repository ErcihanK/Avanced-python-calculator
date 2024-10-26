# Advanced Python Calculator

This is an advanced command-line calculator that supports basic arithmetic operations, history management, dynamic plugin loading, and configuration via environment variables. The calculator operates in a REPL (Read-Eval-Print Loop) interface and is built with a modular design to facilitate easy extension.

## Setup Instructions

### Prerequisites
- Python 3.12.2 (ensure it's added to your PATH)
- Git (for cloning the repository)

### Installation

#### Clone the Repository
Open a terminal or command prompt and clone this repository:

```bash
git clone https://github.com/ErcihanK/Avanced-python-calculator.git
```

#### Navigate to the Project Directory
```bash
cd advanced-calc
```

#### Create a Virtual Environment
```bash
python -m venv venv
```

#### Activate the Virtual Environment
```bash
venv\Scripts\activate
```

#### Install Dependencies
```bash
pip install -r requirements.txt
```

### Run the Calculator
Start the calculator's REPL interface:
```bash
py -m calc.repl
```

## Usage

### Available Commands

#### Arithmetic Operations: Perform basic calculations
- `add <num1> <num2>` - Adds two numbers
- `subtract <num1> <num2>` - Subtracts the second number from the first
- `multiply <num1> <num2>` - Multiplies two numbers
- `divide <num1> <num2>` - Divides the first number by the second (handles division by zero)

#### History Management:
- `history` - Displays a list of past calculations
- `clear_history` - Clears the entire calculation history

### Plugins
The calculator dynamically loads plugins from the `plugins` folder, enabling new commands without modifying the core code. Any `.py` file in the plugins folder with a `register_commands` function will be loaded as a command.

#### Utility Commands:
- `menu` - Lists all available commands (including plugins)
- `exit` - Exits the REPL interface

### Example Usage
```
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
divide     10.0   0.0    Error: Division by zero is not allowed.

calc> clear_history
History cleared.

calc> exit
Goodbye!
```

## Configuration via Environment Variables
This project uses a `.env` file to manage configuration variables. You can customize the logging level and other settings by adding them to `.env` in the project root.

### Example .env file:
```
LOG_LEVEL=DEBUG
```

### Environment Variables Usage
The calculator uses the `dotenv` library to load environment variables, allowing dynamic configuration. The logging level is set based on the `LOG_LEVEL` variable, providing flexibility for debugging.

```python
# Load environment variables
load_dotenv()

# Set up logging configuration
log_level = os.getenv('LOG_LEVEL', 'INFO').upper()
logging.basicConfig(level=log_level, format='%(asctime)s - %(levelname)s - %(message)s')
```

## Logging
The application utilizes Python's built-in logging module for structured logging.

### Logging Features
- `logging.info` - Logs standard operation messages.
- `logging.error` - Logs errors such as invalid input and command execution issues.

Logs are saved in a `logs` directory (created automatically) and contain detailed information about application behavior.

### Logging Usage
A professional logging setup captures essential events and errors, which aids in debugging and tracking application behavior.

```python
# Set up logging configuration
logging.basicConfig(level=log_level, format='%(asctime)s - %(levelname)s - %(message)s')
```

**Log examples in `repl.py`:**
- Successful command execution:
  ```python
  logging.info('Executed %s with %s and %s, result: %s', command, num1, num2, result)
  ```
- Handling division by zero:
  ```python
  logging.error("Attempted to divide by zero.")
  ```

## Exception Handling
The calculator employs exception handling to manage errors gracefully, following the "Look Before You Leap" (LBYL) and "Easier to Ask for Forgiveness than Permission" (EAFP) principles.

### Exception Handling Strategies
- **LBYL**: Checks for potential errors (e.g., validating input before performing operations).
- **EAFP**: Attempts to perform an operation and catches exceptions if they occur.

**Example of exception handling in `commands.py`:**
```python
def divide(a, b):
    """Returns the quotient of a and b. Raises an error if division by zero."""
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero")
    return a / b
```

**Example of handling user input in `repl.py`:**
```python
try:
    num1 = float(num1_str)
    num2 = float(num2_str)
except ValueError:
    logging.error('Invalid number input: %s, %s', num1_str, num2_str)
    print("Please enter valid numbers.")
```

## Run Tests
Tests are located in the `tests` folder, covering various functionalities, including arithmetic operations, history management, and plugin loading.

To run all tests:
```bash
pytest
```

To run tests with Pylint and Coverage:
```bash
pytest --pylint --cov
```

The project aims to maintain high code coverage. After running `pytest --cov`, a coverage report will be displayed, showing the coverage percentage for each module.

## Design Patterns
The calculator uses several design patterns to ensure a scalable and flexible structure:
- **Command Pattern**: Used to handle REPL commands, as seen in the `commands.py` module.
- **Facade Pattern**: Utilized for handling complex data management (history), implemented in the `HistoryManager` class in `history.py`.

### Design Pattern Example
```python
# Command Pattern Implementation in commands.py
def add(a, b):
    """Returns the sum of a and b."""
    return a + b
```
## Video Demonstration
Check out the video demonstration of the Advanced Python Calculator:
[Watch the Video](https://www.youtube.com/watch?v=WzPxkbU_EAI)
