#!/usr/bin/python3

"""
A script that connects to a MySQL database and selects states whose names
start with the letter 'N'.

Usage:
    ./1-filter_states.py <username> <password> <database_name>

Arguments:
    <username>: The MySQL database username.
    <password>: The MySQL database password.
    <database_name>: The name of the MySQL database to connect to.

Note:
    This script assumes that the 'states' table is present in the specified
    database.

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
    cur.execute("""SELECT * FROM states
                WHERE SUBSTRING(name,1,1) = 'N'
                ORDER BY id ASC""")

    result_set = cur.fetchall()

    [print(x) for x in result_set]

    cur.close()
    conn.close()
