import datetime

from app.ui import Ui
from app.subject import Subject
from app.pupil import Pupil
from app.average import Average

from app.string import *

class Mark:
    def __init__(self, value, subject_id, pupil_id, date, id = None) -> None:
        self.value = value
        self.subject_id = subject_id
        self.pupil_id = pupil_id
        self.date = date
        self.id = id

    def create_mark(par):
        value = Ui.enter_int(mark_value, 0, 10)
        subject_id = Subject.choose_subject(par).id
        pupil_id = Pupil.choose_pupil(par).id
        date = Ui.enter_date()
        id = len(par[1])

        new = Mark(value, subject_id, pupil_id, date, id)
        par[1].append(new)
        return new

    def mark_chronology(par):
        pupil = Pupil.choose_pupil(par)
        subject = Subject.choose_subject(par)
        data = dict()

        for mark in par[1]:
            for subject_ in par[2]:
                if mark.pupil_id == pupil.id and mark.subject_id == subject_.id:
                    data[mark.date] = mark.id
        
        sorted_data = sorted(data.items(), key = lambda x:datetime.datetime.strptime(x[0], '%d.%m.%Y'), reverse = False)
        print('\nОценки учащегося {0} {1} по предмету {2} в хронологическом порядке\n'
        .format(pupil.name, pupil.surname, subject.name))

        for item in sorted_data:
            for mark in par[1]:
                if mark.id == int(item[1]):
                    print('Дата: {0}, получена оценка {1}.'.format(item[0], mark.value))

    def mark_in_interval(par):
        pupil = Pupil.choose_pupil(par)
        start = Ui.enter_date(date_start)
        end = Ui.enter_date(date_end)
        data = dict()

        for mark in par[1]:
            if mark.pupil_id == pupil.id:
                if Ui.convert_date(start) <= Ui.convert_date(mark.date) <= Ui.convert_date(end):
                    data[mark.date] = mark.id

        sorted_data = sorted(data.items(), key = lambda x:datetime.datetime.strptime(x[0], '%d.%m.%Y'), reverse = False)
        print('\nОценки учащегося {0} {1} в период с {2} по {3}\n'
            .format(pupil.name, pupil.surname, start, end))

        for item in sorted_data:
            for mark in par[1]:
                if mark.id == int(item[1]):
                    for subject in par[2]:
                        if subject.id == mark.subject_id:
                            print('Дата: {0}, получена оценка {1} по дисциплине {2}.'
                            .format(item[0], mark.value, subject.name))

    def marked_pupils(par):
        subject = Subject.choose_subject(par)
        array = Average.average_mark_interval(par, subject)

        print('\nСписок аттестованных учащихся по предмету {}:\n'.format(subject.name))
        for item in array[0]:
            print('Учащийся {0} {1}, средний балл по предмету: {2}.'.format(item[0], item[1], item[2]))
        
        print('\nСписок лоботрясов по предмету {}:\n'.format(subject.name))
        for item in array[1]:
            print('Учащийся {0} {1}.'.format(item[0], item[1]))