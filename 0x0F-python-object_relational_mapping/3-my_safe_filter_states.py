#!/usr/bin/python3

if __name__ == '__main__':
    import MySQLdb
    import sys

    # Connect to database
    db = MySQLdb.connect("localhost", sys.argv[1], sys.argv[2], sys.argv[3])

    # Initialize cursor to execute commands
    cursor = db.cursor()

    # Command to be executed
    state_name = sys.argv[4]
    query = "SELECT * FROM states WHERE name = %s"

    # Use cursor to execute command
    cursor.execute(query, (state_name,))

    # Store results and print
    results = cursor.fetchall()
    for item in results:
        print(item)

    cursor.close()  # Close cursor
    db.close()  # Close connection
