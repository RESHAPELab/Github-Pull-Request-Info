import pandas as pd
import github

def pulls_to_csv(start_pull, stop_pull, owner, repo, filename="", merged="true", state="closed"):
    (prs, commits, issues) = github.get_pull_requests(owner, repo, start_pull, stop_pull, merged=merged, state=state)

    sep = "\a"

    # df = pd.DataFrame(prs, columns=["PR Number", "Closed Date", "Author", "Title", "Body", "Comments", "Issue Number"])
    # df.to_csv('./data/%s-pulls.csv' % filename, index=False, sep=sep)

    # df = pd.DataFrame(commits, columns=["PR Number", "Message", "Author", "Date", "Patch"])
    # df.to_csv('./data/%s-commits.csv' % filename, index=False, sep=sep)

    df = pd.DataFrame(issues, columns=["Issue Number", "Date Issue Closed", "Author", "Title", "Body", "Comments"])
    df.to_csv('./data/%s-issues.csv' % filename, index=False, sep=sep)
