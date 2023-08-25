import view
import create_info
import model


def phone_book() -> None:
    '''request a command from the user and call the function necessary to execute it'''
    filename = 'client_data.csv'

    interaction_info = view.interaction()
    if interaction_info[0] == '1':
        model.display_data()
    if interaction_info[0] == '2':
        create_info.create_data(interaction_info[1], filename)
    if interaction_info[0] == '3':
        model.edit_row()
    if interaction_info[0] == '4':
        model.ask_for_key()


if __name__ == '__main__':
    create_info.create_book('client_data.csv')
    while True:
        phone_book()
