def run(pr):
    try:
        issues = []
        for item in re.findall("#([0-9])+\w+", pr["body"]):
            issues.append(item.replace("#", ""))

        for item in re.findall("#([0-9])+\w+", pr["title"]):
            issues.append(item.replace("#", ""))
        return issues
    except:
        return ["N/A"]