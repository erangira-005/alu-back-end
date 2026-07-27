#!/usr/bin/python3
"""Export a given employee's TODO list to a CSV file.

Uses the JSONPlaceholder REST API. Takes an employee ID as a command-line
argument and writes all of that employee's tasks to USER_ID.csv in the
format: "USER_ID","USERNAME","TASK_COMPLETED_STATUS","TASK_TITLE".
"""
import csv
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

    with open("{}.csv".format(employee_id), "w", newline="") as csvfile:
        writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
        for task in todos:
            writer.writerow([
                employee_id,
                username,
                task.get("completed"),
                task.get("title"),
            ])