"""
Unit tests for the HistoryManager class.
"""

import os
import pytest
from calc.history import HistoryManager


@pytest.fixture
def setup_history_manager_fixture(tmpdir):
    """Set up the HistoryManager with a temporary file."""
    file_path = os.path.join(tmpdir, "test_history.csv")
    return HistoryManager(file_path)


def test_save_history(setup_history_manager_fixture):  # pylint: disable=redefined-outer-name
    """Test saving history to the manager."""
    history_mgr = setup_history_manager_fixture
    history_mgr.save_history('add', 3, 4, 7.0)
    history = history_mgr.load_history()
    assert len(history) == 1
    assert history.iloc[0]['command'] == 'add'
    assert history.iloc[0]['num1'] == 3
    assert history.iloc[0]['num2'] == 4
    assert history.iloc[0]['result'] == 7.0


def test_clear_history(setup_history_manager_fixture):  # pylint: disable=redefined-outer-name
    """Test clearing history."""
    history_mgr = setup_history_manager_fixture
    history_mgr.save_history('multiply', 3, 4, 12.0)
    history_mgr.clear_history()
    history = history_mgr.load_history()
    assert history.empty


def test_load_history_no_file(setup_history_manager_fixture):  # pylint: disable=redefined-outer-name
    """Test loading history when the history file does not exist."""
    history_mgr = setup_history_manager_fixture
    history = history_mgr.load_history()
    assert history.empty


def test_clear_history_no_file(setup_history_manager_fixture):  # pylint: disable=redefined-outer-name
    """Test clearing history when there is no history file."""
    history_mgr = setup_history_manager_fixture
    history_mgr.clear_history()  # This should not raise an error
    assert not os.path.exists(history_mgr.file_path)


def test_display_history_empty(setup_history_manager_fixture, capsys):  # pylint: disable=redefined-outer-name
    """Test displaying history when it's empty."""
    history_mgr = setup_history_manager_fixture
    history_mgr.display_history()
    captured = capsys.readouterr()
    assert "No history available." in captured.out
