import csv
import os
from operator import itemgetter



def sort_book(filename):
    reader = csv.reader(open(filename), delimiter=",")
    sortedlist = sorted(reader, key=itemgetter(0), reverse=True).remove(['ФИО', 'название организации', 'рабочий телефон', 'сотовый телефон'])
    writer = csv.writer(open(filename, mode='w'), delimiter=',')
    writer.writerow(['ФИО', 'название организации', 'рабочий телефон', 'сотовый телефон'])
    [writer.writerow(i) for i in sortedlist]
    return sortedlist


def is_book_exists():
    dir_path = os.path.dirname(os.path.realpath(__file__))
    return os.path.exists(dir_path + '/client_data.csv')


def create_book():
    if not is_book_exists():
        with open('client_data.csv', mode='w', encoding='utf-8') as file:
            writer = csv.writer(file, delimiter=',')
            writer.writerow(['ФИО', 'название организации', 'рабочий телефон', 'сотовый телефон'])


def create_data(row):
    with open('client_data.csv', mode='a', encoding='utf-8') as file:
        writer = csv.writer(file, delimiter=',')
        ans = '+'
        while ans == '+':
            row = row.split(', ')
            writer.writerow(row)
            ans = input('Хотите добавить еще одну запись ("+" - Да, "-" - нет)')
        sort_book('client_data.csv')


