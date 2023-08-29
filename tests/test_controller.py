from controller import phone_book, validate_row
import csv
import os


def test_validate_row() -> None:
    row = 'name; organization; phone1; phone2'
    assert validate_row(row) == ['name', 'organization', 'phone1', 'phone2']


def test_phone_book_2(test_filename: str) -> None:
    file = open(test_filename, 'w', encoding='utf-8')

    phone_book(('2', 'name; organization; phone1; phone2'), f'{test_filename}')

    reader = csv.reader(open(test_filename), delimiter=";")

    list_for_test = list(reader)
    assert len(list_for_test) == 1

    test_data: list = ['name', 'organization', 'phone1', 'phone2']
    assert test_data in list_for_test

    os.remove(test_filename)
