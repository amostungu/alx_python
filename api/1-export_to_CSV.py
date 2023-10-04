#!/usr/bin/python3
"""
Check student .CSV output of user information and export tasks in CSV format
"""

import csv
import requests
import sys

users_url = "https://jsonplaceholder.typicode.com/users?id="
todos_url = "https://jsonplaceholder.typicode.com/todos"


def export_tasks_to_csv(id, tasks):
    """ Export tasks to CSV format """
    filename = f"{id}.csv"

    with open(filename, 'w', newline='') as csvfile:
        fieldnames = ["USER_ID", "USERNAME", "TASK_COMPLETED_STATUS", "TASK_TITLE"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()  # Write CSV header

        for task in tasks:
            # Retrieve the username for the given user ID from the API
            response = requests.get(users_url + str(id)).json()
            username = response[0]['username']

            # Write task data to CSV
            writer.writerow({
                "USER_ID": id,
                "USERNAME": username,
                "TASK_COMPLETED_STATUS": str(task['completed']),
                "TASK_TITLE": task['title']
            })

    print(f"Tasks exported to {filename}")


def user_info(id):
    """ Check user information and export tasks to CSV """

    # Fetch tasks for the given user ID from the API
    tasks = [task for task in requests.get(todos_url).json() if task['userId'] == id]

    # Export tasks to CSV
    export_tasks_to_csv(id, tasks)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python check_student_output.py <employee_id>")
        sys.exit(1)

    try:
        user_info(int(sys.argv[1]))
    except ValueError:
        print("Employee ID must be an integer.")
        sys.exit(1)
