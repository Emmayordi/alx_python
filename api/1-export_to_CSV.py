#!/usr/bin/env python3
"""
Using what you did in the task #0, extend your Python script to export data in the CSV format.

"""
import csv
import requests
import sys

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
    if not todos_data:
        print(f"No TODO data found for employee {employee_id}.")
        return

    user_info = todos_data[0]["userId"]
    name = todos_data[0]["name"]  
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

    print(f"Exported data to {filename}.")

def main():
    """
    Main function to execute the script.
    """
    if len(sys.argv) != 2:
        print("Usage: python3 1-export_to_CSV.py <employee_id>")
        return

    employee_id = int(sys.argv[1])
    employee_data, todos_data = fetch_employee_data(employee_id)

    if "id" not in employee_data:
        print("Employee not found.")
        return

    export_to_csv(employee_id, todos_data)

if __name__ == "__main__":
    main()
