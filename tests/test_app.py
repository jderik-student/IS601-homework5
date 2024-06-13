# pylint: disable=unnecessary-dunder-call, invalid-name
'''
    This file contains tests to test app.py
'''

import pytest
from app import App

def test_app_start_exit_command(monkeypatch):
    """Test that the REPL exits correctly on 'exit' command."""
    monkeypatch.setattr('builtins.input', lambda _: 'exit')
    app = App()
    with pytest.raises(SystemExit) as e:
        app.start()
    assert e.type == SystemExit
    assert str(e.value) == "Exiting...", "The app did not exit as expected"
