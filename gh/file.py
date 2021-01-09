import json
import pandas

def to_json(path, data):
    with open(path, "w") as json_file:
        json_file.write(json.dumps(data))

def to_csv(path, data):
    df = pandas.DataFrame.from_dict(data)
    csv = df.to_csv(sep="\a")
    with open(path, "w") as csv_file:
        json_file.write(csv)
