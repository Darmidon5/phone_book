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

