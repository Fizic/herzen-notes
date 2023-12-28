from __future__ import annotations

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
        msg = f'''
==============
{self.title}
{self.text}
Дата создания: {self.creation_date}
{'Важно!' if self.important else ''}
==============
'''
        return msg


class Subject(ABC):
    @abstractmethod
    def attach(self, observer: Observer) -> None:
        pass

    @abstractmethod
    def detach(self, observer: Observer) -> None:
        pass

    @abstractmethod
    def notify(self) -> None:
        pass


class Singleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]


class NotebookMeta(Singleton, Subject, ABC):
    pass


class Notebook(metaclass=NotebookMeta):
    def __init__(self):
        self.__notes: list[Note] = []

    def add_note(self, note: Note):
        self.__notes.append(note)
        self.notify()

    def delete_note(self, note: Note):
        self.notify()

    def modify_note(self, note: Note):
        self.notify()

    def notes(self):
        return self.__notes

    _observers: list[Observer] = []

    def attach(self, observer: Observer) -> None:
        self._observers.append(observer)

    def detach(self, observer: Observer) -> None:
        self._observers.remove(observer)

    def notify(self) -> None:
        for observer in self._observers:
            observer.update(self)


class Observer(ABC):
    @abstractmethod
    def update(self, subject: Subject) -> None:
        pass


class EmailSender(Observer):
    def update(self, subject: Subject) -> None:
        print(f'EmailSender: Send email with: {subject}')
