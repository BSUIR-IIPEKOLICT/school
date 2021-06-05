# MODULE: Класс для дисциплин

from app.lib import *
from app.string import *

# Здесь data = dataPython 

class Subject:
    def __init__(self, name, id = None) -> None:
        self.name = name
        self.id = id

    def subject_list(data):
        print(subject_header)
        
        for index, subject in enumerate(data[2]):
            print('#{0} - {1}.'.format(index + 1, subject.name))

    def choose_subject(data):
        Subject.subject_list(data)
        id = enter_int(subject_id, 1, len(data[2])) - 1

        for subject in data[2]:
            if subject.id == id:
                return subject

    def create_subject(data):
        name = enter(subject_name)
        id = len(data[2])

        new = Subject(name, id)
        data[2].append(new)
        return new

    def change_subject(data):
        subject = Subject.choose_subject(data)

        print('Старое имя дисциплины: {}'.format(subject.name))
        subject.name = enter(subject_name)