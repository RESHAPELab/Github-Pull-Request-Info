import src.auth as auth
import src.config as config
import src.gather as gather
import src.file as file
import src.download as download


if __name__ == "__main__":
    print("\n\nPulls and Commmits:")
    configs = config.get_configs("./configs/repos.json")
    auth.Auth.setup(configs["general"]["accounts"], configs["general"]["rate-threshold"])
    repos_result = gather.run(configs["args"], configs["gather"])
    file.to_json("./data/repos-result.json", repos_result)

    print("\n\nIssues:")
    configs = config.get_configs("./configs/issues.json")
    repos_result = gather.run(configs["args"], configs["gather"])
    file.to_json("./data/issues-result.json", repos_result)