import csv


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

    def add_row(self, row: list) -> None:
        with open(self.filename, mode='a', encoding=self.encoding) as file:
            writer = csv.writer(file, delimiter=';')
            writer.writerow(row)

    def read_dict_csv(self) -> list:
        with open(self.filename, encoding=self.encoding) as file:
            dict_reader = csv.DictReader(file, delimiter=self.delimiter)
            return list(dict_reader)

    def add_dict_row(self, row: dict) -> None:
        with open(self.filename, mode='a', encoding=self.encoding) as file:
            writer = csv.DictWriter(file, delimiter=';', fieldnames=self.headers)
            writer.writerow(row)

    def clean_book(self, add_headers=False):
        with open(self.filename, mode='w', encoding=self.encoding) as file:
            writer = csv.writer(file, delimiter=';')
            if add_headers:
                writer.writerow(self.headers)


def data_to_display(page: int, phone_book) -> list:
    rows = []
    list_of_rows = phone_book.read_csv()[1+page * 10:]
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


def find_rows(keys: list, values: list, phone_book) -> list:
    """accepts a list of keys and a list of values and
returns all the corresponding strings from the 'client_data.csv' file"""
    list_of_dicts = phone_book.read_dict_csv()
    ans = []
    if not keys or not values:
        return []
    for dict_ in list_of_dicts:
        all_match = []
        for idx in range(len(keys)):
            all_match.append(dict_[keys[idx]] == values[idx])
        if all(all_match):
            ans.append(dict_)
    return ans


def correct_finding_output(data_to_search: tuple, phone_book) -> list:
    keys, values = data_to_search
    ans = [f"ФИО: {row['ФИО']}, название организации: {row['название организации']}, рабочий телефон: {row['рабочий телефон']}, сотовый телефон: {row['сотовый телефон']}" for row in find_rows(keys, values, phone_book)]
    if not ans:
        return ['По вашему запросу ничего не найдено']
    else:
        return ans


def edit_row(data_to_search: tuple, new_data: list, phone_book) -> str:
    """accepts a row, finds it in the 'client_data.csv' file and overwrites it to the row that the user enters.
after that, it sorts the file."""
    keys, values = data_to_search
    ans = find_rows(keys, values, phone_book)
    if not ans:
        return 'По вашему запросу ничего не найдено'

    if len(ans) > 1:
        return 'По вашему запросу найдено больше одной записи, редактирование невозможно'

    list_of_dicts: list = phone_book.read_dict_csv()
    row_idx = list_of_dicts.index(ans)
    list_of_dicts[row_idx] = new_data

    phone_book.clean_book(add_headers=True)
    [phone_book.add_dict_row(row) for row in list_of_dicts]
    return 'Изменения успешно применены'
