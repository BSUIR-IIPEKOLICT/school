import json
import os.path

from app.pupil import Pupil
from app.mark import Mark
from app.subject import Subject

class File:
    def read(path, file, default):
        parJson = None

        if os.path.isfile(path):
            with open(file, 'r') as f:
                parJson = json.loads(f.read())
        else:
            parJson = json.loads(json.dumps(default, ensure_ascii = False))
            with open(file, 'w+') as f:
                f.write(json.dumps(default, ensure_ascii = False, indent = 4))

        return parJson

    def write(path, file, parJson) -> None:
        if os.path.isfile(path):
            with open(file, 'w+') as f:
                f.seek(0)
                f.close()
        
        with open(file, 'w+') as f:
            f.write(json.dumps(parJson, ensure_ascii = False, indent = 4))

    def build(parPython):
        pupils = []
        for pupil in parPython[0]:
            new = dict()
            new['name'] = pupil.name
            new['surname'] = pupil.surname
            new['address'] = pupil.address
            new['id'] = pupil.id
            pupils.append(new)

        marks = []
        for mark in  parPython[1]:
            new = dict()
            new['value'] = mark.value
            new['subject_id'] = mark.subject_id
            new['pupil_id'] = mark.pupil_id
            new['date'] = mark.date
            new['id'] = mark.id
            marks.append(new)

        subjects = []
        for subject in parPython[2]:
            new = dict()
            new['name'] = subject.name
            new['id'] = subject.id
            subjects.append(new)

        parJson = [pupils, marks, subjects]
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