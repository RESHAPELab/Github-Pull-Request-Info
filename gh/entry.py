import gh.auth as auth
import gh.config as config
import gh.gather as gather
import gh.file as file

class __MineMeta(type):
    def __new__(cls, clsname, supercls, attributes):
        print(cls)


#* Define Inside Main
class Config(metaclass=__MineMeta):
''' Configs the framework and sets everything up'''
    def __init__(self, users:list):
        self.users = users

class Mine(metaclass=__MineMeta):
''' Mines the github REST API'''
    def __init__(self, configs):
        self.result = None
        self.fetch_ref = None
        self.pipe_ref = None

        #* Bools
        self.csv = False
        self.json = False
        self.returnable = False

        #* Defaults
        self.static = {}
        self.dynamic = {}
        self.start = 0
        self.stop = 1
        
    def statics(self, data:dict):
    ''' Data that is used during the data minning process '''
        self.static = data
        return self

    def dynamics(self, data:dict):
    ''' Data that is used during the data minning process '''
        self.dynamic = data
        return self

    def fetch(self, fetch_ref:object):
    ''' Defines the data that is to be fetched from the github API.'''
        self.fetch_ref = fetch_ref
        return self

    def pipe(self, pipe_ref:str):
    ''' Defines the pipes in which the results are to be ran through'''
        self.pipe_ref = pipe_ref
        return self

    def limit(self, start:int = 0, stop:int = 10000):
    '''Defines a limit to run through '''
        self.start = start
        self.stop = stop
        return self

    def to_json(self, location:str):
    '''Creates a JSON File with the results'''
        file.to_json(location+".json", self.result)
        return self

    def to_csv(self, location:str):
    '''Creates a CSV File with the results'''
        file.to_csv(location+".csv", self.result)
        return self

    def return_result(self):
    '''Returns the result of the data mine as a dictionary'''
        return self

    def mine(self):
    '''Runs the github api minning'''
        return self.result

class Fetch(metaclass=__MineMeta):
    def __init__(self, get_list:list):
        pass

    def ref(self):
        return ""

#* Define Inside Pipe
class __PipeMeta(type):
    def __new__(cls, clsname, supercls, attributes):
        print(cls)

class Pipe:
    def __init__(self, pipe_list:list):
        pass

class DefinePipe(metaclass=__PipeMeta):
    def __init__(self, name, function, description):
        pass)