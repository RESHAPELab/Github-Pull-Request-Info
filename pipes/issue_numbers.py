import re

def run(inp):
    issues = {}
    try:
        for item in re.finditer("#([0-9])+\w+", inp["body"]):
            issues[item.group(0)[1:]] = True
    except:
        pass

    try:
        for item in re.finditer("#([0-9])+\w+", inp["title"]):
            issues[item.group(0)[1:]] = True
    except:
        pass

    inp["issues"] = list(issues.keys())
    return inp