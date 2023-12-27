import datetime

from models import Notebook, SimpleNote


def test_add():
    notebook = Notebook()
    note = SimpleNote("дз", "номер 123", datetime.datetime.now(), True)
    notebook.add_note(note)
    assert len(notebook.notes()) == 1
