<img src="https://github.com/ajipelumi/alx-higher_level_programming/blob/392dd641fe826a020d58e4a2584974d009431b5c/images/orms-bridge.png" alt="object relational mapping" width=600px>
Image Credit: Full Stack Python

### Object Relational Mapping

**Object-relational mapping (ORM)** is a programming technique that allows developers to work with a relational database using an object-oriented approach.
In other words, it is a way of mapping database objects to objects in code.

The purpose of an ORM is to simplify the interaction between code and the database. Traditionally, when working with a database, we would write SQL queries to insert, update, or retrieve data from the database.
However, with an ORM, we can interact with the database using object-oriented programming (OOP) concepts such as classes, objects, and methods, making it easier and more intuitive to work with databases in code.

**MySQLdb** is a lightweight library that provides a simple interface for connecting to a MySQL database and executing queries.
Here's an example of using MySQLdb to connect to a MySQL database and execute a query:
```python
import MySQLdb

# Connect to the database
conn = MySQLdb.connect(host="localhost", user="user", passwd="password", db="database")

# Create a cursor object
cursor = conn.cursor()

# Execute a query
cursor.execute("SELECT * FROM users")

# Fetch the results
results = cursor.fetchall()

# Print the results
for row in results:
    print(row)

# Close the cursor and connection
cursor.close()
conn.close()
```

**SQLAlchemy** is a powerful ORM library that provides a higher-level interface for working with databases.
It supports many different database systems, including MySQL, and provides a wide range of features such as database schema management, connection pooling, and transaction management.
Here's an example of using SQLAlchemy to connect to a MySQL database and execute a query:
```python
from sqlalchemy import create_engine

# Create a connection to the database
engine = create_engine("mysql://user:password@localhost/database")

# Execute a query and fetch the results
with engine.connect() as conn:
    result = conn.execute("SELECT * FROM users")
    for row in result:
        print(row)
```

**SQLAlchemy** provides a higher-level and more Pythonic interface for working with MySQL databases.
It also offers more advanced features than **MySQLdb**, such as connection pooling and transaction management, making it a good choice for larger and more complex projects.
