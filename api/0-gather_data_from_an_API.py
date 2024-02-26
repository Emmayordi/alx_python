#!/usr/bin/env python3
"""
Script to gather data from a REST API for a given employee ID.
"""

import requests
from sys import argv

def fetch_employee_data(employee_id):
    """
    Fetch employee data from the API.
    """
    base_url = "https://jsonplaceholder.typicode.com/users"
    employee_url = f"{base_url}/{employee_id}"

    response_employee = requests.get(employee_url)
    response_todos = requests.get(f"{employee_url}/todos")

    return response_employee.json(), response_todos.json()

def display_todo_progress(employee_name, completed_tasks, total_tasks, completed_titles):
    """
    Display TODO list progress in the specified format.
    """
    print(f"Employee {employee_name} is done with tasks({completed_tasks}/{total_tasks}):")
    for title in completed_titles:
        print(f"\t{title}")

def main():
    """
    Main function to execute the script.
    """
    if len(argv) != 2:
        print("Usage: python3 0-gather_data_from_an_API.py <employee_id>")
        return

    employee_id = int(argv[1])
    employee_data, todos_data = fetch_employee_data(employee_id)

    if "id" not in employee_data:
        print("Employee not found.")
        return

    employee_name = employee_data["name"]
    completed_tasks = sum(todo["completed"] for todo in todos_data)
    total_tasks = len(todos_data)
    completed_titles = [todo["title"] for todo in todos_data if todo["completed"]]

    display_todo_progress(employee_name, completed_tasks, total_tasks, completed_titles)

if __name__ == "__main__":
    main()
