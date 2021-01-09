import re

IMPLICT_CHECK = True 

def implcit_check_java(line):
    # import ...;
    if line[0:6] == "import" and line[-1] == ";":
        return line[6:-1]
    else:
        return None

implict_woc = {
    "java": implcit_check_java,
    }

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

def woc_imports(extension, line):
    try:
        if IMPLICT_CHECK:
            return implict_woc[extension](line)
        else:
            return woc_def[extension](line)
    except:
        return None
    
# TODO: Add name of file to data
# TODO: Put log data in results
def run(inp):
    out = {
        "apis": [],
        "langs": []
    }

    if inp == {}:
        return {"message": "No APIs"}

    apis = []
    langs = []
    track_api = {}
    track_lang = {}


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
            
            for lang in langs:
                if lang in track_lang:
                    pass
                else:
                    track_lang[lang] = lang
                    out["langs"].append(lang)


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