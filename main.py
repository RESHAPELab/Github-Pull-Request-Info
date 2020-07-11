import src.auth as auth
import src.config as config
import src.gather as gather
import src.file as file

if __name__ == "__main__":

    configs = config.get_configs("./configs/author.json")
    auth.Auth.setup(configs["general"]["accounts"], configs["general"]["rate-threshold"])
    
    #* NOTE: Gather author
    author_result = gather.run(configs["args"], configs["gather"])
    print(author_result)

    configs = config.get_configs("./configs/author-repos.json")


    repo_result = gather.run(author_result[0]["Repos"], configs["gather"])

    results = {
        "Name": author_result[0]["Name"],
    }

    repo = author_result[0]["Repos"]
    for index in range(len(author_result[0]["Repos"])):
        results["Repos"] = {
            "Owner": repo[index]["owner"],
            "Name": repo[index]["repo"],
            "API": repo_result[index]
        }
    

    file.to_json("./data/result.json", results)