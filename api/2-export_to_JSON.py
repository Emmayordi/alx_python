#!/usr/bin/python3
"""
Module to export data to JSON
"""
import json
import requests
import sys


def export_to_json(employee_id):
    """
    Function to export employee TODO list to a JSON file
    """
    # API endpoints
    user_url = f'https://jsonplaceholder.typicode.com/users/{employee_id}'
    todo_url = f'https://jsonplaceholder.typicode.com/users/{employee_id}/todos'

    # Fetching data from API
    try:
        user_response = requests.get(user_url)
        user_response.raise_for_status()
        user_data = user_response.json()

        todo_response = requests.get(todo_url)
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

    # JSON file name
    json_file_name = f"{employee_id}.json"

    # Creating JSON data
    json_data = {str(user_data["id"]): []}
    for task in todo_data:
        json_data[str(user_data["id"])].append({
            "task": task["title"],
            "completed": task["completed"],
            "username": user_data["username"]
        })

    # Writing data to JSON
    with open(json_file_name, mode='w') as json_file:
        json.dump(json_data, json_file)

    print(f"Data exported to {json_file_name}")

if __name__ == "__main__":
    if len(sys.argv) != 2 or not sys.argv[1].isdigit():
        print("Usage: python3 2-export_to_JSON.py <employee_id>")
        sys.exit(1)

    employee_id = int(sys.argv[1])
    export_to_json(employee_id)
