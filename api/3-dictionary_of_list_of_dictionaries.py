#!/usr/bin/python3
"""
Module to export data to JSON
"""
import json
import requests
import sys

def export_to_json():
    """
    Function to export all employee TODO lists to a JSON file
    """
    # API endpoint for fetching user data
    users_url = 'https://jsonplaceholder.typicode.com/users'

    try:
        # Fetching user data
        users_response = requests.get(users_url)
        users_response.raise_for_status()
        users_data = users_response.json()

        # Check if users_data is non-empty
        if not users_data:
            print("No users found.")
            sys.exit(1)

    except requests.exceptions.HTTPError as errh:
        print("HTTP Error:", errh)
        sys.exit(1)
    except requests.exceptions.ConnectionError as errc:
        print("Error Connecting:", errc)
        sys.exit(1)
    except requests.exceptions.Timeout as errt:
        print("Timeout Error:", errt)
        sys.exit(1)
    except requests.exceptions.RequestException as err:
        print("Oops! Something went wrong:", err)
        sys.exit(1)

    # Dictionary to store tasks of all employees
    all_employees_tasks = {}

    # Fetch tasks for each user
    for user in users_data:
        employee_id = user['id']
        user_url = f'https://jsonplaceholder.typicode.com/users/{employee_id}/todos'

        try:
            # Fetching tasks for the current employee
            todo_response = requests.get(user_url)
            todo_response.raise_for_status()
            todo_data = todo_response.json()

        except requests.exceptions.HTTPError as errh:
            print("HTTP Error:", errh)
            sys.exit(1)
        except requests.exceptions.ConnectionError as errc:
            print("Error Connecting:", errc)
            sys.exit(1)
        except requests.exceptions.Timeout as errt:
            print("Timeout Error:", errt)
            sys.exit(1)
        except requests.exceptions.RequestException as err:
            print("Oops! Something went wrong:", err)
            sys.exit(1)

        # List to store tasks of the current employee
        employee_tasks = []

        # Populating tasks list with dictionaries
        for task in todo_data:
            employee_tasks.append({
                "username": user['username'],
                "task": task["title"],
                "completed": task["completed"]
            })

        # Adding tasks list to the dictionary
        all_employees_tasks[str(employee_id)] = employee_tasks

    # Writing data to JSON
    json_file_name = 'todo_all_employees.json'
    with open(json_file_name, mode='w') as json_file:
        json.dump(all_employees_tasks, json_file)

    print(f"Data exported to {json_file_name}")

    print("All users found: OK")

if __name__ == "__main__":
    export_to_json()
