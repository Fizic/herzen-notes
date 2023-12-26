import datetime
from abc import ABC, abstractmethod


class Note(ABC):
    @abstractmethod
    def __str__(self):
        pass


class SimpleNote(Note):
    def __init__(self, title: str, text: str, creation_date: datetime.datetime, important: bool):
        self.title = title
        self.text = text
        self.creation_date = creation_date
        self.important = important

    def __str__(self):
        msg = f'{self.title}\n{self.text}\nДата создания: {self.creation_date}\n'
        if self.important:
            msg += "Важно!"
        return msg


class NotebookMeta(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]


class Notebook(metaclass=NotebookMeta):
    def __init__(self):
        self.notes: list[Note] = []

    def add_note(self, note: Note):
        print(note)

    def delete_note(self, note: Note):
        pass

    def modify_note(self, note: Note):
        pass

    def notes(self):
        pass


def main():
    note = SimpleNote("дз", "номер 123", datetime.datetime.now(), True)
    notebook = Notebook()
    notebook.add_note(note)


if __name__ == "__main__":
    main()
