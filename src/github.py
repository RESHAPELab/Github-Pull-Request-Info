import requests, time, logging, re
import database, formatdata

logging.basicConfig(filename='.log', filemode='w', format='%(levelname)s: %(message)s')
github_accounts = {
        0: ['Githubfake01', '5RNsya*z#&aA'],
        1: ['GithubFake02', '9dJeg^Bp^g63'],
	    2: ['Github-Fake03', '2A$p3$zy%aaD'],
	    3: ['GithubFake04', '4Yg3&MQN9x%F'],
        4: ['GithubFake05', 'Cm82$$bFa!xb'],
        5: ['GithubFake06', '2t*u2Y8P^tTk'],
        6: ['GithubFake07', 'Hk1233**012'],
        7: ['GithubFake08', 'PO11sd*^%$']
    }



def get_pull_requests(owner="Jabref", 
                      repo="jabref", 
                      min_val=0, 
                      max_val=100, 
                      limit=200, 
                      merged="true", 
                      state="closed", 
                      get_skills=True
                    ):
    mined = False
    index = min_val
    pull_request_list = []
    commits_list = []
    issue_list = []

    while not mined:
        print(index)
        #* Gather Pull
        username = github_accounts[index%len(github_accounts)][0]
        token = github_accounts[index%len(github_accounts)][1]
        pr_response = requests.get("https://api.github.com/repos/google/ExoPlayer/pulls/%i?state=%s&merged=%s" % (index,state,merged), auth=(username,token))
        pr_response_comments = requests.get("https://api.github.com/repos/google/ExoPlayer/pulls/%i/comments?state=%s&merged=%s" % (index,state,merged), auth=(username,token))
        pr_result = pr_response.json()
        pr_result_comments = pr_response_comments.json()
        
        try:
            commit_response = requests.get("https://api.github.com/repos/google/ExoPlayer/commits/%s" % pr_result["head"]["sha"], auth=(username,token))
            commit_result = commit_response.json()
        except:
            pass

        try:
            status_response = requests.get("https://api.github.com/repos/google/ExoPlayer/statuses/%s" % pr_result["head"]["sha"], auth=(username,token))
            status_result = status_response.json()[0]
        except:
            status_result = {"state": "N/A"}
        


        try:
            issue_response = requests.get("https://api.github.com/repos/google/ExoPlayer/issues/%s" % index, auth=(username,token))
            issue_comments_response = requests.get("https://api.github.com/repos/google/ExoPlayer/issues/%s/comments" % index, auth=(username,token))
            issue_result = issue_response.json()
            issue_result_comments = issue_comments_response.json()
            issue_result["number"] = index
        except:
            issue_result = {"number": index}
        
        #* See if valid PR
        try:
            pr_result["message"]
        except:
            #* Process Data
            (pr_results, commit_results) = formatdata.format_data_pr(
                index, 
                pr_result, 
                commit_result, 
                status_result,
                username,
                token,
                pr_result_comments
            )

            commits_list.append(commit_results)
            for item in pr_results:
                pull_request_list.append(item)

        try:
            issue_result["message"]
        except:
            issue_list.append(formatdata.format_data_issues(issue_result, issue_result_comments))
        

        #* Stop if limit reached
        if int(issue_response.headers["X-RateLimit-Remaining"]) < limit:
            sleep = int(issue_response.headers["X-RateLimit-Reset"])
            print("sleeping for: %s seconds" % sleep)
            for sl in range(sleep):
                time.sleep(1)

        #* See if minning is done
        if index >= max_val:
            mined = True
        index += 1

    return (pull_request_list, commits_list, issue_list)