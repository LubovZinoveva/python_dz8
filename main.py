from mod import delete_data as delete
from mod import data_replacement as replace
from mod import add_new_people as add
from mod import data_search as search
from mod import load_data as load

def select_mod():
    print('РЕЖИМЫ\n1. Открыть базу для просмотра\n2. Удалить данные о сотруднике\n3. Внести изменения\n4. Добавить сотрудника\n5. Найти сотрудника')
    choose = int(input('Выберите номер режима: '))
    print()
    match choose:
        case 1:
            load()
        case 2:
            delete()
        case 3:
            replace()
        case 4:
            add()
        case 5:
            search()

select_mod()