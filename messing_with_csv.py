import csv
import faker


with open('client_data.csv', mode='w', encoding='utf-8') as file:
    writer = csv.writer(file, delimiter=',')
    writer.writerow(['ФИО', 'название организации', 'рабочий телефон', 'сотовый телефон'])
    fake = faker.Faker('ru_Ru')
    for _ in range(10):
        writer.writerow([fake.name(), fake.company(), fake.phone_number(), fake.phone_number()])