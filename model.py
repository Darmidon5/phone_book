import csv
from dataclasses import dataclass

from typing import NoReturn, List
import _csv


@dataclass
class PhoneBookRecord:
    full_name: str = ''
    organization: str = ''
    phone1: str = ''
    prone2: str = ''

    def _aslist(self) -> list:
        data_dict: dict = vars(self)
        return [data_dict[i] for i in data_dict]

    def _asstr(self, headers: list) -> str:
        data: list = self._aslist()
        return ', '.join([f"{headers[idx]}: {data[idx]}" for idx in range(len(headers))])


class PhoneBookRepository:
    def __init__(self, filename, headers, delimiter, encoding='utf-8'):
        self.filename = filename
        self.headers = headers
        self.delimiter = delimiter
        self.encoding = encoding

    def read_csv(self) -> list:
        with open(self.filename, encoding=self.encoding) as file:
            reader: list = list(csv.reader(file, delimiter=self.delimiter))
            if self.headers in reader:
                reader.remove(self.headers)
            output: List[PhoneBookRecord] = [PhoneBookRecord(*row) for row in reader]
            return output

    def add_row(self, row: PhoneBookRecord) -> NoReturn:
        with open(self.filename, mode='a', encoding=self.encoding) as file:
            writer: _csv.writer = csv.writer(file, delimiter=';')
            writer.writerow(row._aslist())

    def clean_book(self, add_headers=False) -> NoReturn:
        with open(self.filename, mode='w', encoding=self.encoding) as file:
            writer: _csv.writer = csv.writer(file, delimiter=';')
            if add_headers:
                writer.writerow(self.headers)


def data_to_display(page: int, phone_book: PhoneBookRepository) -> List[str]:
    rows: list = []
    list_of_rows: List[PhoneBookRecord] = phone_book.read_csv()[page * 10:]
    if not list_of_rows:
        return ['Записей больше нет']
    counter: int = 0
    for row in list_of_rows:
        rows.append(row._asstr(phone_book.headers))
        counter += 1
        if counter == 10:
            break
    else:
        rows.append('Записей больше нет')
    return rows


def find_rows(data_to_search, phone_book: PhoneBookRepository) -> List[PhoneBookRecord]:
    keys, values = data_to_search
    keys: List[int] = [phone_book.headers.index(key) for key in keys]
    list_of_recs: List[PhoneBookRecord] = phone_book.read_csv()
    ans: List[PhoneBookRecord] = []
    if not keys or not values:
        return []
    for record in list_of_recs:
        all_match = []
        for idx in range(len(keys)):
            all_match.append(record._aslist()[keys[idx]] == values[idx])
        if all(all_match):
            ans.append(record)
    return ans


def correct_finding_output(data_to_search: tuple, phone_book: PhoneBookRepository) -> List[str]:
    ans: List[str] = [row._asstr(phone_book.headers) for row in find_rows(data_to_search, phone_book)]
    if not ans:
        return ['По вашему запросу ничего не найдено']
    else:
        return ans


def edit_row(data_to_search: tuple, new_data: PhoneBookRecord, phone_book: PhoneBookRepository) -> str:
    ans: List[PhoneBookRecord] = find_rows(data_to_search, phone_book)
    if not ans:
        return 'По вашему запросу ничего не найдено'

    if len(ans) > 1:
        return 'По вашему запросу найдено больше одной записи, редактирование невозможно'

    list_of_dicts: List[PhoneBookRecord] = phone_book.read_csv()
    row_idx: int = list_of_dicts.index(*ans)
    list_of_dicts[row_idx] = new_data

    phone_book.clean_book(add_headers=True)
    [phone_book.add_row(row) for row in list_of_dicts]
    return 'Изменения успешно применены'
