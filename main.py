# Author: Firsov Kirill
import argparse
import datetime

from models import SimpleNote, Notebook


def parse_args():
    parser = argparse.ArgumentParser(description='Process some integers.')
    parser.add_argument('action')

    args = parser.parse_args()

    return args.action


def main():
    action = parse_args()
    notebook = Notebook()
    note = SimpleNote("дз", "номер 123", datetime.datetime.now(), True)
    notebook.add_note(note)
    match action:
        case 'add':
            note = SimpleNote("дз", "номер 123", datetime.datetime.now(), True)
            notebook.add_note(note)
        case 'list':
            for note in notebook.notes():
                print(note)


if __name__ == '__main__':
    main()
