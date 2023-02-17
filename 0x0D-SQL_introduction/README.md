<img src="https://github.com/ajipelumi/alx-higher_level_programming/blob/837cd36f602db17103df2e641351d12978b1090a/images/images.png" alt="SQL Logo" width="200">
Image Credit: Stonebranch

##

**SQL** is a standard language for accessing and manipulating databases.

- SQL stands for **Structured Query Language**.
- SQL lets you access and manipulate databases.
- SQL became a standard of the **American National Standards Institute (ANSI)** in 1986, and of the **International Organization for Standardization (ISO)** in 1987.

### What Can SQL do?
- SQL can execute queries against a database.
- SQL can retrieve data from a database.
- SQL can insert records in a database.
- SQL can update records in a database.
- SQL can delete records from a database.
- SQL can create new databases.
- SQL can create new tables in a database.
- SQL can create stored procedures in a database.
- SQL can create views in a database.
- SQL can set permissions on tables, procedures, and views.

**MySQL** is an open-source database management system that implements the relational model and uses **SQL** to manage its data.

```sql
$ service mysql start                                                   
 * Starting MySQL database server mysqld 
$
$ cat 0-list_databases.sql | mysql -uroot -p                               
Database                                                                                   
information_schema                                                                         
mysql                                                                                      
performance_schema                                                                         
sys                      
$
```

This README describes what each script is doing:

The file `0-list_databases.sql` is a script that lists all databases of our MySQL server.

The file `1-create_database_if_missing.sql` is a script that creates the database hbtn_0c_0 in our MySQL server.

The file `2-remove_database.sql` is a script that deletes the database hbtn_0c_0 in our MySQL server.

The file `3-list_tables.sql` is a script that lists all the tables of a database in our MySQL server.

The file `4-first_table.sql` is a script that creates a table called `first_table` in the current database in our MySQL server.

The file `5-full_table.sql` is a script that prints the full description of the table `first_table` from the database `hbtn_0c_0` in our MySQL server.

The file `6-list_values.sql` is a script that lists all rows of the table `first_table` from the database `hbtn_0c_0` in our MySQL server.

The file `7-insert_value.sql` is a script that inserts a new row in the table `first_table` (database `hbtn_0c_0`) in our MySQL server.

The file `8-count_89.sql` is a script that displays the number of records with `id = 89` in the table `first_table` of the database `hbtn_0c_0` in our MySQL server.

The file `9-full_creation.sql` is a script that creates a table `second_table` in the database `hbtn_0c_0` in our MySQL server and add multiples rows.

The file `10-top_score.sql` is a script that lists all records of the table `second_table` of the database `hbtn_0c_0` in our MySQL server.

The file `11-best_score.sql` is a script that lists all records with a `score >= 10` in the table `second_table` of the database `hbtn_0c_0` in our MySQL server.

The file `12-no_cheating.sql` is a script that updates the score of Bob to `10` in the table `second_table`.

The file `13-change_class.sql` is a script that removes all records with a `score <= 5` in the table `second_table` of the database `hbtn_0c_0` in our MySQL server.

The file `14-average.sql` is a script that computes the score average of all records in the table `second_table` of the database `hbtn_0c_0` in our MySQL server.

The file `15-groups.sql` is a script that lists the number of records with the same score in the table `second_table` of the database `hbtn_0c_0` in our MySQL server.

The file `16-no_link.sql` is a script that lists all records of the table `second_table` of the database `hbtn_0c_0` in our MySQL server.

The file `100-move_to_utf8.sql` is a script that converts `hbtn_0c_0` database to UTF8 (`utf8mb4`, collate `utf8mb4_unicode_ci`) in our MySQL server.

The file `101-avg_temperatures.sql` is a script that displays the average temperature (Fahrenheit) by city ordered by temperature (descending).

The file `102-top_city.sql` is a script that displays the top 3 of cities temperature during July and August ordered by temperature (descending).

The file `103-max_state.sql` is a script that displays the max temperature of each state (ordered by State name).
