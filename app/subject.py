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
        Subject.subject_list(par)
        id = Ui.enter_int(subject_id, 1, len(par[2])) - 1

        for subject in par[2]:
            if subject.id == id:
                return subject

    def create_subject(par):
        name = Ui.enter(subject_name)
        id = len(par[2])

        new = Subject(name, id)
        par[2].append(new)
        return new

    def change_subject(par):
        subject = Subject.choose_subject(par)

        print('Старое имя дисциплины: {}'.format(subject.name))
        subject.name = Ui.enter(subject_name)