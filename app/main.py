# MODULE: Основной каркас программы

from app.ui import Ui
from app.mark import Mark
from app.pupil import Pupil
from app.subject import Subject

from app.string import *

while True:
    Ui.header(main_menu)

    a = input()

    if int(a) == 1:
        pass
    elif int(a) == 2:
        pass
    elif int(a) == 3:
        pass
    elif int(a) == 4:
        pass
    else:
        break