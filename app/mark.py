# MODULE: Класс для оценок

import datetime

from app.subject import Subject
from app.pupil import Pupil
from app.average import Average

from app.lib import *
from app.string import *

# Здесь data = dataPython 

class Mark:
    def __init__(self, value, subject_id, pupil_id, date, id = None) -> None:
        self.value = value
        self.subject_id = subject_id
        self.pupil_id = pupil_id
        self.date = date
        self.id = id

    def create_mark(data):
        value = enter_int(mark_value, 0, 10)
        subject_id = Subject.choose_subject(data).id
        pupil_id = Pupil.choose_pupil(data).id
        date = enter_date()
        id = len(data[1])

        new = Mark(value, subject_id, pupil_id, date, id)
        data[1].append(new)
        return new # запасной вывод

    def mark_chronology(data):
        pupil = Pupil.choose_pupil(data)
        subject = Subject.choose_subject(data)
        data = dict()

        for mark in data[1]:
            for subject_ in data[2]:
                if mark.pupil_id == pupil.id and mark.subject_id == subject_.id:
                    data[mark.date] = mark.id
        
        sorted_data = sorted(data.items(), key = lambda x:datetime.datetime.strptime(x[0], '%d.%m.%Y'), reverse = False)
        print('\nОценки учащегося {0} {1} по предмету {2} в хронологическом порядке\n'
        .format(pupil.name, pupil.surname, subject.name))

        for item in sorted_data:
            for mark in data[1]:
                if mark.id == int(item[1]):
                    print('Дата: {0}, получена оценка {1}.'.format(item[0], mark.value))

    def mark_in_interval(data):
        pupil = Pupil.choose_pupil(data)
        start = enter_date(date_start)
        end = enter_date(date_end)
        d = dict()

        for mark in data[1]:
            if mark.pupil_id == pupil.id:
                if convert_date(start) <= convert_date(mark.date) <= convert_date(end):
                    d[mark.date] = mark.id

        sorted_d = sorted(d.items(), key = lambda x:datetime.datetime.strptime(x[0], '%d.%m.%Y'), reverse = False)
        print('\nОценки учащегося {0} {1} в период с {2} по {3}\n'
            .format(pupil.name, pupil.surname, start, end))

        for item in sorted_d:
            for mark in data[1]:
                if mark.id == int(item[1]):
                    for subject in data[2]:
                        if subject.id == mark.subject_id:
                            print('Дата: {0}, получена оценка {1} по дисциплине {2}.'
                            .format(item[0], mark.value, subject.name))

    def marked_pupils(data):
        subject = Subject.choose_subject(data)
        array = Average.average_mark_interval(data, subject)

        print('\nСписок аттестованных учащихся по предмету {}:\n'.format(subject.name))
        for item in array[0]:
            print('Учащийся {0} {1}, средний балл по предмету: {2}.'.format(item[0], item[1], item[2]))
        
        print('\nСписок лоботрясов по предмету {}:\n'.format(subject.name))
        for item in array[1]:
            print('Учащийся {0} {1}.'.format(item[0], item[1]))