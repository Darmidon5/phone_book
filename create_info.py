import os


def sort_csv_file_by_column(phone_book) -> None:
    sortedlist = sorted(phone_book.read_csv(), key=lambda row: row[0])

    if phone_book.headers in sortedlist:
        sortedlist.remove(phone_book.headers)
        phone_book.clean_book(add_headers=True)
    else:
        phone_book.clean_book()

    [phone_book.add_row(i) for i in sortedlist]


def is_book_exists(filepath: str) -> bool:
    """take filename as an argument and check if it exists in current directory"""
    dir_path: str = os.path.dirname(os.path.realpath(__file__))
    return os.path.exists(dir_path + f'/{filepath}')


def create_book(phonebook) -> None:
    """take filename as an argument and create a csv with this filename if it doesn't exist in current directory"""
    if not is_book_exists(phonebook.filename):
        phonebook.clean_book(add_headers=True)


def add_row_to_file(row: list, phone_book) -> None:
    """write a new row to csv file"""
    phone_book.add_row(row)
    sort_csv_file_by_column(phone_book)
