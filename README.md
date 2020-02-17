# Github Pull Request Info
The purpose of this repository is to facilitate research for Marco Gerosa and Igor Steinmacher regarding drive by commits and pull requests. It allows for the collection of pooled data in a resulting .csv format, for further analysis in any statistical based language.

This tool is written in the Python programming language, and leverages the GitHub API to mine/download information in the form of JSON files, on provided repositories of interest chosen by Marco Gerosa and Igor Steinmacher.


## Setup
1. Install python:latest, postgres, and the python modules requests, psycopg2, and configs
2. Change config values in `src/.conf` to suit run
3. run `py ./src/init.py` from root directory


## How to run
After setup run `py ./src/main.py` from root directory