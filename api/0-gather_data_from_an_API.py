import requests
import sys

def get_employee_data(employee_id):
    """Defining the API endpoint for employee"""
    employee_url = request.get('https://jsonplaceholder.typicode.com/users/{employee_id}')
    todo_url = request.get('https://jsonplaceholder.typicode.com/users/{employee_id}/todos')

    try:
        #Getting the employee details
        employee_response = requests.get(employee_url)
        employee_data = employee_response.json()
        employee_name = employee_data.get('name')

        #Getting Todo list
        todo_response = requests.get(todo_url)
        todo_list = todo_response.json()

        #Getting number of completed items
        completed_tasks = [task for task in todo_list if task['completed']]
        total_tasks = len(todo_list)
        num_completed = len(completed_tasks)

        #Get output results
        print(f'Employee {employee_name} is done with tasks({num_completed}/{total_tasks}):')
        for task in completed_tasks:
            print(f"\t{task['title']}")

    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 0-gather_data_from_an_API.py <employee_id>")
        sys.exit(1)

    employee_id = int(sys.argv[1])
    get_employee_data(employee_id)
