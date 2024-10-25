"""
Test module for calc.commands functions.
"""

from calc.commands import add, subtract, multiply, divide

def test_add():
    """Test for the add function."""
    assert add(3, 4) == 7.0
    assert add(-1, 1) == 0
    assert add(0, 0) == 0

def test_subtract():
    """Test for the subtract function."""
    assert subtract(10, 5) == 5.0
    assert subtract(0, 5) == -5.0

def test_multiply():
    """Test for the multiply function."""
    assert multiply(3, 4) == 12.0
    assert multiply(-1, 5) == -5.0

def test_divide():
    """Test for the divide function."""
    assert divide(10, 2) == 5.0
    assert divide(10, -2) == -5.0
