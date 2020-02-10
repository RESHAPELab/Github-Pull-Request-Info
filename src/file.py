import pandas as pd
import github

def pulls_to_csv(start_pull, stop_pull, owner, repo, filename="", merged="true", state="closed"):
    (prs, commits, skills) = github.get_pull_requests(owner, repo, start_pull, stop_pull, merged=merged, state=state)

    sep = "\a"

    df = pd.DataFrame(prs, columns=["PR", "Name of Repo", "PR Number", "PR State", "Date Created", "Date Closed", "Title", "Body", "# comments", "# review comments", "# additions", "# deletions", "# commits", "# changed Files"])
    df.to_csv('./data/%s-pulls.csv' % filename, index=False, sep=sep)

    df = pd.DataFrame(commits, columns=["Author login", "Committer login", "PR number", "SHA", "Commit Message", "file name", "Patch text", "# Additions", "# Deletions", "status", "changes"])
    df.to_csv('./data/%s-commits.csv' % filename, index=False, sep=sep)

    # df = pd.DataFrame(commits, columns=["Author login", "Committer login", "PR number", "SHA", "Commit Message", "file name", "Patch text", "# Additions", "# Deletions", "status", "changes"])
    # df.to_csv('./data/%s-skills.csv' % filename, index=False, sep=sep)
