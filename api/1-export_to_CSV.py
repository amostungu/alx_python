#!/usr/bin/python3
"""
Using what you did in the task #0, extend your Python
script to export data in the CSV format.
"""

import csv
import requests
import sys

def get_employee_data(employee_id):
    # Define the base URL for the JSONPlaceholder API
    base_url = "https://jsonplaceholder.typicode.com"

    # Construct the URLs for employee details and TODO list
    employee_url = f"{base_url}/users/{employee_id}"
    todo_url = f"{base_url}/users/{employee_id}/todos"

    # Fetch employee details
    try:
        response = requests.get(employee_url)
        response.raise_for_status()
        employee_data = response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching employee details: {e}")
        sys.exit(1)

    # Fetch TODO list
    try:
        response = requests.get(todo_url)
        response.raise_for_status()
        todo_data = response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching TODO list: {e}")
        sys.exit(1)

    return employee_data, todo_data

def export_to_csv(employee_id, employee_name, todo_data):
    # Define the CSV file name
    csv_filename = f"{employee_id}.csv"

    # Write tasks to CSV file
    with open(csv_filename, mode='w', newline='') as file:
        writer = csv.writer(file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

        # Write header row
        writer.writerow(["USER_ID", "USERNAME", "TASK_COMPLETED_STATUS", "TASK_TITLE"])

        # Write tasks
        for task in todo_data:
            writer.writerow([employee_id, employee_name, task["completed"], task["title"]])

def display_todo_progress(employee_name, todo_data):
    completed_tasks = [task for task in todo_data if task["completed"]]
    total_tasks = len(todo_data)

    # Display employee TODO list progress
    print(f"Employee {employee_name} is done with tasks({len(completed_tasks)}/{total_tasks}):")
    for task in completed_tasks:
        print(f"\t{task['title']}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python gather_data_and_export.py <employee_id>")
        sys.exit(1)

    try:
        employee_id = int(sys.argv[1])
    except ValueError:
        print("Employee ID must be an integer.")
        sys.exit(1)

    employee_data, todo_data = get_employee_data(employee_id)
    employee_name = employee_data.get("name")
    
    export_to_csv(employee_id, employee_name, todo_data)
    display_todo_progress(employee_name, todo_data)
