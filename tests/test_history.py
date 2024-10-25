# tests/test_history.py
import os
import pandas as pd
from calc.history import HistoryManager

def test_history_save_and_load(tmpdir):
    history_file = tmpdir.join("history.csv")
    history_manager = HistoryManager(file_path=str(history_file))

    history_manager.save_history("add", 3, 4, 7.0)
    history_df = history_manager.load_history()

    assert not history_df.empty
    assert history_df.iloc[0]['command'] == 'add'
    assert history_df.iloc[0]['result'] == 7.0

def test_clear_history(tmpdir):
    history_file = tmpdir.join("history.csv")
    history_manager = HistoryManager(file_path=str(history_file))

    history_manager.save_history("add", 3, 4, 7.0)
    history_manager.clear_history()

    history_df = history_manager.load_history()
    assert history_df.empty
