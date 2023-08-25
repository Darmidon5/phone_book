import csv
import faker


def create_data(n: int) -> None:
    """accepts a numeric argument and creates a phonebook in the form of a csv file with the number of filled lines
    equal to it"""
    with open('client_data.csv', mode='w', encoding='utf-8') as file:
        writer = csv.writer(file, delimiter=',')
        writer.writerow(['ФИО', 'название организации', 'рабочий телефон', 'сотовый телефон'])
        fake = faker.Faker('ru_Ru')
        for _ in range(n):
            writer.writerow([fake.name(), fake.company(), fake.phone_number(), fake.phone_number()])
