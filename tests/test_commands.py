# tests/test_commands.py
from calc.commands import add, subtract, multiply, divide

def test_add():
    assert add(3, 4) == 7.0
    assert add(-1, 1) == 0
    assert add(0, 0) == 0

def test_subtract():
    assert subtract(10, 5) == 5.0
    assert subtract(0, 5) == -5.0

def test_multiply():
    assert multiply(3, 4) == 12.0
    assert multiply(-1, 5) == -5.0

def test_divide():
    assert divide(10, 2) == 5.0
    assert divide(10, -2) == -5.0
