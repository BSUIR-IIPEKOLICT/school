import datetime

from app.string import *

class Ui:
    def divider():
        print('-' * 80)

    def header(text):
        Ui.divider()
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
            d = Ui.enter_int(date_day, 1, 31)
            m = Ui.enter_int(date_month, 1, 12)
            y = Ui.enter_int(date_year, 1900, 2100)

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
    
    def interfase_loop(instruction, write, menu):
        while True:
            instruction()

            if write:
                # FIXME: Запись изменений в файл с параметрами
                pass

            a = input(menu)

            if int(a) == 1:
                continue
            else:
                break