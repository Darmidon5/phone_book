import os
import model


def test_data_to_display(test_sorted_phone_book) -> None:
    test_page_1 = model.data_to_display(0, test_sorted_phone_book)
    assert test_page_1[0][5] == 'a'
    assert test_page_1[9][5] == 'j'

    test_page_2 = model.data_to_display(1, test_sorted_phone_book)
    assert test_page_2[0][5] == 'k'
    assert test_page_2[9][5] == 't'

    test_page_3 = model.data_to_display(2, test_sorted_phone_book)
    assert test_page_3[0][5] == 'u'
    assert test_page_3[6] == 'Записей больше нет'


def test_find_rows(test_sorted_phone_book) -> None:
    empty_test_data = ([], [])
    keys, values = empty_test_data
    assert model.find_rows(keys, values, test_sorted_phone_book) == []

    full_test_data = (['ФИО', 'название организации', 'рабочий телефон', 'сотовый телефон'], ['a', '1', '1', '1'])
    keys, values = full_test_data
    result = model.find_rows(keys, values, test_sorted_phone_book)
    assert result[0]._aslist()[0] == 'a'

    one_key_test_data = (['ФИО'], ['a'])
    keys, values = one_key_test_data
    result = model.find_rows(keys, values, test_sorted_phone_book)
    assert result[0]._aslist()[0] == 'a'

    all_match_test_data = (['название организации'], ['1'])
    keys, values = all_match_test_data
    result = model.find_rows(keys, values, test_sorted_phone_book)
    assert len(result) == 26


def test_correct_finding_output(test_sorted_phone_book) -> None:
    empty_test_data = ([], [])
    assert model.correct_finding_output(empty_test_data, test_sorted_phone_book) == ['По вашему запросу ничего не найдено']

    full_test_data = (['ФИО', 'название организации', 'рабочий телефон', 'сотовый телефон'], ['a', '1', '1', '1'])
    result = model.correct_finding_output(full_test_data, test_sorted_phone_book)
    assert result[0][5] == 'a'
    assert len(result) == 1

    one_key_test_data = (['ФИО'], ['a'])
    result = model.correct_finding_output(one_key_test_data, test_sorted_phone_book)
    assert result[0][5] == 'a'
    assert len(result) == 1

    all_match_test_data = (['название организации'], ['1'])
    result = model.correct_finding_output(all_match_test_data, test_sorted_phone_book)
    assert len(result) == 26


def test_edit_row(test_phone_book) -> None:
    test_phone_book.clean_book(add_headers=True)

    test_data = [model.PhoneBookRecord(i, '1', '2', '3') for i in 'abc']
    [test_phone_book.add_row(row) for row in test_data]

    empty_test_data = ([], [])
    assert model.edit_row(empty_test_data, [], test_phone_book) == 'По вашему запросу ничего не найдено'

    all_match_test_data = ([test_phone_book.headers[1]], ['1'])
    assert model.edit_row(all_match_test_data, [], test_phone_book) == 'По вашему запросу найдено больше одной записи, редактирование невозможно'

    data_to_edit = (['ФИО'], ['a'])
    new_data = ['a', '2', '2', '2']
    ans = model.edit_row(data_to_edit, new_data, test_phone_book)
    assert ans == 'Изменения успешно применены'

    book_data = map(lambda row: row._aslist(), test_phone_book.read_csv())
    assert new_data in book_data
    assert ['a', '1', '2', '3'] not in book_data
    os.remove(test_phone_book.filename)
