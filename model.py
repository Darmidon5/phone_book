import csv
from operator import itemgetter


class PhoneBookRepository:

    def __init__(self, filename, headers, delimiter, encoding='utf-8'):
        self.filename = filename
        self.headers = headers
        self.delimiter = delimiter
        self.encoding = encoding

    def read_csv(self) -> list:
        with open(self.filename, encoding=self.encoding) as file:
            reader = csv.reader(file, delimiter=self.delimiter)
            return list(reader)

    def read_dict_csv(self) -> list:
        dict_reader = csv.DictReader(self.file, delimiter=self.delimiter)
        return list(dict_reader)

    def add_row(self, row: str) -> None:
        with open(self.filename, mode='a', encoding=self.encoding) as file:
            writer = csv.writer(file, delimiter=';')
            writer.writerow(row)

    def clean_book(self, add_headers=False):
        with open(self.filename, mode='w', encoding=self.encoding) as file:
            writer = csv.writer(file, delimiter=';')
            if add_headers:
                writer.writerow(self.headers)

def data_to_display(page: int, filepath: str) -> list:
    """outputs the first 10 records from the 'client_data.csv' file, and requests the output of the next 10.
if there are not enough records, informs the user about it and stops working"""
    with open(filepath, 'r', encoding='utf-8') as file:
        reader = csv.reader(file, delimiter=';')
        rows = []
        list_of_rows = list(reader)[1+page * 10:]
        if not list_of_rows:
            return ['Записей больше нет']
        counter = 0
        for row in list_of_rows:
            rows.append(f"ФИО: {row[0]}, название организации: {row[1]}, 'рабочий телефон': {row[2]}, 'сотовый телефон': {row[3]}")
            counter += 1
            if counter == 10:
                break
        else:
            rows.append('Записей больше нет')
        return rows


def find_rows(keys: list, values: list, filepath: str) -> list:
    """accepts a list of keys and a list of values and
returns all the corresponding strings from the 'client_data.csv' file"""
    with open(filepath, 'r', encoding='utf-8') as file:
        reader = csv.DictReader(file, delimiter=';')
        ans = []
        if not keys or not values:
            return []
        for row in reader:
            all_match = []
            for idx in range(len(keys)):
                all_match.append(row[keys[idx]] == values[idx])
            if all(all_match):
                ans.append(row)
        return ans


def correct_finding_output(data_to_search: tuple, filepath: str) -> list:
    keys, values = data_to_search
    ans = [f"ФИО: {row['ФИО']}, название организации: {row['название организации']}, рабочий телефон: {row['рабочий телефон']}, сотовый телефон: {row['сотовый телефон']}" for row in find_rows(keys, values, filepath)]
    if not ans:
        return ['По вашему запросу ничего не найдено']
    else:
        return ans


def edit_row(data_to_search: tuple, new_data: list, filename: str) -> str:
    """accepts a row, finds it in the 'client_data.csv' file and overwrites it to the row that the user enters.
after that, it sorts the file."""
    keys, values = data_to_search
    ans = find_rows(keys, values, filename)
    if not ans:
        return 'По вашему запросу ничего не найдено'

    reader = csv.reader(open(filename), delimiter=";")
    rows_list = list(reader)
    rows_list.remove([*ans[0].values()])

    rows_list.append(new_data)
    sortedlist = sorted(rows_list, key=itemgetter(0))
    sortedlist.remove(['ФИО', 'название организации', 'рабочий телефон', 'сотовый телефон'])

    writer = csv.writer(open(filename, mode='w'), delimiter=';')
    writer.writerow(['ФИО', 'название организации', 'рабочий телефон', 'сотовый телефон'])
    [writer.writerow(i) for i in sortedlist]
    return 'Изменения успешно применены'
