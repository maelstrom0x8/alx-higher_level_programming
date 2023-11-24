#!/usr/bin/python3

"""
A script that connects to a MySQL database and safely selects states
based on a provided name.

Usage:
    ./3-my_safe_filter_states.py <username> <password> <database_name>
    <state_name>

Arguments:
    <username>: The MySQL database username.
    <password>: The MySQL database password.
    <database_name>: The name of the MySQL database to connect to.
    <state_name>: The name of the state to filter by.

Note:
    This script assumes that the 'states' table is present in the specified
    database.
    It ensures a safer query by removing potential SQL injection characters
    from the input.
"""


if __name__ == "__main__":

    import sys
    from MySQLdb import connect

    user, password, db, name = sys.argv[1:]
    name = name.split(';')[0].replace("'", "")
    host = 'localhost'
    port = 3306
    conn = connect(host=host, port=port,
                   user=user, passwd=password, db=db, charset="utf8")

    cur = conn.cursor()

    cur.execute("SELECT * FROM states WHERE name = '%s' ORDER BY id ASC"
                % (name))
    result_set = cur.fetchall()

    [print(x) for x in result_set]

    cur.close()
    conn.close()
