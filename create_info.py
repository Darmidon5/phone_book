import csv
import os
from operator import itemgetter


def sort_csv_file_by_column(filename, column_number):
    '''sort the csv file by reading it, sorting the list of lines by column_number and overwriting it
    takes 3 arguments: filename - name of file in the same directory that must be sorted,
    column_number - the number of the column to sort by,
    headers - headers of the csv file'''
    reader = csv.reader(open(filename), delimiter=",")
    sortedlist = sorted(reader, key=itemgetter(column_number), reverse=True).remove(['ФИО', 'название организации', 'рабочий телефон', 'сотовый телефон'])
    writer = csv.writer(open(filename, mode='w'), delimiter=',')
    writer.writerow(['ФИО', 'название организации', 'рабочий телефон', 'сотовый телефон'])
    [writer.writerow(i) for i in sortedlist]
    return sortedlist


def is_book_exists(filename):
    '''check if the necessary file exists in current directory'''
    dir_path = os.path.dirname(os.path.realpath(__file__))
    return os.path.exists(dir_path + f'/{filename}')


def create_book(filename):
    '''create a csv with name of filename argument if it doesn't exist in current directory'''
    if not is_book_exists(filename):
        with open(filename, mode='w', encoding='utf-8') as file:
            writer = csv.writer(file, delimiter=',')
            writer.writerow(['ФИО', 'название организации', 'рабочий телефон', 'сотовый телефон'])


def create_data(row,  filename):
    '''write a new row to csv fiel'''
    with open(filename, mode='a', encoding='utf-8') as file:
        writer = csv.writer(file, delimiter=',')
        while True:
            row = row.split('; ')
            writer.writerow(row)
            ans = input('Хотите добавить еще одну запись ("+" - Да, "-" - нет)')
            if ans == '-':
                break
            row = input('Введите ФИО, название организации, рабочий телефон и сотовый телефон абонента, разделив их знаком ";"')
        sort_csv_file_by_column(filename, 0)


