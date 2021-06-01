# MODULE: Строки

# BLOCK: Разделы в проге

about = '\nПрограмма для учета успеваемости учащихся\n'
main_menu = '''
Меню программы:

1. Информация об учащихся
2. Работа с оценками
3. Изучаемые дисциплины
4. Средний балл учащихся
5. Выход из программы
'''

header_1 = 'Информация об учащихся\n'
menu_1 = '''
1. Добавить нового учащегося
2. Изменить данные учащегося
3. Выход

'''

header_11 = 'Добавление нового учащегося\n'
menu_11 = '''
1. Добавить еще одного учащегося
2. Выход

'''

header_12 = 'Изменение информации об ученике\n'
menu_12 = '''
1. Изменить информацию об еще одном ученике
2. Выход

'''

header_2 = 'Работа с оценками\n'
menu_2 = '''
1. Добавить новую оценку
2. Показать в хронологическом порядке список полученных учеником оценок с указанием предмета
3. Список оценок учащегося, полученных в указанный интервал дат
4. Список аттестованных учеников в указанный период времени
5. Выход

'''

header_21 = 'Добавление новой оценки\n'
menu_21 = '''
1. Добавить еще одну оценку
2. Выход

'''

header_22 = 'Хронология полученных учеником оценок по предмету\n'
menu_22 = '''
1. Выбрать другого ученика и предмет
2. Выход

'''

header_23 = 'Список оценок учащегося, полученных в указанный интервал дат\n'
menu_23 = '''
1. Изменить заданные параметры
2. Выход

'''

header_24 = 'Список аттестованных учеников в указанный период времени\n'
menu_24 = '''
1. Изменить заданный период времени
2. Выход

'''

header_3 = 'Изучаемые дисциплины\n'
menu_3 = '''
1. Добавить новый предмет
2. Изменить существующий предмет
3. Выход

'''

header_31 = 'Добавление нового предмета\n'
menu_31 = '''
1. Добавить еще один предмет
2. Выход

'''

header_32 = 'Изменение информации о предмете\n'
menu_32 = '''
1. Изменить информацию о еще одном предмете
2. Выход

'''

header_4 = 'Средний балл учащихся\n'
menu_4 = '''
1. Показать средний балл учащихся по конкретному предмету
2. Показать учащихся, имеющих средний балл по предмету выше указанного
3. Выход

'''

header_41 = 'Средний балл учащихся по предмету\n'
menu_41 = '''
1. Показать средний балл по другому предмету
2. Выход

'''

header_42 = 'Список учащихся со средним баллом по предмету выше заданного\n'
menu_42 = '''
1. Выбрать другой предмет для просмотра
2. Выход

'''

# BLOCK: Интерфейсы

pupil_name = 'Введите имя ученика: '
pupil_surname = 'Введите фамилию ученика: '
pupil_address = 'Введите адрес ученика: '
pupil_id = 'Введите номер ученика: '

pupil_change_name = '''
Изменить имя?

1. Да
2. Нет

'''
pupil_change_surname = '''
Изменить фамилию?

1. Да
2. Нет

'''
pupil_change_address = '''
Изменить адрес?

1. Да
2. Нет

'''

mark_value = 'Введите полученную оценку: '
mark_subject = 'Введите номер предмета, по которому получена оценка: '
mark_pupil = 'Введите номер ученика, получившего оценку: '
mark_user = 'Введите значение: '

subject_id = 'Введите номер предмета: '
subject_name = 'Введите название дисциплины: '

date_day = 'Введите день: '
date_month = 'Введите месяц: '
date_year = 'Введите год: '
date_start = '\nДата начала интервала\n'
date_end = '\nКонечная дата интервала\n'

# BLOCK: ERROR

error_empty = 'ОШИБКА: ничего не было введено.\n'
error_nodigit = 'ОШИБКА: необходимо ввести число.\n'
error_wrong = 'ОШИБКА: введено неверное значение.\n'
error_nodate = 'ОШИБКА: неверная дата.\n'

# BLOCK: Работа с файлом

file_name = 'par.json'
file_path = 'par.json'