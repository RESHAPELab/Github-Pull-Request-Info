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
        "url": lambda args: f"https://api.github.com/users/{args['username']}",
        "args": ["username"]
    },
    "commits": {
        "url": lambda args: f"https://api.github.com/repos/{args['owner']}/{args['repo']}/commits/{args['sha']}",
        "args": ["owner", "repo", "sha"]
    },
    "branches": {
        "url": lambda args: f"https://api.github.com/repos/{args['owner']}/{args['repo']}/branches",
        "args": ["owner", "repo"]
    },
    "branch-commits": {
        "url": lambda args: f"https://api.github.com/repos/{args['owner']}/{args['repo']}/commits?per_page=100&sha={args['sha']}",
        "args": ["owner", "repo", "sha"]
    },
    "tree": {
        "url": lambda args: f"https://api.github.com/repos/{args['owner']}/{args['repo']}/git/trees/{args['sha']}",
        "args": ["owner", "repo", "sha"]
    },
}