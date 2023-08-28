import csv
import faker


def create_data(n: int, filepath: str) -> None:
    """accepts a numeric argument and filename and creates a phonebook in the form of a csv file with the number of filled lines
    equal to it"""
    with open(filepath, mode='w', encoding='utf-8') as file:
        writer = csv.writer(file, delimiter=';')
        writer.writerow(['ФИО', 'название организации', 'рабочий телефон', 'сотовый телефон'])
        fake = faker.Faker('ru_Ru')
        for _ in range(n):
            writer.writerow([fake.name(), fake.company(), fake.phone_number(), fake.phone_number()])


if __name__ == '__main__':
    rows = int(input('Введите число записей, которое вы желаете сгенерировать'))
    filename = input('Введите путь до книги, которую хотите создать и заполнить')
    create_data(rows, filename)
