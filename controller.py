import view
import create_info
import model


def get_keys_from_input() -> tuple:
    """accepts a string containing key-value pairs separated by a colon.
if there are several pairs, they should be separated by a ';' sign. returns a list of keys and a list of values"""

    key = input()
    while ':' not in key:
        key = input('Пожалуйста, введите запись в соответствии с образцом')
    keys, values = [], []
    if ';' not in key:
        key, value = key.split(': ')
        keys.append(key)
        values.append(value)
    else:
        for items in key.split('; '):
            key, value = items.split(': ')
            keys.append(key)
            values.append(value)
    return keys, values


def are_keys_valid(keys: list) -> bool:
    """accepts a list of keys and checks them against the contained list of headers of the csv file 'client_data.csv'.
returns False if it finds a mismatch"""
    for key in keys:
        if key not in ("ФИО", "название организации", "рабочий телефон", "сотовый телефон"):
            return False
    return True


def asking_for_valid_keys() -> tuple:
    """returns valid list of keys and list of values from input"""
    keys, values = get_keys_from_input()
    while not are_keys_valid(keys):
        print('''Проверьте корректность полей введенных данных и введите их снова 
    ("ФИО", "название организации", "рабочий телефон", "сотовый телефон")''')

        keys, values = get_keys_from_input()
    return keys, values


def validate_row_delimiter(row: str) -> str:
    while ';' not in row:
        row = input('пожалуйста, введите данные еще раз, разделив их знаком ";" ')
    return row


def validate_row(row: str) -> list:
    validate_row_delimiter(row)
    row = row.split('; ')
    while len(row) < 4:
        row = input('пожалуйста, введите данные еще раз, заполнив все 4 колонки и разделив их знаком ";" ')
        validate_row_delimiter(row)
        row = row.split('; ')
    return row


def phone_book(command, filename) -> None:
    """request a command from the user and call the function necessary to execute it"""
    if type(command) is str:
        if command == '1':
            ans = '+'
            page = 0
            while ans == '+':
                [print(i) for i in model.data_to_display(page, filename)]
                page += 1
                ans = input('Введите "+" если хотите увидеть еще одну страницу')
        if command == '3':
            model.edit_row()
        if command == '4':
            model.ask_for_key(asking_for_valid_keys())

    elif type(command) is tuple:
        command, input_data = command
        if command == '2':
            row = input_data
            valid_row = validate_row(row)
            create_info.add_row_to_file(valid_row, filename)


if __name__ == '__main__':
    phone_book_name: str = 'client_data.csv'
    create_info.create_book(phone_book_name)
    try:
        while True:
            user_command = view.interaction()
            phone_book(user_command, phone_book_name)
    except KeyboardInterrupt:
        print('Спасибо, что выбрали нас!')
