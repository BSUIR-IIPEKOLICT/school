# MODULE: Методы для работы с файлом

import json
import os.path

from app.pupil import Pupil
from app.mark import Mark
from app.subject import Subject

class File:
    def read(path, name, default):
        parJson = None

        if os.path.isfile(path):
            with open(name, 'r') as f:
                parJson = json.loads(f.read())
        else:
            parJson = json.loads(json.dumps(default, ensure_ascii = False))
            with open(name, 'w+') as f:
                f.write(json.dumps(default, ensure_ascii = False, indent = 4))

        return parJson

    def write(path, name, parJson) -> None:
        if os.path.isfile(path):
            with open(name, 'w+') as f:
                f.seek(0)
                f.close()
        
        with open(name, 'w+') as f:
            f.write(json.dumps(parJson, ensure_ascii = False, indent = 4))

    def build_pupils(parPython):
        pupilsJson = []
        
        for pupil in parPython[0]:
            new = dict()
            new['name'] = pupil.name
            new['surname'] = pupil.surname
            new['address'] = pupil.address
            new['id'] = pupil.id
            pupilsJson.append(new)
        
        return pupilsJson

    def build_marks(parPython):
        marksJson = []

        for mark in  parPython[1]:
            new = dict()
            new['value'] = mark.value
            new['subject_id'] = mark.subject_id
            new['pupil_id'] = mark.pupil_id
            new['date'] = mark.date
            new['id'] = mark.id
            marksJson.append(new)
        
        return marksJson

    def build_subjects(parPython):
        subjectsJson = []

        for subject in parPython[2]:
            new = dict()
            new['name'] = subject.name
            new['id'] = subject.id
            subjectsJson.append(new)

        return subjectsJson

    def build(parPython):
        parJson = [File.build_pupils(parPython), File.build_marks(parPython), File.build_subjects(parPython)]
        return parJson

    def load(parJson):
        pupils = []
        for pupil in parJson[0]:
            new = Pupil(pupil['name'], pupil['surname'], pupil['address'], int(pupil['id']))
            pupils.append(new)

        marks = []
        for mark in parJson[1]:
            new = Mark(int(mark['value']), int(mark['subject_id']), int(mark['pupil_id']), mark['date'], int(mark['id']))
            marks.append(new)

        subjects = []
        for subject in parJson[2]:
            new = Subject(subject['name'], int(subject['id']))
            subjects.append(new)

        parPython = [pupils, marks, subjects]
        return parPython