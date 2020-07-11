def get_configs(path:str):
    import json
    with open(path, "r") as json_file:
        return json.loads(json_file.read())
    