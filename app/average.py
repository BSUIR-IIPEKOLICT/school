# MODULE: Класс для подсчета среднего балла

from app.subject import Subject

from app.lib import *
from app.string import *

# Здесь data = dataPython 

class Average:
    def average_mark(data, pupil, subject):
        sum = i = rez = 0

        for mark in data[1]:
            if mark.subject_id == subject.id and mark.pupil_id == pupil.id:
                sum += mark.value
                i += 1

        if sum > 0 and i > 0:
            rez = sum / i
        return rez

    def average_mark_interval(data, subject):
        start = enter_date(date_start)
        end = enter_date(date_end)
        list_marked = []
        list_nomarked = []

        for pupil in data[0]:
            sum = 0
            i = 0

            for mark in data[1]:
                if convert_date(start) <= convert_date(mark.date) <= convert_date(end):
                    if mark.subject_id == subject.id and mark.pupil_id == pupil.id:
                        sum += mark.value
                        i += 1

            if sum > 0 and i > 0:
                rez = sum / i
                list_marked.append([pupil.name, pupil.surname, rez])
            else:
                list_nomarked.append([pupil.name, pupil.surname])
        
        return [list_marked, list_nomarked]

    def average_mark_subject(data):
        subject = Subject.choose_subject(data)
        print('Средний балл учащихся по предмету {}\n'.format(subject.name))

        for pupil in data[0]:
            print('{0} {1}: средний балл равен {2}.'
            .format(pupil.name, pupil.surname, Average.average_mark(data, pupil, subject)))

    def average_mark_larger(data):
        subject = Subject.choose_subject(data)
        value = enter_int(mark_user, 0, 9)
        print('Список учащихся, у которых средний балл по предмету {0} выше {1}\n'.format(subject.name, value))
        i = 0

        for pupil in data[0]:
            average = Average.average_mark(data, pupil, subject)

            if average > float(value):
                i += 1
                print('#{0} - {1} {2} (средний балл {3}).'.format(i, pupil.name, pupil.surname, average))

    def average_total(data):
        for pupil in data[0]:
            sum = 0.0
            i = 0
            rez = 0

            for subject in data[2]:
                i += 1
                sum += Average.average_mark(data, pupil, subject)

            if sum > 0 and i > 0:
                rez = sum / i

            print('Учащийся {0} {1}: суммарный средний балл по всем предметам {2}.'
            .format(pupil.name, pupil.surname, rez))