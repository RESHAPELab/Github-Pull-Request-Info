_endpoints = {
    "pr": {
        "url": lambda args: f"https://api.github.com/repos/{args['owner']}/{args['repo']}/pulls/{args['index']}",
        "args": ["owner", "repo", "index"]
    },
    "issue": {
        "url": lambda args: f"https://api.github.com/repos/{args['owner']}/{args['repo']}/issues/{args['index']}",
        "args": ["owner", "repo", "index"]
    },
    "author": {
        "url": lambda args: f"https://api.github.com/repos/{args['owner']}/{args['repo']}/issues/{args['index']}",
        "args": ["owner", "repo", "index"]
    }
}