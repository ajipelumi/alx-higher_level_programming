#!/usr/bin/python3
""" Displays all values in states table of where name matches the argument. """

if __name__ == '__main__':
    import MySQLdb
    import sys

    # Connect to database
    db = MySQLdb.connect("localhost", sys.argv[1], sys.argv[2], sys.argv[3])

    # Initialize cursor to execute commands
    cursor = db.cursor()

    # Command to be executed
    state_name = sys.argv[4]
    query = "SELECT * FROM states WHERE BINARY name = '{0}' \
            ORDER BY states.id ASC".format(state_name)

    # Use cursor to execute command
    cursor.execute(query)

    # Store results and print
    results = cursor.fetchall()
    for item in results:
        print(item)

    cursor.close()  # Close cursor
    db.close()  # Close connection
