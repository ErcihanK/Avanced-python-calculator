import os
import pandas as pd
import pytest
from calc.history import HistoryManager

@pytest.fixture
def setup_history_manager(tmpdir):
    """Set up the HistoryManager with a temporary file."""
    file_path = os.path.join(tmpdir, "test_history.csv")
    return HistoryManager(file_path)

def test_save_history(setup_history_manager):
    """Test saving history to the manager."""
    history_manager = setup_history_manager
    history_manager.save_history('add', 3, 4, 7.0)
    history = history_manager.load_history()
    assert len(history) == 1
    assert history.iloc[0]['command'] == 'add'
    assert history.iloc[0]['num1'] == 3
    assert history.iloc[0]['num2'] == 4
    assert history.iloc[0]['result'] == 7.0

def test_clear_history(setup_history_manager):
    """Test clearing history."""
    history_manager = setup_history_manager
    history_manager.save_history('multiply', 3, 4, 12.0)
    history_manager.clear_history()
    history = history_manager.load_history()
    assert history.empty

def test_load_history_no_file(setup_history_manager):
    """Test loading history when the history file does not exist."""
    history_manager = setup_history_manager
    history = history_manager.load_history()
    assert history.empty

def test_clear_history_no_file(setup_history_manager):
    """Test clearing history when there is no history file."""
    history_manager = setup_history_manager
    history_manager.clear_history()  # This should not raise an error
    # Ensure file does not exist
    assert not os.path.exists(history_manager.file_path)

def test_display_history_empty(setup_history_manager, capsys):
    """Test displaying history when it's empty."""
    history_manager = setup_history_manager
    history_manager.display_history()
    captured = capsys.readouterr()
    assert "No history available." in captured.out
