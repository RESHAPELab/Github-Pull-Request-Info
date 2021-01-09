def run(inp):
    # print(f"Branch Sha:{inp}")
    master_branch_sha = ""
    for branch in inp:
        if branch["name"] == "master":
            master_branch_sha = branch["commit"]["sha"]
            break
    return master_branch_sha