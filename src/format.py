

def flatten2d(dictionary:dict):
    return [dictionary]

def aliases(ref:dict, data:dict):
    result = {}
    for (key, value) in ref.items():
        try:
            if value["alias"] != "":
                result[value["alias"]] = data[key]
        except:
            pass
    return result