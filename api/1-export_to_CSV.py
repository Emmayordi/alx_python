#!/usr/bin/python3
"""
Module to export data to CSV
"""
import requests
import sys
import csv

def gather_data(employee_id):
    """
    Function to gather and display employee TODO list progress
    """
    # API endpoints
    user_url = f'https://jsonplaceholder.typicode.com/users/{employee_id}'
    todo_url = f'https://jsonplaceholder.typicode.com/users/{employee_id}/todos'

    # Fetching data from API
    user_response = requests.get(user_url)
    todo_response = requests.get(todo_url)

    # Checking if requests were successful
    if user_response.status_code != 200:
        print("Error: Unable to fetch user data")
        return

    if todo_response.status_code != 200:
        print("Error: Unable to fetch TODO data")
        return

    # Extracting relevant information
    user_data = user_response.json()
    todo_data = todo_response.json()

    # Exporting to CSV
    csv_file_name = f"{employee_id}.csv"
    with open(csv_file_name, mode='w', newline='') as csv_file:
        fieldnames = ["USER_ID", "USERNAME", "TASK_COMPLETED_STATUS", "TASK_TITLE"]
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

        writer.writeheader()
        for task in todo_data:
            writer.writerow({
                "USER_ID": user_data["id"],
                "USERNAME": user_data["username"],
                "TASK_COMPLETED_STATUS": str(task["completed"]),
                "TASK_TITLE": task["title"]
            })

    print(f"Data exported to {csv_file_name}")

if __name__ == "__main__":
    if len(sys.argv) != 2 or not sys.argv[1].isdigit():
        print("Usage: python3 1-export_to_CSV.py <employee_id>")
        sys.exit(1)

    employee_id = int(sys.argv[1])
    gather_data(employee_id)
