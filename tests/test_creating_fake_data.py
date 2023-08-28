from creating_fake_data import create_data
import os
import csv

test_filename = 'test_client_data.csv'


def is_file_exists(filename: str) -> bool:
    """take filename as an argument and check if it exists in current directory"""
    dir_path: str = os.path.dirname(os.path.realpath(__file__))
    return os.path.exists(dir_path + f'/{filename}')


def test_create_data() -> None:
    rows_amount_without_headers: int = 20
    create_data(rows_amount_without_headers, test_filename)
    assert is_file_exists(test_filename)

    reader = csv.reader(open(test_filename), delimiter=";")
    row_count: int = sum(1 for row in reader)
    assert row_count == rows_amount_without_headers + 1

    os.remove(test_filename)
    assert not is_file_exists(test_filename)
