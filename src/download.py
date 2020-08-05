import os
def get_repo(owner, repo, location):
    os.system(f"git clone https://github.com/{owner}/{repo} {location}/{repo}")