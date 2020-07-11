import requests, src.auth as auth, src.endpoints as endpoints

def send_request(url):
    account = auth.Auth.get()
    current_request = requests.get(url, auth=account)
    auth.Auth.check(current_request)
    
    try:
        return current_request.json()
    except:
        return current_request.text

_endpoints = endpoints._endpoints

def get_args(general, arg_list):
    args = {}
    for arg in arg_list:
        if arg in general:
            try:
                if general[arg][:4] == "get@":
                    #* NOTE: Get Keys
                    key_def = general[arg][4:].split("/")
                    endpoint = key_def[0]
                    temp_args = get_args(general, _endpoints[endpoint]["args"])
                    results = send_request(_endpoints[endpoint]["url"](temp_args))
                    
                    if result_failed(results):
                        continue

                    new_args = get_def(results, key_def[1:], arg)
                    args[arg] = new_args[arg]
                    print(temp_args)
                else:
                    #* NOTE: Filter Args
                    if arg in general:
                        args[arg] = general[arg]
                    else:
                        raise Exception("Arg not available: %s" % arg)
            except:
                #* NOTE: Filter Args
                if arg in general:
                    args[arg] = general[arg]
                else:
                    raise Exception("Arg not available: %s" % arg)
    return args

def result_failed(dictionary:dict):
    try:
        temp_dict["message"]
        return True
    except:
        return False

def parse_defs(result, items):
    defs = {}

    for item in items.keys():
        if "alias" in items[item]:
            new_def = get_def(result, item.split("/"), items[item]["alias"])
        else:
            new_def = get_def(result, item.split("/"))
        defs.update(new_def)

    return defs
    

def get_def(results, defs, alias = ""):
    filtered = {}
    temp_dict = results

    for key_def in defs:
        for key in key_def:
            if key_def in temp_dict:
                if key_def == defs[-1]:
                    if alias == "":
                        alias =  key_def

                    if temp_dict[key_def][:4] == "http":
                        filtered[alias] = send_request(temp_dict[key_def])
                    else:
                        filtered[alias] = temp_dict[key_def]
                else:
                    if type(temp_dict[key_def]) == 'str' and temp_dict[key_def][:4] == "http":
                        temp_dict = send_request(temp_dict[key_def])
                    else:
                        temp_dict = temp_dict[key_def]
            else:
                break

    return filtered

def request(general:dict, fetches:list, items:list):
    for fetch in fetches:
        args = get_args(general, _endpoints[fetch]["args"])
        result = send_request(_endpoints[fetch]["url"](args))
        return parse_defs(result, items)
    