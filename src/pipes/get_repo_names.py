
def run(inp):
    # print("Repo Name: %s" % inp)
    out = {}
    out["Name"] = inp["Name"]
    out["Repos"] = []
    for repo in inp["Repos"]:
        full_name = repo["full_name"].split("/")
        out["Repos"].append({
            "type": "repos",
            "owner": full_name[0],
            "repo": full_name[1]
        })
    
    return out