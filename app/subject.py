from app.ui import Ui

from app.string import *

class Subject:
    def __init__(self, name, id = None) -> None:
        self.name = name
        self.id = id

    def subject_list(par) -> None:
        for index, subject in enumerate(par[2]):
            print('#{0} - {1}.'.format(index + 1, subject.name))

    def choose_subject(par):
        id = Ui.enter_int(subject_id, 0, len(par[2]) + 1) - 1

        for subject in par[2]:
            if subject.id == id:
                return subject