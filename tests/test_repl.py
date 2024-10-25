"""
Unit tests for the REPL functionality.
"""

from unittest.mock import patch
import pytest
from calc.repl import repl, load_plugins


@patch('builtins.input', side_effect=['add 3 4', 'exit'])
def test_repl_add_command(_mock_input):
    """Test 'add' command in REPL."""
    with patch('builtins.print') as mocked_print:
        with pytest.raises(SystemExit):
            repl()
        mocked_print.assert_any_call('Result: 7.0')


@patch('builtins.input', side_effect=['divide 10 0', 'exit'])
def test_repl_divide_by_zero(_mock_input):
    """Test division by zero in REPL."""
    with patch('builtins.print') as mocked_print:
        with pytest.raises(SystemExit):
            repl()
        mocked_print.assert_any_call("Error: Division by zero is not allowed.")


@patch('builtins.input', side_effect=['add foo bar', 'exit'])
def test_repl_invalid_number(_mock_input):
    """Test invalid number input in REPL."""
    with patch('builtins.print') as mocked_print:
        with pytest.raises(SystemExit):
            repl()
        mocked_print.assert_any_call("Please enter valid numbers.")


@patch('builtins.input', side_effect=['menu', 'exit'])
def test_repl_menu(_mock_input):
    """Test menu command in REPL."""
    with patch('builtins.print') as mocked_print:
        with pytest.raises(SystemExit):
            repl()
        mocked_print.assert_any_call("Available commands:")


@patch('builtins.input', side_effect=['unknown_cmd 1 2', 'exit'])
def test_repl_unknown_command(_mock_input):
    """Test handling of unknown commands in REPL."""
    with patch('builtins.print') as mocked_print:
        with pytest.raises(SystemExit):
            repl()
        mocked_print.assert_any_call("Unknown command.")


@patch('os.listdir', side_effect=FileNotFoundError())
def test_plugin_loading_failure(mock_listdir):
    """Test plugin loading failure due to missing directory."""
    with patch('calc.repl.logging') as mocked_log:
        load_plugins('nonexistent_plugins_dir')
        mocked_log.error.assert_any_call(
            'Plugin directory not found: %s', mock_listdir.side_effect
        )


@patch('builtins.input', side_effect=['exit'])
def test_repl_exit(_mock_input):
    """Test exit command in REPL."""
    with patch('builtins.print') as mocked_print:
        with pytest.raises(SystemExit):
            repl()
        mocked_print.assert_any_call("Goodbye!")


@patch('builtins.input', side_effect=['clear_history', 'exit'])
def test_repl_clear_history(_mock_input):
    """Test clearing history in REPL."""
    with patch('builtins.print') as mocked_print:
        with pytest.raises(SystemExit):
            repl()
        mocked_print.assert_any_call("History cleared.")


@patch('builtins.input', side_effect=['history', 'exit'])
def test_repl_history(_mock_input):
    """Test history command in REPL."""
    with patch('builtins.print') as mocked_print:
        with pytest.raises(SystemExit):
            repl()
        mocked_print.assert_any_call("No history available.")
