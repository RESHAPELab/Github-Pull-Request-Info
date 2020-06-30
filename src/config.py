def get_configs():
    import json
    with open("./config.json", "r") as json_file:
        return json.loads(json_file.read())
    