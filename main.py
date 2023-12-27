# Author: Firsov Kirill
import argparse
import datetime

from models import Notebook, SimpleNote


def add_note(notebook: Notebook):
    print('Введите имя заметки: ')
    name = input()
    print('Введите описание заметки: ')
    description = input()
    print('Важная ли заметка(Да/Нет): ')
    important = input() == 'Да'
    note = SimpleNote(name, description, datetime.datetime.now(), important)
    notebook.add_note(note)


def delete_note(notebook):
    pass


def modify_note(notebook):
    pass


def notes(notebook):
    for note in notebook.notes():
        print(note)


def main():
    parser = argparse.ArgumentParser()
    subparsers = parser.add_subparsers()

    add_note_parser = subparsers.add_parser('add')
    add_note_parser.set_defaults(action=add_note)

    delete_note_parser = subparsers.add_parser('delete')
    delete_note_parser.set_defaults(action=delete_note)

    modify_note_parser = subparsers.add_parser('modify')
    modify_note_parser.set_defaults(action=modify_note)

    notes_parser = subparsers.add_parser('notes')
    notes_parser.set_defaults(action=notes)

    notebook = Notebook()

    args = parser.parse_args()
    args.action(notebook)


if __name__ == '__main__':
    main()
