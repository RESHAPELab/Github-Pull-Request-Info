types = {
    "repos": lambda index, args: {
        "index": index,
        "owner": args["owner"],
        "repo": args["repo"]
    },
    "authors": lambda index, args: {
        "name": args["name"]
    }
}