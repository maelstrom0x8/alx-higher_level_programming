#!/usr/bin/python3

"""
A script that connects to a MySQL database and retrieves the names of
cities in a specified state.

Usage:
    ./5-filter_cities.py <username> <password> <database_name> <state_name>

Arguments:
    <username>: The MySQL database username.
    <password>: The MySQL database password.
    <database_name>: The name of the MySQL database to connect to.
    <state_name>: The name of the state for which city names are to be
    retrieved.

Note:
    This script assumes that the 'cities' and 'states' tables are present in
    the specified database.
    It retrieves the names of cities in the specified state through a SQL query
    and prints them to the console.

"""


if __name__ == "__main__":

    import sys
    from MySQLdb import connect

    user, password, db, city = sys.argv[1:]
    host = '127.0.0.1'
    port = 3306
    conn = connect(host=host, port=port,
                   user=user, passwd=password, db=db, charset="utf8")

    cur = conn.cursor()
    cur.execute("""SELECT c.name
                FROM states s INNER JOIN cities c
                ON c.state_id = s.id
                WHERE s.name = '%s'
                ORDER BY c.id ASC""" % city)

    query_rows = cur.fetchall()
    print(', '.join([x[0] for x in query_rows]))
    cur.close()
    conn.close()
