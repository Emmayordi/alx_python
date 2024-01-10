"""
Python script that takes your GitHub 
credentials (username and password) and 
uses the GitHub API to display your id
"""

import requests
import sys

if __name__ == "__main__":
    url = "https://api.github.com/Emmayordi"
    username = sys.argv[1]
    password = sys.argv[2]
    response = requests.get(url, auth=(username, password))
    if response.status_code == 200:
        json_response = response.json()
        print(json_response.get("id"))
    else:
        print("None")