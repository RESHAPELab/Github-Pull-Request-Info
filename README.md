# Github Pull Request Info
The purpose of this repository is to facilitate research for Marco Gerosa and Igor Steinmacher regarding drive by commits and pull requests. It allows for the collection of pooled data in a resulting .csv format, for further analysis in any statistical based language.

This tool is written in the Python programming language, and leverages the GitHub API to mine/download information in the form of JSON files, on provided repositories of interest chosen by Marco Gerosa and Igor Steinmacher.


## Setup
1. Change the Config files in the configs directory to the desired outcome. You can have multiple configs.
2. Change the main.py file to get the desired outcome. By default the main.py is set up to collect pull request information.

## How to run
After setup run `python main.py` from root directory

## Modufications
If you want to add a new pipe, add a new python file to the directory `.\pipes` with that name being the name of the pipe. The program will call the run function within that file to operate so that needs to be in the newly created file. This is an example.
 
``` python
def run(inp):
    print(f"Logged: {inp}")
    return inp
```