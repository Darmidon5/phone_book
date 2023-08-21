import csv
import os


def is_book_exists():
    dir_path = os.path.dirname(os.path.realpath(__file__))
    return os.path.exists(dir_path + '/client_data.csv')


def create_data(row):
    if not is_book_exists():
        with open('client_data.csv', mode='w', encoding='utf-8') as file:
            writer = csv.writer(file, delimiter=',')
            writer.writerow(['ФИО', 'название организации', 'рабочий телефон', 'сотовый телефон'])
    with open('client_data.csv', mode='a', encoding='utf-8') as file:
        writer = csv.writer(file, delimiter=',')
        ans = '+'
        while ans == '+':
            row = row.split(', ')
            writer.writerow(row)
            ans = input('Хотите добавить еще одну запись ("+" - Да, "-" - нет)')




print(os.path.dirname(os.path.realpath(__file__)))
