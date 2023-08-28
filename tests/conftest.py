import pytest


@pytest.fixture
def test_filename() -> str:
    test_filename = 'test_client_data.csv'
    return test_filename

