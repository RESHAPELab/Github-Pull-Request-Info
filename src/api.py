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

def request(general:dict, fetches:list, items:list):
    #* Note: Initial Request
    results = {}
    for fetch in fetches:
        args = {}
        for arg in _endpoints[fetch]["args"]:
            if arg in general:
                args[arg] = general[arg]
        if len(args) == len(_endpoints[fetch]["args"]):
            result = send_request(_endpoints[fetch]["url"](args))
        results[fetch] = result
    
    #* Sequential Requests and grab values
    result_dict = {}
    for item in items:
        item = item.split("~")[0]
        key_list = item.split("/")

        if len(key_list) == 1:
            try:
                temp_dict["message"]
                continue
            except:
                pass
            result_dict[item] = results[key_list[0]]
            continue
        
        temp_dict = results[key_list[0]]

        try:
            temp_dict["message"]
            continue
        except:
            pass

        for key in key_list[1:]:
            if key in temp_dict:
                if key == key_list[-1]:
                    if temp_dict[key][:4] == "http":
                        result_dict[item] = send_request(temp_dict[key])
                        break
                    result_dict[item] = temp_dict[key]
                    break
                if type(temp_dict[key]) is str:
                    temp_dict = send_request(temp_dict[key])
                    if type(temp_dict) is str:
                        result_dict[item] = temp_dict
                        break
                else:
                    temp_dict = temp_dict[key]
            else:
                break

    return result_dict