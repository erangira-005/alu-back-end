#!/usr/bin/python3
"""Export a given employee's TODO list to a JSON file.

Uses the JSONPlaceholder REST API. Takes an employee ID as a command-line
argument and writes all of that employee's tasks to USER_ID.json in the
format: {"USER_ID": [{"task": ..., "completed": ..., "username": ...}, ...]}.
"""
import json
import requests
import sys


if __name__ == "__main__":
    employee_id = sys.argv[1]
    base_url = "https://jsonplaceholder.typicode.com"

    user = requests.get("{}/users/{}".format(base_url, employee_id)).json()
    todos = requests.get(
        "{}/todos".format(base_url), params={"userId": employee_id}
    ).json()

    username = user.get("username")

    tasks = [{
        "task": task.get("title"),
        "completed": task.get("completed"),
        "username": username,
    } for task in todos]

    with open("{}.json".format(employee_id), "w") as jsonfile:
        json.dump({employee_id: tasks}, jsonfile)