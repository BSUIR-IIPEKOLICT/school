# MODULE: Методы для оформления интерфейса

import datetime

from app.string import *

def header(text):
    print('-' * 80)
    print(text)

def enter(text):
    while True:
        rez = input(text)

        if not rez:
            print(error_empty)
            continue
        else:
            return rez

def enter_int(text, min = 0, max = 999):
    while True:
        rez = input(text)

        if not rez:
            print(error_empty)
            continue
        elif not rez.isdigit():
            print(error_nodigit)
            continue
        elif not min <= int(rez) <= max:
            print(error_wrong)
            continue
        else:
            return int(rez)

def enter_date(text = ''):
    print(text)
    
    while True:
        d = enter_int(date_day, 1, 31)
        m = enter_int(date_month, 1, 12)
        y = enter_int(date_year, 1900, 2100)

        try:
            datetime.date(y, m, d)
            date_str = datetime.datetime(y, m, d).strftime('%d.%m.%Y')
            return date_str
        except:
            print(error_nodate)
            continue

def convert_date(date_str):
    date = datetime.datetime.strptime(date_str, '%d.%m.%Y')
    return date

def interfase(instruction, menu):
    while True:
        instruction()

        a = input(menu)

        if int(a) == 1:
            continue
        else:
            break