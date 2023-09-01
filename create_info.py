import os
from model import PhoneBookRecord, PhoneBookRepository
from typing import NoReturn


def sort_csv_file_by_column(phone_book: PhoneBookRepository) -> NoReturn:
    sortedlist = sorted(phone_book.read_csv(), key=lambda row: row._aslist())

    phone_book.clean_book()
    [phone_book.add_row(i) for i in sortedlist]


def is_book_exists(filepath: str) -> bool:
    """check if file exists in current directory by filename"""
    dir_path: str = os.path.dirname(os.path.realpath(__file__))
    return os.path.exists(dir_path + f'/{filepath}')


def create_book(phonebook: PhoneBookRepository) -> NoReturn:
    """create a csv with filename argument if it doesn't exist in current directory"""
    if not is_book_exists(phonebook.filename):
        phonebook.clean_book(add_headers=True)


def add_row_to_file(row: PhoneBookRecord, phone_book: PhoneBookRepository) -> NoReturn:
    """write a new row to csv file"""
    phone_book.add_row(row)
    sort_csv_file_by_column(phone_book)
