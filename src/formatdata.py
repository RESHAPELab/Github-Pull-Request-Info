import database, logging, requests

database = database.query_db()
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

def get_patch(file, user, token):
    path = ""

    for line in database[3]:
        if file == line[0]:
            path = line[1].split("/")[:6]

    try:
        content_response = requests.get("https://api.github.com/repos/Jabref/jabref/content/%s" % path, auth=(username,token))
        content = pr_response.text
        return content
    except:
        return None

def get_api_name(line):
    found_api = False
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

    return api_name

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

    return ",".join(skills)

def get_related_files(api_name):
    found_file = False
    files = []

    for line2 in database[1]:
        if api_name == (line2[1]).split(".")[-1]:
            files.append(line2[0])
            found_file = True

    #* Log Not found API in files
    if not found_file:
        logging.warning("import \"%s\" is not recorded in files table" % api_name)

    return files

def get_known_import(line, user, password):
    api_name = get_api_name(line)
    related_files = ""
    patch = []
    skills = ""

    if api_name is not None:
        #* Check Api DB
        skills = get_skills(api_name)
        related_files_list = get_related_files(api_name)

        for file in related_files_list:
            temp_patch = get_patch(file, user, password)
            if temp_patch is not None:
                patch.append("%s-%s"%(file, temp_patch))
        
        ",".join(related_files_list)
        ",".join(patch)
        
        return (api_name, skills, related_files, patch)
    else:
        return None

def parse_skills(text:str, file, user, password):
    lines = text.split("\n")
    results = []
    #* Get Import
    for line in lines:
        result = get_known_import(line, user, password)

        if result is None:
            pass
        else:
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

def format_data(pr_num, pulls, commits, status, user, password):
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

    try:
        data = []
        for file in commits["files"]:
            (api_name, skills, related_files, patch_list) = parse_skills(file["patch"], file, user, password)
            data.append("%s|%s|%s|%s"%(api_name, skills, related_files, patch_list))
    except:
        pass
    
    
    try:
        pr_result = [
            pr_num,
            result_value(pulls, ["user", "login"], "N/A"),
            result_value(pulls, ["user", "id"], "N/A"),
            result_value(pulls, ["state"], "N/A"),
            result_value(pulls, ["created_at"], "N/A"),
            result_value(pulls, ["closed_at"], "N/A"),
            result_value(pulls, ["title"], "N/A"),
            result_value(pulls, ["body"], "N/A"),
            result_value(pulls, ["comments"], "N/A"),
            result_value(pulls, ["review_comments"], "N/A"),
            result_value(pulls, ["additions"], "N/A"),
            result_value(pulls, ["deletions"], "N/A"),
            result_value(pulls, ["commits"], "N/A"),
            result_value(pulls, ["changed_files"], "N/A")
        ]
    except Exception as ex:
        pass


    

    try:
        commit_results = [
            result_value(commits, ["commit", "author", "name"], "N/A"),
            result_value(commits, ["commit", "committer", "name"], "N/A"),
            pr_num,
            result_value(commits, ["sha"], "N/A"),
            result_value(commits, ["commit", "message"], "N/A"),
            files,
            patch,
            result_value(commits, ["stats", "additions"], "N/A"),
            result_value(commits, ["stats", "deletions"], "N/A"),
            result_value(status, ["state"], "N/A"),
            result_value(commits, ["stats", "total"], "N/A")
        ]
    except Exception as ex:
        pass

    try:
        skill_results = [
            pr_num,
            result_value(pulls, ["title"], "N/A"),
            result_value(pulls, ["body"], "N/A"),
            data
        ]
    except Exception as ex:
        pass

    return (pr_result, commit_results, skill_results)