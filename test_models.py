import datetime

from models import Notebook, SimpleNote


def test_ne_first_root():
    notebook = Notebook()
    note = SimpleNote("дз", "номер 123", datetime.datetime.now(), True)
    notebook.add_note(note)
    assert len(notebook.notes()) == 1
