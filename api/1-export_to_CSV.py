#!/usr/bin/python3
''''is this just fantasy'''
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

    f = open(str(eval(identity)) + ".csv", "x")

    for task in list:
        csv = '"' + str(user.get("id")) + '","' + str(
            user.get("username")) + '","' + str(
                task.get("completed")) + '","' + str(
                    task.get("title")) + '"\n'
        f.write(csv)
