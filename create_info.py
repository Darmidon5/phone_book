import csv
import os


def sort_csv_file_by_column(filepath: str) -> None:
    """sort the csv file by reading it, sorting the list of lines by column_number and overwriting it
    takes 3 arguments: filename - name of file in the same directory that must be sorted,
    column_number - the number of the column to sort by,
    headers - headers of the csv file"""
    headers: list = ['ФИО', 'название организации', 'рабочий телефон', 'сотовый телефон']
    reader = csv.reader(open(filepath, encoding='utf-8'), delimiter=";")
    sortedlist = sorted(reader, key=lambda row: row[0])

    writer = csv.writer(open(filepath, mode='w', encoding='utf-8'), delimiter=';')
    if headers in sortedlist:
        sortedlist.remove(headers)
        writer.writerow(headers)
    [writer.writerow(i) for i in sortedlist]


def is_book_exists(filepath: str) -> bool:
    """take filename as an argument and check if it exists in current directory"""
    dir_path: str = os.path.dirname(os.path.realpath(__file__))
    return os.path.exists(dir_path + f'/{filepath}')


def create_book(filepath: str) -> None:
    """take filename as an argument and create a csv with this filename if it doesn't exist in current directory"""
    if not is_book_exists(filepath):
        with open(filepath, mode='w', encoding='utf-8') as file:
            writer = csv.writer(file, delimiter=';')
            writer.writerow(['ФИО', 'название организации', 'рабочий телефон', 'сотовый телефон'])


def add_row_to_file(row: list, filepath: str) -> None:
    """write a new row to csv file"""
    with open(filepath, mode='a', encoding='utf-8') as file:
        writer = csv.writer(file, delimiter=';')
        writer.writerow(row)
    sort_csv_file_by_column(filepath)
