# MODULE: Методы для работы с файлом

import json
import os.path

from app.pupil import Pupil
from app.mark import Mark
from app.subject import Subject

class File:
    def read(path, name, default): # фуункция для чтения данных из файла
        dataJson = None

        if os.path.isfile(path): # если файл существует
            with open(name, 'r') as f: # открыть
                dataJson = json.loads(f.read()) # и прочитать (попутно сконвертировав в json-строку)
        else: # если нет файла
            dataJson = json.loads(json.dumps(default, ensure_ascii = False)) # загрузить и сконвертить дефолт даные
            with open(name, 'w+') as f: # создать и записать дефолтные данные в файл
                f.write(json.dumps(default, ensure_ascii = False, indent = 4))

        return dataJson # данные в json-формате

    def write(path, name, dataJson): # функция для записи данных в файл
        if os.path.isfile(path): # если файл существует
            with open(name, 'w+') as f: # открыть и очистить
                f.seek(0)
                f.close()
        
        with open(name, 'w+') as f: # снова открыть
            f.write(json.dumps(dataJson, ensure_ascii = False, indent = 4)) # записать данные

    def build_pupils(dataPython): # преобразование инфы об учениках из питоновского в json-формат
        pupilsJson = []
        
        for pupil in dataPython[0]: # перебор учеников
            new = dict() # каждый ученик - словарь
            new['name'] = pupil.name
            new['surname'] = pupil.surname
            new['address'] = pupil.address
            new['id'] = pupil.id
            pupilsJson.append(new) # добавить словарь в итоговый лист
        
        return pupilsJson # лист учеников в json

    def build_marks(dataPython): # преобразование инфы об оценках из питоновского в json-формат
        marksJson = []

        for mark in  dataPython[1]: # перебор оценок
            new = dict() # каждая оценка - словарь
            new['value'] = mark.value
            new['subject_id'] = mark.subject_id
            new['pupil_id'] = mark.pupil_id
            new['date'] = mark.date
            new['id'] = mark.id
            marksJson.append(new) # добавить словарь в итоговый лист
        
        return marksJson # лист оценок в json

    def build_subjects(dataPython): # преобразование инфы о предметах из питоновского в json-формат
        subjectsJson = []

        for subject in dataPython[2]: # перебор предметов
            new = dict() # каждый предмет - словарь
            new['name'] = subject.name
            new['id'] = subject.id
            subjectsJson.append(new) # добавить словарь в итоговый лист

        return subjectsJson # лист предметов в json

    def build(dataPython): # сборка полного файла json
        return [File.build_pupils(dataPython), File.build_marks(dataPython), File.build_subjects(dataPython)]

    def load(dataJson): # Преобразование json-строки данных в питон-формат
        pupils = []
        for pupil in dataJson[0]:
            new = Pupil(pupil['name'], pupil['surname'], pupil['address'], int(pupil['id']))
            pupils.append(new)

        marks = []
        for mark in dataJson[1]:
            new = Mark(int(mark['value']), int(mark['subject_id']), int(mark['pupil_id']), mark['date'], int(mark['id']))
            marks.append(new)

        subjects = []
        for subject in dataJson[2]:
            new = Subject(subject['name'], int(subject['id']))
            subjects.append(new)

        return [pupils, marks, subjects] # dataPython