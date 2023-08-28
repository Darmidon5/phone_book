from controller import phone_book
import csv
import os


def test_phone_book(test_filename: str) -> None:
    file = open(test_filename, 'w', encoding='utf-8')

    phone_book((2, 'name; organization; phone1; phone2'), f'/tests/{test_filename}')
    test_data: list = ['name', 'organization', 'phone1', 'phone2']

    reader = csv.reader(open(test_filename), delimiter=";")
    list_for_test = list(reader)

    assert len(list_for_test) == 1
    assert test_data in list_for_test
    os.remove(test_filename)
