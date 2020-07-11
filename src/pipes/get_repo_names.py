import src.api as api

def run(inp):
    out = {}
    out["Name"] = inp["Name"]
    out["Repos"] = []
    for repo in inp["Repos"]:
        full_name = repo["full_name"].split("/")
        out["Repos"].append({
            "type": "repos",
            "owner": full_name[0],
            "repo": full_name[1],
            "sha": "get@pr/merge_commit_sha",
            "range": {
                "start": 0,
                "stop": 1000
            }
        })
    return out