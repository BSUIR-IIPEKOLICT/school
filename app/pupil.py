# MODULE: Класс для учеников

from app.lib import *
from app.string import *

# Здесь data = dataPython 

class Pupil:
    def __init__(self, name, surname, address, id = None) -> None:
        self.name = name
        self.surname = surname
        self.address = address
        self.id = id

    def pupil_table(data):
        print(pupil_header)
        
        for index, pupil in enumerate(data[0]):
            print('#{0} - учащийся {1} {2}, адрес: {3}.'
            .format(index + 1, pupil.name, pupil.surname, pupil.address))

    def create_pupil(data):
        name = enter(pupil_name)
        surname = enter(pupil_surname)
        address = enter(pupil_address)
        id = len(data[0])

        new = Pupil(name, surname, address, id)
        data[0].append(new)
        return new # запасной вывод

    def choose_pupil(data):
        Pupil.pupil_table(data)
        id = enter_int(pupil_id, 1, len(data[0])) - 1

        for pupil in data[0]:
            if pupil.id == id:
                return pupil

    def change_pupil(data):
        pupil = Pupil.choose_pupil(data)

        a = input(pupil_change_name)
        if int(a) == 1:
            print('\nСтарое имя: {}'.format(pupil.name))
            pupil.name = enter(pupil_name)

        a = input(pupil_change_surname)
        if int(a) == 1:
            print('\nСтарая фамилия: {}'.format(pupil.surname))
            pupil.surname = enter(pupil_surname)

        a = input(pupil_change_address)
        if int(a) == 1:
            print('\nСтарый адрес: {}'.format(pupil.address))
            pupil.address = enter(pupil_address)