"""
This module defines basic arithmetic operations.
"""

def add(a, b):
    """Returns the sum of a and b."""
    return a + b

def subtract(a, b):
    """Returns the difference between a and b."""
    return a - b

def multiply(a, b):
    """Returns the product of a and b."""
    return a * b

def divide(a, b):
    """Returns the quotient of a and b. Raises an error if division by zero."""
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero")
    return a / b
