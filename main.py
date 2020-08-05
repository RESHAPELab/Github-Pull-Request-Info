import src.auth as auth
import src.config as config
import src.gather as gather
import src.file as file
import src.download as download


if __name__ == "__main__":
    configs = config.get_configs("./configs/author.json")
    auth.Auth.setup(configs["general"]["accounts"], configs["general"]["rate-threshold"])
    
    #* NOTE: Gather Repo Branch INFO

    author_result = gather.run(configs["args"], configs["gather"])
    
    configs = config.get_configs("./configs/branches.json")
    branches_result = gather.run(author_result[0]["Repos"], configs["gather"])

    args = []
    for index in range(len(author_result[0]["Repos"])):
        args.append({
            "type": "branch-commits",
            "owner": author_result[0]["Repos"][index]["owner"],
            "repo": author_result[0]["Repos"][index]["repo"],
            "sha": branches_result[index]
        })

    configs = config.get_configs("./configs/branch.json")
    branch = gather.run(args, configs["gather"])

    args = []
    for index in range(len(author_result[0]["Repos"])):
        for index2 in range(len(branch[index])):
            args.append({
                "type": "commits",
                "owner": author_result[0]["Repos"][index]["owner"],
                "repo": author_result[0]["Repos"][index]["repo"],
                "sha": branch[index][index2]
            })

    configs = config.get_configs("./configs/tree.json")
    apis = gather.run(args, configs["gather"])


    results = {
        "Name": author_result[0]["Name"],
        "Repos": []
    }

    repo = author_result[0]["Repos"]
    for index in range(len(repo)):
        results["Repos"].append({
            "Owner": repo[index]["owner"],
            "Name": repo[index]["repo"],
            "API": apis[index]
        })
    

    print(results)
    file.to_json("./data/result.json", results)