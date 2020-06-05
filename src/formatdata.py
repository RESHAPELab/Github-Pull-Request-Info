import database, logging, requests, base64, time, os

database = None
# database = database.query_db()
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

paths_memo = {}

def file_exists(file, username, token):
    path = ""

    for line in database[3]:
        if file == line[0]:
            path = "/".join(line[1].split("/")[6:]) + "/" + file

    if path not in paths_memo:
        passed = False
        url = "../repos/ExoPlayer"
        
        # Print Path
        if os.path.exists(url + path):
            passed = True

        paths_memo[path] = passed

    return paths_memo[path]

def get_api_name(line):
    found_api = False
    if line[0] == "+":
        api_status = "added"
    elif line[0] == "-":
        api_status = "removed"
    else:
        api_status = "other"
    if line[1:7] == "import":
        api_name = line[8:-1].lstrip().split(".")[-1]
        if api_name == "*":
            api_name = line[8:-1].lstrip().split(".")[-2]

        #* Log Unadded APIs
        for db_line in database[0]:
            if api_name == db_line[0]:
                found_api = True
        
        if not found_api:
            logging.warning("import \"%s\" is not recorded in api table" % api_name)
    else:
        api_name = None


    return (api_name, api_status)

def get_skills(api_name):
    found_skill = False

    skills = []
    for line3 in database[2]:
        if api_name == (line3[2]).split(".")[-1]:
            skills.append(line3[0])
        else:
            pass

    #* Log Not found API in files
    if not found_skill:
        logging.warning("import \"%s\" is not recorded in api_specific table" % api_name)

    return skills

def get_related_files(api_name, user, password):
    found_file = False
    files = []

    for line2 in database[1]:
        if api_name == (line2[1]).split(".")[-1] and file_exists(line2[0], user, password):
            files.append(line2[0])
            found_file = True

    #* Log Not found API in files
    if not found_file:
        logging.warning("import \"%s\" is not recorded in files table" % api_name)

    return files

def get_known_import(file_name, line, user, password):
    (api_name, api_status) = get_api_name(line)
    related_files = []
    skills = []
    grid = []

    if api_name is not None:
        #* Check Api DB
        skills = get_skills(api_name)
        related_files = get_related_files(api_name, user, password)
        # grid = [api_name, api_status, skills[0]]
        try:
            if related_files == [] and skills == []:
                grid.append([file_name, api_name, api_status, "N/A", "N/A"])
            elif related_files == []:
                grid.append([file_name, api_name, api_status, skills[0], "N/A"])
            elif skills == []:
                for index in related_files:
                    grid.append([file_name, api_name, api_status, "N/A", index])
            else:
                for index in related_files:
                    grid.append([file_name, api_name, api_status, skills[0], index])
        except Exception as e:
            print(e)
    return grid

def parse_skills(text:str, file, user, password):
    lines = text.split("\n")
    results = []
    #* Get Import
    for line in lines:
        result = get_known_import(file["filename"], line, user, password)
        if result != []:
            results.append(result)
    return results

def result_value(result, value, default):
    try:
        if len(value) == 1:
            return result[value[0]]
        elif len(value) == 2:
            return result[value[0]][value[1]]
        elif len(value) == 3:
            return result[value[0]][value[1]][value[2]]
        elif len(value) == 4:
            return result[value[0]][value[1]][value[2]][value[3]]
        else:
            return default
    except:
        return default

def get_issue(pr):
    try:
        issues = []
        for item in re.findall("#([0-9])+\w+", pr["body"]):
            issues.append(item.replace("#", ""))

        for item in re.findall("#([0-9])+\w+", pr["title"]):
            issues.append(item.replace("#", ""))
        return issues
    except:
        return ["N/A"]

def merge_comments(comments):
    result = ""
    for comment in comments:
        result = result + " =||= " + comment["body"]
    return result

def format_data_issues(issue, comments):
    try:
        issue_results = [
            result_value(issue, ["number"], "N/A"),
            result_value(issue, ["closed_at"], "N/A"),
            result_value(issue, ["user", "login"], "N/A"),
            result_value(issue, ["title"], "N/A"),
            result_value(issue, ["body"], "N/A"),
            merge_comments(comments)
        ]

        return issue_results
    except Exception:
        return ["N/A", "N/A", "N/A", "N/A", "N/A"]


def format_data_skills(pr_num, pulls, commits, status, user, password, comments):
    try:
        data = []
        for file in commits["files"]:
            skill_in_file = parse_skills(file["patch"], file, user, password)
            for file_index in skill_in_file:
                if skill_in_file != []:
                    data.append(file_index[0])
    except Exception as e:
        print(e)

    try:
        skill_results = []  
        for item in data:
            for item2 in item[1:]:
                skill_results.append(
                [
                    pr_num,
                    result_value(pulls, ["title"], "N/A"),
                    result_value(pulls, ["body"], "N/A"),
                    item[0], item2[0], item2[1], item2[2], item2[3]
                ])
    except Exception as ex:
        pass

    return skill_results


def format_data_pr(pr_num, pulls, commits, status, user, password, comments):
    try:
        files = "["
        patch = "["
        for file in commits["files"]:
            files = files + file["filename"] + ", "
            patch = patch + file["patch"] + ", "
        files = files + "]"
        patch = patch + "]"
    except:
        pass

    issues = get_issue(pulls)
    
    pr_results = []
    try:
        for issue in issues:
            pr_results.append([
                pr_num,
                result_value(pulls, ["closed_at"], "N/A"),
                result_value(pulls, ["user", "login"], "N/A"),
                result_value(pulls, ["title"], "N/A"),
                result_value(pulls, ["body"], "N/A"),
                merge_comments(comments),
                issue
            ])
    except Exception as ex:
        pass

    try:
        commit_results = [
            pr_num,
            result_value(commits, ["commit", "author", "name"], "N/A"),
            result_value(commits, ["commit", "committer", "date"], "N/A"),
            result_value(commits, ["commit", "message"], "N/A"),
            patch,
        ]
    except Exception as ex:
        commit_results = [
            "N/A", "N/A","N/A","N/A","N/A"
        ]

    return (pr_results, commit_results)