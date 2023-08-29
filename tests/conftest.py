import pytest


@pytest.fixture
def test_filename() -> str:
    test_filename = '/home/darmidon/projects/phone_book/tests/test_client_data.csv'
    # is_file_exists function checks this variable with os.path.isabs
    # if you violate its rules tests won't work
    # read official documentation before changing test_filename

    # also you should check test_controller
    return test_filename
