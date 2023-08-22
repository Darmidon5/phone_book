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


def get_keys_from_input():
    key = input()
    keys, values = [], []
    if ';' not in key:
        key, value = key.split(': ')
        keys.append(key)
        values.append(value)
    else:
        for items in key.split('; '):
            key, value = items.split(': ')
            keys.append(key)
            values.append(value)
    return keys, values


def are_keys_valid(keys):
    for key in keys:
        if key not in ("ФИО", "название организации", "рабочий телефон", "сотовый телефон"):
            return False
    return True


def find_rows(keys, values):
    with open('client_data.csv', 'r', encoding='utf-8') as file:
        reader = csv.DictReader(file, delimiter=',')
        ans = []
        for row in reader:
            all_match = []
            for idx in range(len(keys)):
                all_match.append(row[keys[idx]] == values[idx])
            if all(all_match):
                ans.append(row)
        return ans


def ask_for_key():
    keys, values = get_keys_from_input()
    while not are_keys_valid(keys):
        print('Проверьте корректность полей введенных данных и введите их снова ("ФИО", "название организации", "рабочий телефон", "сотовый телефон")')
        keys, values = get_keys_from_input()
    ans = [f"'ФИО': {row['ФИО']}, 'название организации': {row['название организации']}, 'рабочий телефон': {row['рабочий телефон']}, 'сотовый телефон': {row['сотовый телефон']}" for row in find_rows(keys, values)]
    if ans:
        print(*ans, sep='\n')
    else:
        print('По вашему запросу ничего не найдено')



