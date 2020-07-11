import re

woc_def = {
    ".java": lambda line: re.search("[import ]([a-z]|[A-Z])+[;]"),
    ".py": lambda line: re.search("[import ]([a-z]|[A-Z])")
}

woc_lang = {
    ".java": "Java",
    ".py": "Python"
}

def count_defs():
    return 0

def woc_imports(extension, line):
    try:
        return woc_def[extension](line)
    except:
        return
    

def run(inp):
    print(inp)

    out = {
        "apis": [],
        "langs": []
    }

    if inp == {}:
        return out

    apis = []
    for file in inp["files"]:
        for line in file["patch"].split("\n"):
            apis.append(woc_imports(file["filename"].split(".")[-1], line))
            out["langs"].append(woc_lang[file["filename"].split(".")[-1]])
        
        track_api = {}
        for api in apis:
            if api in track_api:
                track_api[api] += 1
            else:
                track_api[api] = 1

        for (api, count) in track_api.items():
            out["apis"].append({
                "name": api,
                "count": count
            })

    return out