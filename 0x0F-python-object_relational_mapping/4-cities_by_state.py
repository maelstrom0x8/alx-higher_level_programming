#!/usr/bin/python3

"""
A script that connects to a MySQL database and retrieves information about
cities and their corresponding states.

Usage:
    ./4-cities_by_state.py <username> <password> <database_name>

Arguments:
    <username>: The MySQL database username.
    <password>: The MySQL database password.
    <database_name>: The name of the MySQL database to connect to.

Note:
    This script assumes that the 'cities' and 'states' tables are present in
    the specified database.
    It retrieves information about cities and their corresponding states
    through a SQL query.
"""


if __name__ == "__main__":

    import sys
    from MySQLdb import connect

    user, password, db = sys.argv[1:]
    host = '127.0.0.1'
    port = 3306
    conn = connect(host=host, port=port,
                   user=user, passwd=password, db=db, charset="utf8")

    cur = conn.cursor()

    cur.execute("""SELECT c.id, c.name, s.name
                FROM states s
                INNER JOIN cities c
                ON c.state_id = s.id
                ORDER BY c.id ASC""")
    result_set = cur.fetchall()

    [print(x) for x in result_set]

    cur.close()
    conn.close()
