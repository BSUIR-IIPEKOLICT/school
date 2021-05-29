from app.string import error_empty, error_nodigit, error_wrong

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

    def enterInt(text, min = 0, max = 9999):
        while True:
            rez = input(text)

            if not rez:
                print(error_empty)
                continue
            elif not rez.isdigit():
                print(error_nodigit)
                continue
            elif not min < rez < max:
                print(error_wrong)
                continue
            else:
                return int(rez)
    
    def interfase_loop(func, write, menu):
        while True:
            func()

            if write:
                # FIXME: Запись изменений в файл с параметрами
                pass

            a = input(menu)

            if int(a) == 1:
                continue
            else:
                break

    def interfase_variable(func, func1, func2, write, menu):
        while True:
            func()

            if write:
                # FIXME: Запись изменений в файл с параметрами
                pass

            a = input(menu)

            if int(a) == 1:
                func1()
            elif int(a) == 2:
                func2()
            else:
                break