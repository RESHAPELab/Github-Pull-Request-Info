types = {
    "repos": lambda index, args: {
        "index": index,
        "owner": args["owner"],
        "repo": args["repo"],
        "sha": args["sha"]
    },
    "author": lambda index, args: {
        "username": args["username"]
    }
}