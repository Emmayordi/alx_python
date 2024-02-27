#!/usr/bin/python3
"""
Module to gather data from an API
"""
import requests
import sys

def gather_data(employee_id):
    """
    Function to gather and display employee TODO list progress
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
        print ("HTTP Error:", errh)
        sys.exit(1)
    except requests.exceptions.ConnectionError as errc:
        print ("Error Connecting:", errc)
        sys.exit(1)
    except requests.exceptions.Timeout as errt:
        print ("Timeout Error:", errt)
        sys.exit(1)
    except requests.exceptions.RequestException as err:
        print ("Oops! Something went wrong:", err)
        sys.exit(1)

    # Processing TODO list
    total_tasks = len(todo_data)
    done_tasks = [task for task in todo_data if task['completed']]

    # Displaying output in the specified format
    print(f"Employee {user_data['name']} is done with tasks({len(done_tasks)}/{total_tasks}):")
    for task in done_tasks:
        print(f"\t{task['title']}")

if __name__ == "__main__":
    if len(sys.argv) != 2 or not sys.argv[1].isdigit():
        print("Usage: python3 0-gather_data_from_an_API.py <employee_id>")
        sys.exit(1)

    employee_id = int(sys.argv[1])
    gather_data(employee_id)
