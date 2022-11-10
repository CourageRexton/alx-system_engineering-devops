#!/usr/bin/python3
"""
Extends Python script to export data in the JSON format
"""
import json
import requests
import sys

if __name__ == "__main__":
    api_url = "https://jsonplaceholder.typicode.com/"
    user = requests.get(api_url + "users/{}".format(sys.argv[1])).json()
    username = user.get("username")
    todos = requests.get(
        api_url + "todos", params={"userId": sys.argv[1]}).json()

    with open("{}.json".format(sys.argv[1]), "w") as jsonfile:
        json.dump({sys.argv[1]: [{
                "task": t.get("title"),
                "completed": t.get("completed"),
                "username": username
            } for t in todos]}, jsonfile)
