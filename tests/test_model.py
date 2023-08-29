import csv
import os
import model


def test_data_to_display() -> None:
    test_page_1 = model.data_to_display(0, 'sorted_csv')
    assert test_page_1[0][5] == 'a'
    assert test_page_1[9][5] == 'j'

    test_page_2 = model.data_to_display(1, 'sorted_csv')
    assert test_page_2[0][5] == 'k'
    assert test_page_2[9][5] == 't'

    test_page_3 = model.data_to_display(2, 'sorted_csv')
    assert test_page_3[0][5] == 'u'
    assert test_page_3[6] == 'Записей больше нет'


def test_find_rows() -> None:
    test_filename = 'sorted_csv'
    empty_test_data = ([], [])
    keys, values = empty_test_data
    assert model.find_rows(keys, values, test_filename) == []

    full_test_data = (['ФИО', 'название организации', 'рабочий телефон', 'сотовый телефон'], ['a', '1', '1', '1'])
    keys, values = full_test_data
    result = model.find_rows(keys, values, test_filename)
    assert result[0]['ФИО'] == 'a'

    one_key_test_data = (['ФИО'], ['a'])
    keys, values = one_key_test_data
    result = model.find_rows(keys, values, test_filename)
    assert result[0]['ФИО'] == 'a'

    all_match_test_data = (['название организации'], ['1'])
    keys, values = all_match_test_data
    result = model.find_rows(keys, values, test_filename)
    assert len(result) == 26


def test_correct_finding_output() -> None:
    test_filename = 'sorted_csv'
    empty_test_data = ([], [])
    assert model.correct_finding_output(empty_test_data, test_filename) == ['По вашему запросу ничего не найдено']

    full_test_data = (['ФИО', 'название организации', 'рабочий телефон', 'сотовый телефон'], ['a', '1', '1', '1'])
    result = model.correct_finding_output(full_test_data, test_filename)
    assert result[0][5] == 'a'
    assert len(result) == 1

    one_key_test_data = (['ФИО'], ['a'])
    result = model.correct_finding_output(one_key_test_data, test_filename)
    assert result[0][5] == 'a'
    assert len(result) == 1

    all_match_test_data = (['название организации'], ['1'])
    result = model.correct_finding_output(all_match_test_data, test_filename)
    assert len(result) == 26


def test_edit_row(test_filename):
    with open(test_filename, 'w', encoding='utf-8') as file:
        writer = csv.writer(file, delimiter=';')
        test_data = [[i, 1, 2, 3] for i in 'abc']
        writer.writerow(['ФИО', 'название организации', 'рабочий телефон', 'сотовый телефон'])
        [writer.writerow(i) for i in test_data]

    empty_test_data = ([], [])
    assert model.edit_row(empty_test_data, [], test_filename) == 'По вашему запросу ничего не найдено'

    data_to_edit = (['ФИО'], ['a'])
    new_data = ['a', '2', '2', '2']
    ans = model.edit_row(data_to_edit, new_data, test_filename)
    assert ans == 'Изменения успешно применены'

    reader = csv.reader(open(test_filename), delimiter=';')
    assert new_data in list(reader)
    assert ['a', '1', '2', '3'] not in list(reader)
    os.remove(test_filename)
