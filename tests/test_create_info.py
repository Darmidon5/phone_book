from create_info import is_book_exists, create_book, sort_csv_file_by_column, create_data
from test_creating_fake_data import is_file_exists
import csv
import os
from string import ascii_lowercase
from random import shuffle


test_filename = 'test_client_data.csv'
sorting_test_filename = 'test_csv'


def test_is_book_exists() -> None:
    assert is_book_exists('tests/test_creating_fake_data.py')


def test_create_book() -> None:
    create_book(test_filename)
    assert is_file_exists(test_filename)

    reader = csv.reader(open(test_filename), delimiter=";")
    row_count: int = sum(1 for row in reader)
    assert row_count == 1

    os.remove(test_filename)
    assert not is_file_exists(test_filename)


def create_messed_csv() -> None:
    with open(sorting_test_filename, 'w', encoding='utf-8') as file:
        writer = csv.writer(file, delimiter=';')
        writer.writerow(['ФИО', 'название организации', 'рабочий телефон', 'сотовый телефон'])
        random_letters: list = [i for i in ascii_lowercase]
        shuffle(random_letters)
        for i in random_letters:
            writer.writerow([i, 1, 1, 1])


def test_sort_csv_file_by_column() -> None:
    create_messed_csv()

    sorted_rows = open('sorted_csv', 'r', encoding='utf-8').readlines()

    sort_csv_file_by_column(sorting_test_filename)
    test_reader = open(sorting_test_filename, 'r', encoding='utf-8').readlines()

    counter = 0
    all_match = []
    for row in sorted_rows:
        all_match.append(row == test_reader[counter])
        counter += 1
    assert all(all_match)

    os.remove(sorting_test_filename)
    assert not is_file_exists(sorting_test_filename)
