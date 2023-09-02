import csv
from dataclasses import dataclass

from typing import NoReturn, List
import _csv


@dataclass
class PhoneBookRecord:
    """a @dataclass object representing row in phone book, takes 4 arguments:
    full_name: str
    organisation: str
    phone1: str
    phone2: str

    it has 2 methods:
    _aslist(self): returns list of object arguments values
    _asstr(self, headers): returns string mathes (<header>: <arg_value>, <header>: <arg_value>...) format"""
    full_name: str = ''
    organization: str = ''
    phone1: str = ''
    prone2: str = ''

    def _aslist(self) -> list:
        """_aslist(self): returns list of object arguments values"""
        data_dict: dict = vars(self)
        return [data_dict[i] for i in data_dict]

    def _asstr(self, headers: list) -> str:
        """_asstr(self, headers): returns string mathes (<header>: <arg_value>, <header>: <arg_value>...) format"""
        data: list = self._aslist()
        return ', '.join([f"{headers[idx]}: {data[idx]}" for idx in range(len(headers))])


class PhoneBookRepository:
    """class object representing phone book, takes 4 arguments:
    filename: filename or absolute path to file to store data in
    headers: headers to write in csv file
    delimiter: delimeter to read csv file
    encoding: encoding to read csv file

    has 3 methods:
    read_csv(): read self.filename csv ana return list of PhoneBookRecords
    add_row(row): takes PhoneBookRecord row  and writes it down to self.filename csv file
    clean_book(add_headers=False): wipe out ll the data from self.filename csv file
    if add_header is True - it will add header to file afterwards"""
    def __init__(self, filename, headers, delimiter, encoding='utf-8'):
        self.filename = filename
        self.headers = headers
        self.delimiter = delimiter
        self.encoding = encoding

    def read_csv(self) -> list:
        """open self.filename file and return list of its rows as PhoneBookRecord objects"""
        with open(self.filename, encoding=self.encoding) as file:
            reader: list = list(csv.reader(file, delimiter=self.delimiter))
            if self.headers in reader:
                reader.remove(self.headers)
            output: List[PhoneBookRecord] = [PhoneBookRecord(*row) for row in reader]
            return output

    def add_row(self, row: PhoneBookRecord) -> NoReturn:
        """take PhoneBookRecord as an argument and adds it to self.filename file"""
        with open(self.filename, mode='a', encoding=self.encoding) as file:
            writer: _csv.writer = csv.writer(file, delimiter=';')
            writer.writerow(row._aslist())

    def clean_book(self, add_headers=False) -> NoReturn:
        """remove all the rows from self.filename file.
        Will add headers to a file if add_headers argument is True"""
        with open(self.filename, mode='w', encoding=self.encoding) as file:
            writer: _csv.writer = csv.writer(file, delimiter=';')
            if add_headers:
                writer.writerow(self.headers)


def data_to_display(page: int, phone_book: PhoneBookRepository) -> List[str]:
    """get 10 rows from phone book according to their page. will return 'Записей больше нет' as final row
    takes two arguments:
    page - shows the sequence number of a group of ten records extracted from the file
    phone_book - an object of PhoneBookRepository class"""
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
    """takes tuple containing list of keys and list of values and returns all mathicng rows from PhoneBookRepository"""
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
    """takes tuple containing list of keys and list of values
     and returns all mathicng rows from PhoneBookRepository as strings
    takes 2 arguments:
    data_to_search - tuple of two lists - keys and matching values to look for
    phone_book - PhoneBookRepository object"""
    ans: List[str] = [row._asstr(phone_book.headers) for row in find_rows(data_to_search, phone_book)]
    if not ans:
        return ['По вашему запросу ничего не найдено']
    else:
        return ans


def edit_row(data_to_search: tuple, new_data: PhoneBookRecord, phone_book: PhoneBookRepository) -> str:
    """edit a row in PhoneBookRepository
    takes 3 arguments:
    data_to_search - tuple of two lists - keys and matching values to look for
    new_data - PhoneBookRecord object to replace the line being edited
    phone_book - PhoneBookRepository object"""
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
