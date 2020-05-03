import file, requests

if __name__ == "__main__":
    start_pull= 0

    owner = "Jabref"
    repo = "jabref"

    stop_pull_json = requests.get("https://api.github.com/repos/%s/%s/pulls" % (owner, repo)).json()
    stop_issue_request = requests.get("https://api.github.com/search/issues?q=repo:%s/%s+type:issue" % (owner, repo)).json()
    stop_pull = int(stop_pull_json[0]["number"])
    stop_issue = int(stop_issue_request["total_count"])

    if stop_pull > stop_issue:
        stop = stop_pull
    else:
        stop = stop_issue
    
    stop = 30
    print("scanning %i pulls\n\n\n" % stop)

    # Clean Data

    file.pulls_to_csv(start_pull, stop, owner, repo, merged="true", state="closed", filename="merged-closed")
    # file.pulls_to_csv(start_pull, stop_pull, owner, repo, merged="true", state="open", filename="merged-open")
    # file.pulls_to_csv(start_pull, stop_pull, owner, repo, merged="false", state="closed", filename="unmerged-closed")
    # file.pulls_to_csv(start_pull, stop_pull, owner, repo, merged="false", state="open", filename="unmerged-open")
   