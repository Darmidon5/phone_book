import view
import create_info
import model
from model import PhoneBookRepository, PhoneBookRecord
from typing import List, NoReturn


def get_keys_from_input() -> tuple:
    key: str = input()
    while ':' not in key:
        key: str = input('Пожалуйста, введите запись в соответствии с образцом ')
    keys, values = [], []
    if ';' not in key:
        key, value = key.split(':')
        keys.append(key)
        values.append(value)
    else:
        for items in key.split(';'):
            key, value = items.split(':')
            keys.append(key)
            values.append(value)
    return keys, values


def are_keys_valid(keys: list, phone_book: PhoneBookRepository) -> bool:
    for key in keys:
        if key not in phone_book.headers:
            return False
    return True


def asking_for_valid_keys(phone_book: PhoneBookRepository) -> tuple:
    keys, values = get_keys_from_input()
    while not are_keys_valid(keys, phone_book):
        print(f'''Проверьте корректность полей введенных данных и введите их снова 
    {tuple(phone_book.headers)} ''')

        keys, values = get_keys_from_input()
    return keys, values


def validate_row_delimiter(row: str) -> str:
    while ';' not in row:
        row = input('пожалуйста, введите данные еще раз, разделив их знаком ";" ')
    return row


def validate_row(row: str, phone_book: PhoneBookRepository) -> PhoneBookRecord:
    validate_row_delimiter(row)
    valid_row: List[str] = row.split(';')
    while len(valid_row) < len(phone_book.headers):
        row: str = input(f'пожалуйста, введите данные еще раз, заполнив все колонки ({len(phone_book.headers)}) и разделив их знаком ";" ')
        validate_row_delimiter(row)
        valid_row = row.split(';')
    return PhoneBookRecord(*valid_row)


def phone_book(command, phone_book: PhoneBookRepository) -> NoReturn:
    if type(command) is str:
        if command == '1':
            ans: str = '+'
            page: int = 0
            while ans == '+':
                [print(i) for i in model.data_to_display(page, phone_book)]
                page += 1
                ans = input('Введите "+" если хотите увидеть еще одну страницу ')

        if command == '3':
            data_to_search: tuple = asking_for_valid_keys(phone_book)
            print('Теперь введите новые данные')
            new_data: PhoneBookRecord = validate_row(input('Введите ФИО, название организации, рабочий телефон и сотовый телефон абонента, разделив их знаком ";" '), phone_book)
            print(model.edit_row(data_to_search, new_data, phone_book))

        if command == '4':
            rows: List[str] = model.correct_finding_output(asking_for_valid_keys(phone_book), phone_book)
            [print(i) for i in rows]

    elif type(command) is tuple:
        command, input_data = command
        if command == '2':
            valid_row: PhoneBookRecord = validate_row(input_data, phone_book)
            create_info.add_row_to_file(valid_row, phone_book)


if __name__ == '__main__':
    clients_data: PhoneBookRepository = model.PhoneBookRepository('client_data.csv',
                                       ['ФИО', 'название организации', 'рабочий телефон', 'сотовый телефон'], ';')
    create_info.create_book(clients_data)
    try:
        while True:
            user_command = view.interaction()
            phone_book(user_command, clients_data)
    except KeyboardInterrupt:
        print('Спасибо, что выбрали нас!')
