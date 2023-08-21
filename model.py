import csv


def display_data():
    with open('client_data.csv', 'r', encoding='utf-8') as file:
        reader = csv.DictReader(file, delimiter=',')
        counter = 0
        for row in reader:
            counter += 1
            print(f"'ФИО': {row['ФИО']}, 'название организации': {row['название организации']}, 'рабочий телефон': {row['рабочий телефон']}, 'сотовый телефон': {row['сотовый телефон']}")

            if counter % 10 == 0:
                ans = input('Хотите вывести еще однц страницу? ("+" - Да, "-" - нет)')
                if ans == '-':
                    break
        else:
            print('Записей больше нет')


def find_row():
    key = input('Выберите поле, по которому хотите совершить поиск ("ФИО", "название организации", "рабочий телефон", "сотовый телефон")')
    while key not in ("ФИО", "название организации", "рабочий телефон", "сотовый телефон"):
        print('Введите корректное название ("ФИО", "название организации", "рабочий телефон", "сотовый телефон")')
    value = input('введите данные записи, которую хотите найти')
    with open('client_data.csv', 'r', encoding='utf-8') as file:
        reader = csv.DictReader(file, delimiter=',')
        ans = []
        for row in reader:
            if row[key] == value:
                ans.append(f"'ФИО': {row['ФИО']}, 'название организации': {row['название организации']}, 'рабочий телефон': {row['рабочий телефон']}, 'сотовый телефон': {row['сотовый телефон']}")
        print(*ans if ans else 'По вашему запросу ничего не найдено', sep='\n')