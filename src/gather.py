import src.api as api
import src.pipelines as pipes
import src.args as types

def run(args:list, gather:dict):
    results = []
    for arg in args:
        try:
            range_start = arg["range"]["start"]
            range_end = arg["range"]["stop"]
        except:
            range_start = 0
            range_end = 1

        for index in range(range_start, range_end):
            for item in gather:
                if arg["type"] != item["type"]: 
                    continue

                result = request(index, arg["type"], arg, item)

                if result != {} or result != []:
                    #* Run thorugh pipes
                    result = pipes.pipeline_data(result, item["data"]["pipeline"])

                    #* Note: Append None Empty Response
                    results.append(result)
    return results

def request(index: int, data_type:str, arg:dict, item:dict):
    type_data = types.types[data_type](index, arg)
    return api.request(type_data, item["data"]["fetch"], item["data"]["get"])
