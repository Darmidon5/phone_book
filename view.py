

def interaction():
    '''request a comand from the user by asking him questions'''
    action = input('''Введите команду:
1 - вывод следующей страницы справочника
2 - добавить новую запись в справочник
3 - редактировать запись
4 - поиск записи  
    ''')

    if action == '1':
        return action

    if action == '2':
        text_input = input('Введите ФИО, название организации, рабочий телефон и сотовый телефон абонента, разделив их знаком ";"')
        return action, text_input

    if action == '3':
        print('''По образцу введите данные записи, которую хотите отредактировать
ФИО: Иванов Иван Иванович; название организации: ООО "ААА"; рабочий телефон: +7 666 555 44 33; сотовый телефон: +7 777 777 77 77
''')
        return action

    if action == '4':
        print('''Введите данные, по которым хотите совершить поиск вида: 
ФИО: Иванов Иван Иванович; название организации: ООО "ААА"; рабочий телефон: +7 666 555 44 33; сотовый телефон: +7 777 777 77 77
ввести данные можно как полностью так и отдельные поля, к примеру только ФИО''')
        return action
