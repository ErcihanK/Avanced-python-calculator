# calc/repl.py
import sys
from calc.commands import add, subtract, multiply, divide

def repl():
    print("Welcome to the Advanced Python Calculator!")
    print("Available commands: add, subtract, multiply, divide")
    print("Enter 'exit' to quit.")
    
    while True:
        user_input = input("calc> ").strip().lower()
        
        if user_input == 'exit':
            print("Goodbye!")
            sys.exit()
        
        parts = user_input.split()
        if len(parts) != 3:
            print("Invalid input. Please use the format: command number1 number2")
            continue
        
        command, num1_str, num2_str = parts
        try:
            num1 = float(num1_str)
            num2 = float(num2_str)
        except ValueError:
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
            print("Unknown command.")
            continue
        
        print(f"Result: {result}")

if __name__ == "__main__":
    repl()
