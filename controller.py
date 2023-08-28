import view
import create_info
import model


def validate_row(row):
    while ';' not in row:
        row = input('пожалуйста, введите данные еще раз, разделив их знаком ";"')
    row = row.split('; ')
    while len(row) < 4:
        row = input('пожалуйста, введите данные еще раз, заполнив все 4 колонки и разделив их знаком ";"')
        row = row.split('; ')
    return row

def phone_book() -> None:
    """request a command from the user and call the function necessary to execute it"""

    interaction_info = view.interaction()
    if interaction_info[0] == '1':
        model.display_data()
    if interaction_info[0] == '2':
        row = interaction_info[1]
        valid_row = validate_row(row)
        create_info.create_data(valid_row, 'client_data.csv')
    if interaction_info[0] == '3':
        model.edit_row()
    if interaction_info[0] == '4':
        model.ask_for_key()


if __name__ == '__main__':
    create_info.create_book('client_data.csv')
    try:
        while True:
            phone_book()
    except KeyboardInterrupt:
        print('Спасибо, что выбрали нас!')
