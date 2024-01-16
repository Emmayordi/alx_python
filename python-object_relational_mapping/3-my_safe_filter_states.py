"""
Script that takes in an argument and displays all values
safe from MySQL injections!
"""
import MySQLdb
from sys import argv

# The code should not be executed when imported
if __name__ == '__main__':

    
    db = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                         passwd=argv[2], db=argv[3])

    
   
    cur = db.cursor()
    cur.execute("SELECT * FROM states WHERE BINARY name = %s", [argv[4]])

    rows = cur.fetchall()
    for i in rows:
        print(i)
    # Clean up process
    cur.close()
    db.close()