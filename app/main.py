# MODULE: Основной каркас программы

from app.average import Average
from app.ui import Ui
from app.pupil import Pupil
from app.mark import Mark
from app.subject import Subject
from app.file import File

from app.string import *

# BLOCK: Дефолтные параметры

defaultPar = [
    [
        Pupil('Игорь', 'Макар', 'Вильнюс', 0),
        Pupil('Александр', 'Лукашенко', 'Минск', 1),
        Pupil('Риаз', 'Гремори', 'Лошица', 2)
    ],
    [
        Mark(9, 0, 2, '21.05.2021', 0),
        Mark(2, 0, 1, '12.05.2021', 1),
        Mark(6, 1, 0, '10.05.2021', 2),
        Mark(8, 3, 0, '14.05.2021', 3),
        Mark(1, 2, 1, '18.05.2021', 4),
    ],
    [
        Subject('Математика', 0),
        Subject('Физика', 1),
        Subject('История', 2)
    ]
]

par = File.load(File.read(file_path, file_name, File.build(defaultPar)))

# BLOCK: Инструкции для интерфейсов

def createPupil():
    Ui.header(header_11)
    Pupil.create_pupil(par)

def changePupil():
    Ui.header(header_12)
    Pupil.change_pupil(par)

def createMark():
    Ui.header(header_21)
    Mark.create_mark(par)

def markChronology():
    Ui.header(header_22)
    Mark.mark_chronology(par)

def markInInterval():
    Ui.header(header_23)
    Mark.mark_in_interval(par)

def markedPupils():
    Ui.header(header_24)
    Mark.marked_pupils(par)

def createSubject():
    Ui.header(header_31)
    Subject.create_subject(par)

def changeSubject():
    Ui.header(header_32)
    Subject.change_subject(par)

def averageMarkSubject():
    Ui.header(header_41)
    Average.average_mark_subject(par)

def averageMarkLarger():
    Ui.header(header_42)
    Average.average_mark_larger(par)

# BLOCK: Сама прога

Ui.header(about)

while True:
    Ui.header(main_menu)
    a = input()

    if int(a) == 1:
        while True:
            Ui.header(header_1)
            Pupil.pupil_table(par)

            b = input(menu_1)

            if int(b) == 1:
                Ui.interfase(createPupil, menu_11)
            elif int(b) == 2:
                Ui.interfase(changePupil, menu_12)
            else:
                break
    elif int(a) == 2:
        while True:
            Ui.header(header_2)

            b = input(menu_2)

            if int(b) == 1:
                Ui.interfase(createMark, menu_21)
            elif int(b) == 2:
                Ui.interfase(markChronology, menu_22)
            elif int(b) == 3:
                Ui.interfase(markInInterval, menu_23)
            elif int(b) == 4:
                Ui.interfase(markedPupils, menu_24)
            else:
                break
    elif int(a) == 3:
        while True:
            Ui.header(header_3)
            Subject.subject_list(par)

            b = input(menu_3)

            if int(b) == 1:
                Ui.interfase(createSubject, menu_31)
            elif int(b) == 2:
                Ui.interfase(changeSubject, menu_32)
            else:
                break
    elif int(a) == 4:
        while True:
            Ui.header(header_4)
            Average.average_total(par)

            b = input(menu_4)

            if int(b) == 1:
                Ui.interfase(averageMarkSubject, menu_41)
            elif int(b) == 2:
                Ui.interfase(averageMarkLarger, menu_42)
            else:
                break
    else:
        break