

def get_delite():
    id = input('Введите id сотрудника для удаления из базы: ')
    return id

def get_replacement():
    result = []
    result.append(input('Введите id сотрудника: '))
    result.append(input('Какой столбец меняем: '))
    result.append(input('Новые данные: '))
    return result

def get_new_people():
    print('Заполните поля:')
    man = {}
    man = \
        {
            'id' : input('id = '),
            'Фамилия' : input('Фамилия = '),
            'Имя' : input('Имя = '),
            'Отчество' : input('Отчество = '),
            'Телефон' : input('Телефон = '),
            'Дата рождения' : input('Дата рождения = '),
            'Адрес': input('Адрес = '),
            'Паспорт' : input('Паспорт = ')
        }
    return man 

def get_search_data():
    info = input('Введите информацию о сотруднике: ')
    return info