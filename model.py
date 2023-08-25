import csv
from operator import itemgetter


def display_data():
    '''outputs the first 10 records from the 'client_data.csv' file, and requests the output of the next 10. if there are not enough records, informs the user about it and stops working'''
    with open('client_data.csv', 'r', encoding='utf-8') as file:
        reader = csv.DictReader(file, delimiter=',')
        counter = 0
        for row in reader:
            counter += 1
            print(f"ФИО: {row['ФИО']}, название организации: {row['название организации']}, 'рабочий телефон': {row['рабочий телефон']}, 'сотовый телефон': {row['сотовый телефон']}")

            if counter % 10 == 0:
                ans = input('Хотите вывести еще однц страницу? ("+" - Да, "-" - нет)')
                if ans == '-':
                    break
        else:
            print('Записей больше нет')


def get_keys_from_input():
    '''accepts a string containing key-value pairs separated by a colon. if there are several pairs, they should be separated by a ';' sign. returns a list of keys and a list of values'''
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
    '''accepts a list of keys and checks them against the contained list of headers of the csv file 'client_data.csv'. returns False if it finds a mismatch'''
    for key in keys:
        if key not in ("ФИО", "название организации", "рабочий телефон", "сотовый телефон"):
            return False
    return True


def asking_for_valid_keys():
    '''contains a function that returns lists of keys and values from the input. requests re-entry if there is an error in the keys'''
    keys, values = get_keys_from_input()
    while not are_keys_valid(keys):
        print('Проверьте корректность полей введенных данных и введите их снова ("ФИО", "название организации", "рабочий телефон", "сотовый телефон")')
        keys, values = get_keys_from_input()
    return keys, values


def find_rows(keys, values):
    '''accepts a list of keys and a list of values and returns all the corresponding strings from the 'client_data.csv' file'''
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
    '''requests a string containing key-value pairs from the user. divides it into a list of keys and a list of values, checks their correctness and searches for the corresponding record. If records are found, it outputs them. otherwise, notifies the user about the absence of relevant records'''
    keys, values = asking_for_valid_keys()
    ans = [f"ФИО: {row['ФИО']}, название организации: {row['название организации']}, рабочий телефон: {row['рабочий телефон']}, сотовый телефон: {row['сотовый телефон']}" for row in find_rows(keys, values)]
    if ans:
        print(*ans, sep='\n')
    else:
        print('По вашему запросу ничего не найдено')


def edit_row():
    '''accepts an entry, finds it in the 'client_data.csv' file and overwrites it to the line that the user enters. after that, it sorts the file.'''
    keys, values = asking_for_valid_keys()
    ans = find_rows(keys, values)

    reader = csv.reader(open('client_data.csv'), delimiter=",")
    rows_list = list(reader)
    if not ans:
        print('По вашему запросу ничего не найдено')
        return False
    rows_list.remove([*ans[0].values()])

    row = input('Пожалуйста, введите измененные данные')
    print(row)
    row = [items.split(': ')[1] for items in row.split('; ')]
    print(row)
    rows_list.append(row)
    sortedlist = sorted(rows_list, key=itemgetter(0))
    sortedlist.remove(['ФИО', 'название организации', 'рабочий телефон', 'сотовый телефон'])

    writer = csv.writer(open('client_data.csv', mode='w'), delimiter=',')
    writer.writerow(['ФИО', 'название организации', 'рабочий телефон', 'сотовый телефон'])
    [writer.writerow(i) for i in sortedlist]
