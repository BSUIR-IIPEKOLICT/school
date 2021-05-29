import json
import os.path

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
