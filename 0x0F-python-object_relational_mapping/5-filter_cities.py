#!/usr/bin/python3
""" Lists all cities of a state passed as argument. """

if __name__ == '__main__':
    import MySQLdb
    import sys

    # Connect to database
    db = MySQLdb.connect("localhost", sys.argv[1], sys.argv[2], sys.argv[3])

    # Initialize cursor to execute commands
    cursor = db.cursor()

    # Command to be executed
    state_name = sys.argv[4]
    query = "SELECT cities.name FROM cities \
            LEFT JOIN states ON cities.state_id = states.id \
            WHERE states.name = %s ORDER BY cities.id ASC"

    # Use cursor to execute command
    cursor.execute(query, (state_name,))

    # Store results and print
    results = cursor.fetchall()
    cities_list = []
    for item in results:
        # Result is a tuble so extract first element only
        cities_list.append(item[0])
    print(', '.join(cities_list))

    cursor.close()  # Close cursor
    db.close()  # Close connection
