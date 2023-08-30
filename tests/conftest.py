import pytest
import model
import os

@pytest.fixture
def test_filename() -> str:
    dir_path: str = os.path.dirname(os.path.realpath(__file__))
    test_filename = dir_path + f'/test_client_data.csv'
    # is_file_exists function checks this variable with os.path.isabs
    # if you violate its rules tests won't work
    # read official documentation before changing test_filename

    # also you should check test_controller
    return test_filename


@pytest.fixture
def test_phone_book():
    test_clients_data = model.PhoneBookRepository(os.path.dirname(os.path.realpath(__file__)) + '/test_client_data.csv',
                                             ['ФИО', 'название организации', 'рабочий телефон', 'сотовый телефон'], ';')
    return test_clients_data


@pytest.fixture
def test_sorted_phone_book():
    test_sorted_clients_data = model.PhoneBookRepository(os.path.dirname(os.path.realpath(__file__)) + '/sorted_csv',
                                             ['ФИО', 'название организации', 'рабочий телефон', 'сотовый телефон'], ';')
    return test_sorted_clients_data
