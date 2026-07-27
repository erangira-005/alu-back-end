#!/usr/bin/python3
"""Fetch and display a given employee's TODO list progress.

Uses the JSONPlaceholder REST API. Takes an employee ID as a command-line
argument and prints how many of that employee's tasks are completed,
followed by the title of each completed task.
"""
import requests
import sys


if __name__ == "__main__":
    employee_id = sys.argv[1]
    base_url = "https://jsonplaceholder.typicode.com"

    user = requests.get("{}/users/{}".format(base_url, employee_id)).json()
    todos = requests.get(
        "{}/todos".format(base_url), params={"userId": employee_id}
    ).json()

    employee_name = user.get("name")
    completed_tasks = [t for t in todos if t.get("completed") is True]
    total_tasks = len(todos)

    print("Employee {} is done with tasks({}/{}):".format(
        employee_name, len(completed_tasks), total_tasks))

    for task in completed_tasks:
        print("\t {}".format(task.get("title")))