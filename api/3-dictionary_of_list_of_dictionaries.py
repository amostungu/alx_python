#!/usr/bin/python3
"""
Write a Python script that, using this REST API,
for all employees, returns information about
their TODO list progress and exports it in JSON format.
"""

import requests
import sys

def get_all_employee_data():
    # Define the base URL for the JSONPlaceholder API
    base_url = "https://jsonplaceholder.typicode.com"

    # Fetch all users
    users_url = f"{base_url}/users"
    try:
        response = requests.get(users_url)
        response.raise_for_status()
        all_users = response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching user data: {e}")
        sys.exit(1)

    # Initialize a dictionary to store tasks for all users
    all_tasks = {}

    for user in all_users:
        user_id = user["id"]
        username = user["username"]

        # Construct the URL for the TODO list of the current user
        todo_url = f"{base_url}/users/{user_id}/todos"

        # Fetch TODO list for the current user
        try:
            response = requests.get(todo_url)
            response.raise_for_status()
            todo_data = response.json()
        except requests.exceptions.RequestException as e:
            print(f"Error fetching TODO list for user {user_id}: {e}")
            continue

        # Extract relevant information and organize tasks
        user_tasks = [{"username": username, "task": task["title"], "completed": task["completed"]} for task in todo_data]

        # Store tasks in the dictionary
        all_tasks[user_id] = user_tasks

    return all_tasks

if __name__ == "__main__":
    # Fetch and organize tasks for all employees
    all_employee_tasks = get_all_employee_data()

    # Export tasks to JSON file
    with open("todo_all_employees.json", "w") as json_file:
        json_file.write(str(all_employee_tasks))

    # Check if all users exist in the JSON output
    all_users_exist = all(user["id"] in all_employee_tasks for user in all_users)

    if all_users_exist:
        print("All users found: OK")
    else:
        print("Not all users found in the JSON output")

    # Check if all tasks are correctly assigned to the user IDs
    user_tasks_correct = all(len(tasks) == len(all_employee_tasks[user["id"]]) for user in all_users)

    if user_tasks_correct:
        print("User ID and Tasks output: OK")
    else:
        print("Tasks are not correctly assigned to the user IDs")
