"""
Test module for plugin functionality.
"""

import pytest
from plugins.modulo import modulo
from plugins.mean_plugin import mean

def test_modulo():
    """Test for the modulo function."""
    assert modulo(10, 3) == 1
    assert modulo(10, 5) == 0
    assert modulo(-10, 3) == 2  # Python returns 2 for modulo(-10, 3)

    # Test division by zero case
    with pytest.raises(ZeroDivisionError):
        modulo(10, 0)

def test_mean():
    """Test for the mean function."""
    assert mean(10, 20) == 15
    assert mean(5, 5) == 5
    assert mean(0, 10) == 5
    assert mean(-5, 5) == 0
