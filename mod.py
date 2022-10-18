from view import get_replacement as replace
from view import get_new_people as new
from logger import load, save
from view import get_delite as delete
from view import get_search_data as search


def load_data():
    data = load()
    print('{:<13} {:<20} {:<12} {:<25} {:<18} {:<0}'.format('id', 'ФИО', 'Телефон', 'Дата рождения', 'Адрес', 'Паспорт'))
    for el in data:
        val = [v for v in el.values()]
        val[1] = val[1] + ' ' + val[2] + ' ' + val[3]
        val.pop(3)
        val.pop(2)
        print('{:<3} {:<28} {:<15} {:<15} {:<25} {:<15}'.format(val[0], val[1], val[2], val[3], val[4], val[5]))   

def delete_data():
    data = load()
    id = delete()
    for el in data:
        if el.get('id') == id:
            data.remove(el)
    save(data)
    print('Сотрудник удален')

def data_replacement():
    data = load()
    info = replace()
    for el in data:
        if el.get('id') == info[0]:
            el[info[1]] = info[2]
    save(data)
    print('Данные успешно изменены')

def add_new_people():
    new_man = new()
    bd = load()
    result = []
    for e in bd:
        result.append(e)
    result.append(new_man)
    save(result)
    print('\nСотрудник добавлен')

def data_search():
    data = load()
    info = search()
    for el in data:
        for k in el.keys():
            if el.get(k) == info:
                for key,value in el.items(): 
                    print("{:<15} {:<15}".format(key, value))