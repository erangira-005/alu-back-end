#!/usr/bin/python3
"""Gather data from a REST API for a given employee's TODO progress."""
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
    total_tasks = len(todos)
    done_tasks = [task for task in todos if task.get("completed")]
    number_of_done_tasks = len(done_tasks)

    print("Employee {} is done with tasks({}/{}):".format(
        employee_name, number_of_done_tasks, total_tasks))

    for task in done_tasks:
        print("\t {}".format(task.get("title")))
