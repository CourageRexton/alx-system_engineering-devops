#!/usr/bin/python3
"""
Extends Python script to export data in the CSV format
"""
import csv
import requests
import sys

if __name__ == "__main__":
    api_url = "https://jsonplaceholder.typicode.com/"
    user = requests.get(api_url + "users/{}".format(sys.argv[1])).json()
    username = user.get("username")
    todos = requests.get(
        api_url + "todos", params={"userId": sys.argv[1]}).json()

    with open("{}.csv".format(sys.argv[1]), "w", newline="") as csvfile:
        writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
        [writer.writerow(
            [sys.argv[1], username, t.get("completed"), t.get("title")]
        ) for t in todos]
