import pytest
from plugins.modulo import modulo
from plugins.mean_plugin import mean

def test_modulo():
    assert modulo(10, 3) == 1
    assert modulo(10, 5) == 0
    assert modulo(-10, 3) == 2  # Fix: Python returns 2 for modulo(-10, 3)

    # Test division by zero case
    with pytest.raises(ZeroDivisionError):
        modulo(10, 0)

# Test mean function
def test_mean():
    assert mean(10, 20) == 15
    assert mean(5, 5) == 5
    assert mean(0, 10) == 5
    assert mean(-5, 5) == 0

    # Edge case: very small numbers
    assert mean(1e-10, 1e-10) == 1e-10
