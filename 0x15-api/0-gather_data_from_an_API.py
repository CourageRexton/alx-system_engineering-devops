#!/usr/bin/python3
"""
A Python script that, using this REST API,
for a given employee ID, returns information
about his/her TODO list progress.
"""
import requests
import sys

if __name__ == "__main__":
    api_url = "https://jsonplaceholder.typicode.com/"
    response = requests.get(api_url + "users/{}".format(sys.argv[1])).json()
    todos = requests.get(
        api_url + "todos", params={"userId": sys.argv[1]}).json()

    completed = [t.get("title") for t in todos if t.get("completed") is True]
    print("Employee {} is done with tasks({}/{}):".format(
        response.get("name"), len(completed), len(todos)))
    [print("\t {}".format(c)) for c in completed]
