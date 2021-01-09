AUTHOR = "Daniel Rustrum"

def run(inp):
    out = []
    for commit in inp:
        if commit["commit"]["committer"]["name"] == AUTHOR:
            out.append(commit["sha"])
    return out