import gh.entry as gh

#* All Parameters need to have a default value
def next_index(reset:bool = false) -> int:
    index = 0
    while True:
        if reset == true:
            index = 0
        else:
            index += 1


if __name__ == "__main__":

    gh.Config(users=[

    ])

    print("\n\nPulls and Commmits:")


    #* Use https://docs.github.com/en/free-pro-team@latest/graphql/overview/explorer to get your query
    #* Each curly brace within the query needs to be a double curly brace here 
    pr_fetch = gh.Fetch("repo-commit", "V4", , [
       lambda data: f"""
        {{
            organization(login: "{data.static.org}") {{
                repository(name: "{data.static.repo}") {{
                    pullRequest(number: {data.dynamic.index}) {{
                        number
                        additions
                    }}
                }}
            }}
        }}
       """
    ]).ref()

    log_pipe = gh.Pipe([
        "log"
    ])

    (pull_request_miner = gh.Mine()
        .statics({
            org: "Jabref",
            repo: "jabref"
        })
        .dynamics({
            index: next_index
        })
        .limit(start = 0, stop = 4100)
        .fetch(pr_fetch)
        .pipe(log_pipe)
        .to_json("./data/repos-result")
        .to_csv("./data/repos-result"))
        .return_result()

    next_index(reset = true)