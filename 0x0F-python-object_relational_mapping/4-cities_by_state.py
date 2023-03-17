#!/usr/bin/python3

if __name__ == '__main__':
    import MySQLdb
    import sys

    # Connect to database
    db = MySQLdb.connect("localhost", sys.argv[1], sys.argv[2], sys.argv[3])

    # Initialize cursor to execute commands
    cursor = db.cursor()

    # Command to be executed
    query = "SELECT cities.id, cities.name, states.name \
    FROM cities INNER JOIN states ON cities.state_id = states.id \
    ORDER BY cities.id ASC"

    # Use cursor to execute command
    cursor.execute(query)

    # Store results and print
    results = cursor.fetchall()
    for item in results:
        print(item)

    cursor.close()  # Close cursor
    db.close()  # Close connection
