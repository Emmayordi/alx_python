import MySQLdb
import sys

def list_states(username, password, database_name):
    try:
        # Connect to MySQL server
        connection = MySQLdb.connect(host='localhost', port=3306, user=username, passwd=password, db=database_name)
        cursor = connection.cursor()

        # Execute SQL query to retrieve states
        query = "SELECT * FROM states ORDER BY states.id ASC"
        cursor.execute(query)

        # Fetch all rows
        states = cursor.fetchall()

        # Display results
        for state in states:
            print(state)

    except MySQLdb.Error as e:
        print(f"Error: {e}")

    finally:
        # Close the database connection
        if connection:
            connection.close()

if __name__ == "__main__":
    # Check if the correct number of arguments is provided
    if len(sys.argv) != 4:
        print("Usage: python script.py <username> <password> <database_name>")
        sys.exit(1)

    # Get MySQL credentials from command line arguments
    username, password, database_name = sys.argv[1:]

    # Call the function to list states
    list_states(username, password, database_name)
