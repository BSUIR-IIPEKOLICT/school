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