import csv
import os


def sort_csv_file_by_column() -> None:
    """sort the csv file by reading it, sorting the list of lines by column_number and overwriting it
    takes 3 arguments: filename - name of file in the same directory that must be sorted,
    column_number - the number of the column to sort by,
    headers - headers of the csv file"""
    reader = csv.reader(open('client_data.csv', encoding='utf-8'), delimiter=";")
    sortedlist = sorted(reader, key=lambda row: row[0], reverse=True)
    sortedlist.remove(['ФИО', 'название организации', 'рабочий телефон', 'сотовый телефон'])
    writer = csv.writer(open('client_data.csv', mode='w', encoding='utf-8'), delimiter=';')
    writer.writerow(['ФИО', 'название организации', 'рабочий телефон', 'сотовый телефон'])
    [writer.writerow(i) for i in sortedlist]


def is_book_exists() -> bool:
    """check if the necessary file exists in current directory"""
    dir_path = os.path.dirname(os.path.realpath(__file__))
    return os.path.exists(dir_path + '/client_data.csv')


def create_book() -> None:
    """create a csv with name of filename argument if it doesn't exist in current directory"""
    if not is_book_exists():
        with open('client_data.csv', mode='w', encoding='utf-8') as file:
            writer = csv.writer(file, delimiter=';')
            writer.writerow(['ФИО', 'название организации', 'рабочий телефон', 'сотовый телефон'])


def create_data(row: str) -> None:
    """write a new row to csv file"""
    with open('client_data.csv', mode='a', encoding='utf-8') as file:
        writer = csv.writer(file, delimiter=';')
        while True:
            row = row.split('; ')
            if len(row) < 4:
                print('пожалуйста, заполните все 4 колонки')
                break
            writer.writerow(row)
            ans = input('Хотите добавить еще одну запись ("+" - Да, "-" - нет)')
            while ans not in ['-', '+']:
                ans = input('Введите "+" если хотите добавить еще одну запись, в противном случае введите "-"')
            if ans == '-':
                break
            row = input('Введите ФИО, название организации, рабочий телефон и сотовый телефон абонента, разделив их знаком ";"')
        sort_csv_file_by_column()
