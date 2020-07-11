import json

def to_json(path, data):
    with open(path, "w") as json_file:
        json_file.write(json.dumps(data))