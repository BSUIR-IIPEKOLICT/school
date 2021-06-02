# MODULE: Класс для учеников

from app.lib import *
from app.string import *

class Pupil:
    def __init__(self, name, surname, address, id = None) -> None:
        self.name = name
        self.surname = surname
        self.address = address
        self.id = id

    def pupil_table(par) -> None:
        for index, pupil in enumerate(par[0]):
            print('#{0} - учащийся {1} {2}, адрес: {3}.'
            .format(index + 1, pupil.name, pupil.surname, pupil.address))

    def create_pupil(par):
        name = enter(pupil_name)
        surname = enter(pupil_surname)
        address = enter(pupil_address)
        id = len(par[0])

        new = Pupil(name, surname, address, id)
        par[0].append(new)
        return new

    def choose_pupil(par):
        Pupil.pupil_table(par)
        id = enter_int(pupil_id, 1, len(par[0])) - 1

        for pupil in par[0]:
            if pupil.id == id:
                return pupil

    def change_pupil(par):
        pupil = Pupil.choose_pupil(par)

        a = input(pupil_change_name)
        if int(a) == 1:
            print('Старое имя: {}'.format(pupil.name))
            pupil.name = enter(pupil_name)

        a = input(pupil_change_surname)
        if int(a) == 1:
            print('Старая фамилия: {}'.format(pupil.surname))
            pupil.surname = enter(pupil_surname)

        a = input(pupil_change_address)
        if int(a) == 1:
            print('Старый адрес: {}'.format(pupil.address))
            pupil.address = enter(pupil_address)