#!/usr/bin/python3
"""Export every employee's TODO list to a single JSON file.

Uses the JSONPlaceholder REST API. Fetches all users and all tasks, then
writes them to todo_all_employees.json in the format:
{"USER_ID": [{"username": ..., "task": ..., "completed": ...}, ...], ...}.
"""
import json
import requests


if __name__ == "__main__":
    base_url = "https://jsonplaceholder.typicode.com"

    users = requests.get("{}/users".format(base_url)).json()
    todos = requests.get("{}/todos".format(base_url)).json()

    all_tasks = {}
    for user in users:
        user_id = user.get("id")
        username = user.get("username")
        all_tasks[str(user_id)] = [{
            "username": username,
            "task": task.get("title"),
            "completed": task.get("completed"),
        } for task in todos if task.get("userId") == user_id]

    with open("todo_all_employees.json", "w") as jsonfile:
        json.dump(all_tasks, jsonfile)