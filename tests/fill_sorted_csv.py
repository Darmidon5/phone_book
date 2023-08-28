import csv
from string import ascii_lowercase


def create_test_data(filepath: str) -> None:
    """accepts a numeric argument and filename and creates a phonebook in the form of a csv file with the number of filled lines
    equal to it"""
    with open(filepath, mode='w', encoding='utf-8') as file:
        writer = csv.writer(file, delimiter=';')
        writer.writerow(['ФИО', 'название организации', 'рабочий телефон', 'сотовый телефон'])
        for letter in ascii_lowercase:
            writer.writerow([letter, 1, 1, 1])


if __name__ == '__main__':
    create_test_data('sorted_csv')
