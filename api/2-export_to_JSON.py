#!/usr/bin/python3
''''easy come'''
import json
import requests
import sys
if __name__ == '__main__':
    identity = sys.argv[1]
    payload = {"userId": identity}
    user = requests.get(
        "https://jsonplaceholder.typicode.com/users/{}"
        .format(identity)).json()
    list = requests.get(
        "https://jsonplaceholder.typicode.com/todos",
        params=payload).json()
    jsonn = {}
    for task in list:
        jsonn.update({user.get("id"): [{"task": task.get("task"),
                                        "completed": task.get("completed"),
                                        "username": user.get("username")}]})
    with open(identity + ".json", 'w') as f:
        json.dump(jsonn, f)
