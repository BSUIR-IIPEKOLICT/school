# MODULE: Основной каркас программы

from app.average import Average
from app.pupil import Pupil
from app.mark import Mark
from app.subject import Subject
from app.file import File

from app.lib import *
from app.string import *

# BLOCK: Дефолтные параметры

defaultData = [ # python-формат
    [
        Pupil('Иван', 'Иванов', 'г. Минск', 0),
        Pupil('Александр', 'Серов', 'г. Лошица', 1),
        Pupil('Сергей', 'Миронов', 'г. Жодино', 2),
        Pupil('Евгений', 'Кривоносов', 'г. Барановичи', 3)
    ],
    [
        Mark(9, 0, 0, '12.05.2021', 0),
        Mark(2, 0, 1, '19.05.2021', 1),
        Mark(6, 0, 1, '14.05.2021', 2),
        Mark(8, 0, 2, '11.05.2021', 3),
        Mark(4, 1, 0, '18.05.2021', 4),
        Mark(5, 1, 1, '03.05.2021', 5),
        Mark(7, 1, 2, '09.05.2021', 6),
        Mark(8, 1, 3, '02.05.2021', 7),
        Mark(10, 2, 0, '16.05.2021', 8),
        Mark(5, 2, 2, '12.05.2021', 9),
        Mark(8, 2, 2, '18.05.2021', 10)
    ],
    [
        Subject('Математика', 0),
        Subject('Физика', 1),
        Subject('История', 2)
    ]
]

dataPython = File.load(File.read(file_path, file_name, File.build(defaultData)))

# BLOCK: Инструкции для интерфейсов

def createPupil():
    header(header_11)
    Pupil.create_pupil(dataPython)
    File.write(file_path, file_name, File.build(dataPython))

def changePupil():
    header(header_12)
    Pupil.change_pupil(dataPython)
    File.write(file_path, file_name, File.build(dataPython))

def createMark():
    header(header_21)
    Mark.create_mark(dataPython)
    File.write(file_path, file_name, File.build(dataPython))

def markChronology():
    header(header_22)
    Mark.mark_chronology(dataPython)

def markInInterval():
    header(header_23)
    Mark.mark_in_interval(dataPython)

def markedPupils():
    header(header_24)
    Mark.marked_pupils(dataPython)

def createSubject():
    header(header_31)
    Subject.create_subject(dataPython)
    File.write(file_path, file_name, File.build(dataPython))

def changeSubject():
    header(header_32)
    Subject.change_subject(dataPython)
    File.write(file_path, file_name, File.build(dataPython))

def averageMarkSubject():
    header(header_41)
    Average.average_mark_subject(dataPython)

def averageMarkLarger():
    header(header_42)
    Average.average_mark_larger(dataPython)

# BLOCK: Сама прога

header(about)

while True:
    header(main_menu)
    a = input()

    if int(a) == 1:
        while True:
            header(header_1)
            Pupil.pupil_table(dataPython)

            b = input(menu_1)

            if int(b) == 1:
                interfase(createPupil, menu_11)
            elif int(b) == 2:
                interfase(changePupil, menu_12)
            else:
                break
    elif int(a) == 2:
        while True:
            header(header_2)

            b = input(menu_2)

            if int(b) == 1:
                interfase(createMark, menu_21)
            elif int(b) == 2:
                interfase(markChronology, menu_22)
            elif int(b) == 3:
                interfase(markInInterval, menu_23)
            elif int(b) == 4:
                interfase(markedPupils, menu_24)
            else:
                break
    elif int(a) == 3:
        while True:
            header(header_3)
            Subject.subject_list(dataPython)

            b = input(menu_3)

            if int(b) == 1:
                interfase(createSubject, menu_31)
            elif int(b) == 2:
                interfase(changeSubject, menu_32)
            else:
                break
    elif int(a) == 4:
        while True:
            header(header_4)
            Average.average_total(dataPython)

            b = input(menu_4)

            if int(b) == 1:
                interfase(averageMarkSubject, menu_41)
            elif int(b) == 2:
                interfase(averageMarkLarger, menu_42)
            else:
                break
    else:
        break