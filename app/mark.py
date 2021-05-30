from app.ui import Ui
from app.subject import Subject
from app.pupil import Pupil
import datetime

from app.string import *

class Mark:
    def __init__(self, value, subject_id, pupil_id, date, id = None) -> None:
        self.value = value
        self.subject_id = subject_id
        self.pupil_id = pupil_id
        self.date = date
        self.id = id

    def create_mark(par):
        value = Ui.enter_int(mark_value, -1, 11)

        Subject.subject_list(par)
        subject_id = Ui.enter_int(mark_subject, 0, len(par[2]) + 1) - 1

        Pupil.pupil_table(par)
        pupil_id = Ui.enter_int(mark_pupil, 0, len(par[0]) + 1) - 1

        date = Ui.enter_date()
        id = len(par[1])

        new = Mark(value, subject_id, pupil_id, date, id)
        par[1].append(new)
        return new

    def mark_chronology(type, par):
        pupil = Pupil.choose_pupil(par)

        if type == 1:
            Subject.subject_list(par)
            subject = Subject.choose_subject(par)
        else:
            print(date_start)
            start = Ui.enter_date()
            print(date_end)
            end = Ui.enter_date()

        data = dict()

        if type == 1:
            for mark in par[1]:
                for subject in par[2]:
                    if mark.pupil_id == pupil.id and mark.subject_id == subject.id:
                        data[mark.date] = mark.id
        else:
            for mark in par[1]:
                if mark.pupil_id == pupil.id:
                    if Ui.convert_date(start) <= Ui.convert_date(mark.date) <= Ui.convert_date(end):
                        data[mark.date] = mark.id
        
        sorted_data = sorted(data.items(), key = lambda x:datetime.datetime.strptime(x[0], '%d.%m.%Y'), reverse=True)
        
        if type == 1:
            print('\nОценки учащегося {0} {1} по предмету {2} в хронологическом порядке\n'
            .format(pupil.name, pupil.surname, subject.name))

            for item in sorted_data:
                for mark in par[1]:
                    if mark.id == int(item[1]):
                        print('Дата: {0}, получена оценка {1}.'.format(item[0], mark.value))
        else:
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
        Subject.subject_list(par)
        subject = Subject.choose_subject(par)

        print(date_start)
        start = Ui.enter_date()
        print(date_end)
        end = Ui.enter_date()

        list_marked = []
        list_nomarked = []

        for pupil in par[0]:
            sum = 0
            i = 0

            for mark in par[1]:
                if Ui.convert_date(start) <= Ui.convert_date(mark.date) <= Ui.convert_date(end):
                    if mark.subject_id == subject.id and mark.pupil_id == pupil.id:
                        sum += mark.value
                        i += 1

            if sum > 0 and i > 0:
                rez = sum / i
                list_marked.append([pupil.name, pupil.surname, rez])
            else:
                list_nomarked.append([pupil.name, pupil.surname])

        print('\nСписок аттестованных учащихся по предмету {}:\n'.format(subject.name))
        for item in list_marked:
            print('Учащийся {0} {1}, средний балл по предмету: {2}.'.format(item[0], item[1], item[2]))
        
        print('\nСписок лоботрясов по предмету {}:\n'.format(subject.name))
        for item in list_nomarked:
            print('Учащийся {0} {1}.'.format(item[0], item[1]))