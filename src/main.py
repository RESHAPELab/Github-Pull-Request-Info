import file, requests

if __name__ == "__main__":
    start_pull= 0
    owner = "Jabref"
    repo = "jabref"
    stop_pull_json = requests.get("https://api.github.com/repos/%s/%s/pulls" % (owner, repo)).json()
    stop_pull = int(stop_pull_json[0]["number"])
    stop_pull = 5
    print("scanning %i pulls\n\n\n" % stop_pull)

    # Clean Data

    file.pulls_to_csv(start_pull, stop_pull, owner, repo, merged="true", state="closed", filename="merged-closed")
    # file.pulls_to_csv(start_pull, stop_pull, owner, repo, merged="true", state="open", filename="merged-open")
    # file.pulls_to_csv(start_pull, stop_pull, owner, repo, merged="false", state="closed", filename="unmerged-closed")
    # file.pulls_to_csv(start_pull, stop_pull, owner, repo, merged="false", state="open", filename="unmerged-open")
   