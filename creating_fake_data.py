import csv
import faker
from typing import NoReturn
import _csv


def create_data(n: int, filepath: str) -> NoReturn:
    with open(filepath, mode='w', encoding='utf-8') as file:
        writer: _csv.writer = csv.writer(file, delimiter=';')
        writer.writerow(['ФИО', 'название организации', 'рабочий телефон', 'сотовый телефон'])
        fake = faker.Faker('ru_Ru')
        for _ in range(n):
            writer.writerow([fake.name(), fake.company(), fake.phone_number(), fake.phone_number()])


if __name__ == '__main__':
    rows = int(input('Введите число записей, которое вы желаете сгенерировать '))
    filename = input('Введите название книги, которую хотите создать и заполнить ')
    create_data(rows, filename)
