#!/usr/bin/python3

import MySQLdb
import sys

# Connect to database
db = MySQLdb.connect("localhost", sys.argv[1], sys.argv[2], sys.argv[3])

# Initialize cursor to execute commands
cursor = db.cursor()

# Command to be executed
query = "SELECT * FROM states ORDER BY states.id ASC"

# Use cursor to execute command
cursor.execute(query)

# Store results and print
results = cursor.fetchall()
for item in results:
    print(item)

cursor.close()  # Close cursor
db.close()  # Close connection
