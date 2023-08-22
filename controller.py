import view
import create_info
import model


def phone_book():
    interaction_info = view.interaction()
    if interaction_info[0] == '1':
        model.display_data()
    if interaction_info[0] == '2':
        create_info.create_data(interaction_info[1])
    if interaction_info[0] == '3':
        model.edit_row()
    if interaction_info[0] == '4':
        model.ask_for_key()


create_info.create_book()
while True:
    phone_book()
