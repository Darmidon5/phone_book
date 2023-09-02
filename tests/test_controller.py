from controller import phone_book, validate_row
import os
import model


def test_validate_row(test_phone_book) -> None:
    row = 'name; organization; phone1; phone2'
    assert validate_row(row, test_phone_book) == model.PhoneBookRecord('name', 'organization', 'phone1', 'phone2')


def test_phone_book_2(test_phone_book) -> None:
    test_phone_book.clean_book()

    phone_book(('2', 'name; organization; phone1; phone2'), test_phone_book)

    reader = test_phone_book.read_csv()

    assert len(reader) == 1

    test_data: model.PhoneBookRecord = model.PhoneBookRecord('name', 'organization', 'phone1', 'phone2')
    assert test_data in reader

    os.remove(test_phone_book.filename)
