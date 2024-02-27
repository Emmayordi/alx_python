def export_to_csv(employee_id, todos_data):
    """
    Export TODO list data to CSV.
    """
    if not todos_data:
        print(f"No TODO data found for employee {employee_id}.")
        return

    user_info = todos_data[0]["userId"]
    user_name = todos_data[0]["name"]  # Change "username" to "name"
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
