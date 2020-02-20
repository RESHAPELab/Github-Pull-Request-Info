import requests, time, logging
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
                      limit=100, 
                      merged="true", 
                      state="closed", 
                      get_skills=True
                    ):
    mined = False
    index = min_val
    pull_request_list = []
    commits_list = []
    skills_list = []

    while not mined:
        #* Gather Pull
        username = github_accounts[index%8][0]
        token = github_accounts[index%8][1]
        pr_response = requests.get("https://api.github.com/repos/Jabref/jabref/pulls/%i?state=%s&merged=%s" % (index,state,merged), auth=(username,token))
        pr_result = pr_response.json()
        # print(pr_result)
        
        try:
            commit_response = requests.get("https://api.github.com/repos/JabRef/jabref/commits/%s" % pr_result["head"]["sha"], auth=(username,token))
            commit_result = commit_response.json()
        except:
            pass

        try:
            status_response = requests.get("https://api.github.com/repos/JabRef/jabref/statuses/%s" % pr_result["head"]["sha"], auth=(username,token))
            status_result = status_response.json()[0]
        except:
            status_result = {"state": "N/A"}
        
        
        #* See if valid PR
        try:
            result["message"]
        except:
            try:
                #* Process Data
                (pr_results, commit_results, skill_results) = formatdata.format_data(
                    index, 
                    pr_result, 
                    commit_result, 
                    status_result,
                    github_accounts[index%8][0],
                    github_accounts[index%8][1]
                )
            except Exception as e:
                print("%i - skipped - %s" % (index, e))
                if index >= max_val:
                    mined = True
                index += 1
                continue

            print(index)
            #* Add Data
            pull_request_list.append(pr_results)
            commits_list.append(commit_results)
            skills_list.append(skill_results)

        #* Stop if limit reached
        if int(pr_response.headers["X-RateLimit-Remaining"]) < limit:
            time.sleep(int(pr_response.headers["X-RateLimit-Reset"]))

        #* See if minning is done
        if index >= max_val:
            mined = True
        index += 1

    return (pull_request_list, commits_list, skills_list)