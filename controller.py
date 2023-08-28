import view
import create_info
import model


def validate_row_delimiter(row: str) -> str:
    while ';' not in row:
        row = input('пожалуйста, введите данные еще раз, разделив их знаком ";"')
    return row


def validate_row(row: str) -> list:
    validate_row_delimiter(row)
    row = row.split('; ')
    while len(row) < 4:
        row = input('пожалуйста, введите данные еще раз, заполнив все 4 колонки и разделив их знаком ";"')
        validate_row_delimiter(row)
        row = row.split('; ')
    return row


def phone_book(command, filepath) -> None:
    """request a command from the user and call the function necessary to execute it"""
    if type(command) is str:
        if command == '1':
            model.display_data()
        if command == '3':
            model.edit_row()
        if command == '4':
            model.ask_for_key()

    elif type(command) is tuple:
        command, input_data = command
        if command == '2':
            row = input_data
            valid_row = validate_row(row)
            create_info.add_row_to_file(valid_row, filepath)


if __name__ == '__main__':
    phone_book_name: str = 'client_data.csv'
    create_info.create_book(phone_book_name)
    try:
        while True:
            user_command = view.interaction()
            phone_book(user_command, phone_book_name)
    except KeyboardInterrupt:
        print('Спасибо, что выбрали нас!')
