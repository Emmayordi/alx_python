#!/usr/bin/env python3
"""
Script to gather data from a REST API for a given employee ID and export it to CSV.
"""

import requests
import csv
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

def export_to_csv(employee_id, todos_data):
    """
    Export TODO list data to CSV.
    """
    user_info = todos_data[0]["userId"]
    user_name = todos_data[0]["username"]
    filename = f"{user_info}.csv"

    with open(filename, mode="w", newline="") as csvfile:
        fieldnames = ["USER_ID", "USERNAME", "TASK_COMPLETED_STATUS", "TASK_TITLE"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()

        for todo in todos_data:
            writer.writerow({
                "USER_ID": user_info,
                "USERNAME": user_name,
                "TASK_COMPLETED_STATUS": str(todo["completed"]),
                "TASK_TITLE": todo["title"]
            })

def main():
    """
    Main function to execute the script.
    """
    if len(argv) != 2:
        print("Usage: python3 1-export_to_CSV.py <employee_id>")
        return

    employee_id = int(argv[1])
    _, todos_data = fetch_employee_data(employee_id)

    if not todos_data:
        print("Employee not found.")
        return

    export_to_csv(employee_id, todos_data)

if __name__ == "__main__":
    main()
