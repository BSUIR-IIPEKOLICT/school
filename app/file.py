# MODULE: Методы для работы с файлом

import json
import os.path

from app.pupil import Pupil
from app.mark import Mark
from app.subject import Subject

class File:
    def read(path, name, default):
        dataJson = None

        if os.path.isfile(path):
            with open(name, 'r') as f:
                dataJson = json.loads(f.read())
        else:
            dataJson = json.loads(json.dumps(default, ensure_ascii = False))
            with open(name, 'w+') as f:
                f.write(json.dumps(default, ensure_ascii = False, indent = 4))

        return dataJson

    def write(path, name, dataJson) -> None:
        if os.path.isfile(path):
            with open(name, 'w+') as f:
                f.seek(0)
                f.close()
        
        with open(name, 'w+') as f:
            f.write(json.dumps(dataJson, ensure_ascii = False, indent = 4))

    def build_pupils(dataPython):
        pupilsJson = []
        
        for pupil in dataPython[0]:
            new = dict()
            new['name'] = pupil.name
            new['surname'] = pupil.surname
            new['address'] = pupil.address
            new['id'] = pupil.id
            pupilsJson.append(new)
        
        return pupilsJson

    def build_marks(dataPython):
        marksJson = []

        for mark in  dataPython[1]:
            new = dict()
            new['value'] = mark.value
            new['subject_id'] = mark.subject_id
            new['pupil_id'] = mark.pupil_id
            new['date'] = mark.date
            new['id'] = mark.id
            marksJson.append(new)
        
        return marksJson

    def build_subjects(dataPython):
        subjectsJson = []

        for subject in dataPython[2]:
            new = dict()
            new['name'] = subject.name
            new['id'] = subject.id
            subjectsJson.append(new)

        return subjectsJson

    def build(dataPython):
        dataJson = [File.build_pupils(dataPython), File.build_marks(dataPython), File.build_subjects(dataPython)]
        return dataJson

    def load(dataJson):
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

        return [pupils, marks, subjects] # dataJson