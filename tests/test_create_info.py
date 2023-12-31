from create_info import is_book_exists, create_book, sort_csv_file_by_column, add_row_to_file
from test_creating_fake_data import is_file_exists
import csv
import os
from string import ascii_lowercase
from random import shuffle
from model import PhoneBookRecord

def test_is_book_exists() -> None:
    assert is_book_exists('tests/test_creating_fake_data.py')


def test_create_book(test_phone_book) -> None:
    create_book(test_phone_book)
    assert is_file_exists(test_phone_book.filename)

    list_of_rows = test_phone_book.read_csv()
    row_count: int = len(list_of_rows)
    assert row_count == 0

    os.remove(test_phone_book.filename)
    assert not is_file_exists(test_phone_book.filename)


def create_messed_csv(filename: str) -> None:
    with open(filename, 'w', encoding='utf-8') as file:
        writer = csv.writer(file, delimiter=';')
        writer.writerow(['ФИО', 'название организации', 'рабочий телефон', 'сотовый телефон'])
        random_letters: list = [i for i in ascii_lowercase]
        shuffle(random_letters)
        for i in random_letters:
            writer.writerow([i, 1, 1, 1])


def test_sort_csv_file_by_column(test_filename, test_sorted_phone_book, test_phone_book) -> None:
    create_messed_csv(test_filename)

    sorted_rows = list(test_sorted_phone_book.read_csv())

    sort_csv_file_by_column(test_phone_book)
    test_reader = test_phone_book.read_csv()

    all_match = []
    for idx in range(len(sorted_rows)):
        all_match.append(sorted_rows[idx] == test_reader[idx])
    assert all(all_match)

    os.remove(test_filename)
    assert not is_file_exists(test_filename)


def test_add_row_to_file(test_filename: str, test_phone_book) -> None:
    file = open(test_filename, 'w', encoding='utf-8')
    test_data: PhoneBookRecord = PhoneBookRecord('name', 'organization', 'phone1', 'phone2')
    add_row_to_file(test_data, test_phone_book)

    reader = csv.reader(open(test_filename), delimiter=";")
    list_for_test = list(reader)

    assert len(list_for_test) == 1
    assert test_data._aslist() in list_for_test

    os.remove(test_filename)
