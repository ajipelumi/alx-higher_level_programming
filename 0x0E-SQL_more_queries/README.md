The `CREATE USER` statement creates one or more user accounts with no privileges. It means that the user accounts can log in to the `MySQL Server`, but cannot do anything such as selecting a database and querying data from tables.

To allow user accounts to work with database objects, we need to grant the user accounts privileges. And the `GRANT` statement grants a user account one or more privileges.

The following illustrates the basic syntax of the `GRANT` statement:

```sql
GRANT <privilege> <,privilege>,.. 
ON <privilege_level>
TO <username>@<host>;
```

### How to import a SQL dump

```sql
$ echo "CREATE DATABASE hbtn_0d_tvshows;" | mysql -uroot -p
Enter password: 
$ curl "https://s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/274/hbtn_0d_tvshows.sql" -s | mysql -uroot -p hbtn_0d_tvshows
Enter password: 
$ echo "SELECT * FROM tv_genres" | mysql -uroot -p hbtn_0d_tvshows
Enter password: 
id  name
1   Drama
2   Mystery
3   Adventure
4   Fantasy
5   Comedy
6   Crime
7   Suspense
8   Thriller
$
```

The project explores:
- Grant Permissions in **MySQL**.
- **MySQL** constraints.
- **MySQL** subqueries.
- Basic query operation: the join.
- Join types.
- Union and Minus.
- **SQL** Style Guide.

This README describes what each script is doing:

The file `0-privileges.sql` is a script that lists all privileges of the MySQL users `user_0d_1` and `user_0d_2` on our server (in `localhost`).

The file `1-create_user.sql` is a script that creates the MySQL server user `user_0d_1`.

The file `2-create_read_user.sql` is a script that creates the database `hbtn_0d_2` and the user `user_0d_2`.

The file `3-force_name.sql` is a script that creates the table `force_name` on our MySQL server.

The file `4-never_empty.sql` is a script that creates the table `id_not_null` on our MySQL server.

The file `5-unique_id.sql` is a script that creates the table `unique_id` on our MySQL server.

The file `6-states.sql` is a script that creates the database `hbtn_0d_usa` and the table `states` (in the database `hbtn_0d_usa`) on our MySQL server.

The file `7-cities.sql` is a script that creates the database `hbtn_0d_usa` and the table `cities` (in the database `hbtn_0d_usa`) on our MySQL server.

The file `8-cities_of_california_subquery.sql` is a script that lists all the cities of California that can be found in the database `hbtn_0d_usa`.

The file `9-cities_by_state_join.sql` is a script that lists all cities contained in the database `hbtn_0d_usa`.

The file `10-genre_id_by_show.sql` is a script that lists all shows contained in `hbtn_0d_tvshows` that have at least one genre linked.

The file `11-genre_id_all_shows.sql` is a script that lists all shows contained in the database `hbtn_0d_tvshows`.

The file `12-no_genre.sql` is a script that lists all shows contained in `hbtn_0d_tvshows` without a genre linked.

The file `13-count_shows_by_genre.sql` is a script that lists all genres from `hbtn_0d_tvshows` and displays the number of shows linked to each.

The file `14-my_genres.sql` is a script that uses the `hbtn_0d_tvshows` database to lists all genres of the show `Dexter`.

The file `15-comedy_only.sql` is a script that lists all Comedy shows in the database `hbtn_0d_tvshows`.

The file `16-shows_by_genre.sql` is a script that lists all shows, and all genres linked to that show, from the database `hbtn_0d_tvshows`.

The file `100-not_my_genres.sql` is a script that uses the `hbtn_0d_tvshows` database to list all genres not linked to the show `Dexter`.

The file `101-not_a_comedy.sql` is a script that lists all shows without the genre `Comedy` in the database `hbtn_0d_tvshows`.

The file `102-rating_shows.sql` is a script that lists all shows from `hbtn_0d_tvshows_rate` by their rating.

The file `103-rating_genres.sql` is a script that lists all genres in the database `hbtn_0d_tvshows_rate` by their rating.
