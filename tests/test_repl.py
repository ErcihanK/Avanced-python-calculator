# tests/test_repl.py
from unittest.mock import patch
from calc.repl import repl
import pytest

@patch('builtins.input', side_effect=['add 3 4', 'exit'])
def test_repl_add(mock_input):
    with patch('builtins.print') as mocked_print:
        # Catch the SystemExit caused by sys.exit() in the repl function
        with pytest.raises(SystemExit):
            repl()
        mocked_print.assert_any_call("Result: 7.0")

@patch('builtins.input', side_effect=['divide 10 0', 'exit'])
def test_repl_divide_by_zero(mock_input):
    with patch('builtins.print') as mocked_print:
        # Catch the SystemExit caused by sys.exit() in the repl function
        with pytest.raises(SystemExit):
            repl()
        mocked_print.assert_any_call("Error: Division by zero is not allowed.")
