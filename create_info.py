import csv
import os
from operator import itemgetter
import faker


def sort_book(filename):
    reader = csv.reader(open(filename), delimiter=",")
    sortedlist = sorted(reader, key=itemgetter(0), reverse=True)
    writer = csv.writer(open(filename, mode='w'), delimiter=',')
    [writer.writerow(i) for i in sortedlist]
    return sortedlist


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
        sort_book('client_data.csv')


with open('client_data.csv', mode='a', encoding='utf-8') as file:
    writer = csv.writer(file, delimiter=',')
    writer.writerow(['ФИО', 'название организации', 'рабочий телефон', 'сотовый телефон'])
    fake = faker.Faker('ru_Ru')
    for _ in range(100):
        writer.writerow([fake.name(), fake.company(), fake.phone_number(), fake.phone_number()])