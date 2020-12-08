types = {
    "repos": lambda index, args: {
        "index": index,
        "owner": args["owner"],
        "repo": args["repo"]
    },
    "author": lambda index, args: {
        "username": args["username"]
    },
    "commits": lambda index, args: {
        "owner": args["owner"],
        "repo": args["repo"],
        "sha": args["sha"]
    },
    "branches": lambda index, args: {
        "owner": args["owner"],
        "repo": args["repo"]
    },
    "branch-commits": lambda index, args: {
        "owner": args["owner"],
        "repo": args["repo"],
        "sha": args["sha"]
    },
    "tree": lambda index, args: {
        "owner": args["owner"],
        "repo": args["repo"],
        "sha": args["sha"]
    },
    "issue" : lambda index, args: {
        "index": index,
        "owner": args["owner"],
        "repo": args["repo"]
    }
}