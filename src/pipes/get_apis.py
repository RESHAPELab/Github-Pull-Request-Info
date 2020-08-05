import re

AUTHOR = "Daniel Rustrum"

woc_def = {
    "java": lambda line: re.search("[import ]([a-z]|[A-Z]|[.])+[;]", line).group(0),
    "py": lambda line: re.search("^(?:from[ ]+(\S+)[ ]+)?import[ ]+(\S+)[ ]*$", line).group(0),
    "js": lambda line: re.search("[import ]([*]|[{]|[}][,]|[a-z]|[A-Z])+[ from ]([\"]|['])([a-z]|[A-Z]|[.])+([\"]|['])[;]*", line).group(0),
    "go": lambda line: re.search("^(?:from[ ]+(\S+)[ ]+)?import[ ]+(\S+)[ ]*$", line).group(0)
}

woc_lang = {
    "java": "Java",
    "py": "Python",
    "js": "Javascript",
    "go": "GO-Lang"
}

def count_defs():
    return 0

def woc_imports(extension, line):
    try:
        return woc_def[extension](line)
    except:
        return None
    

def run(inp):
    # print(inp)

    try:
        if inp["commit"]["author"] != AUTHOR:
            return {}
    except Exception as e:
        pass

        

    out = {
        "apis": [],
        "langs": []
    }

    if inp == {}:
        return out

    apis = []
    langs = []
    for file in inp["files"]:
        try:
            for line in file["patch"].split("\n"):
                if line[1:3] == "@ " and line[-1:-3] == "@@":
                    continue

                import_api = woc_imports(file["filename"].split(".")[-1], line[1:])
                if import_api is None:
                    continue
                lang = woc_lang[file["filename"].split(".")[-1]]

                apis.append(import_api)
                langs.append(lang)
            
            track_lang = {}
            for lang in langs:
                if lang in track_lang:
                    pass
                else:
                    track_lang[lang] = lang
                    out["langs"].append(lang)


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
        except:
            pass

    return out