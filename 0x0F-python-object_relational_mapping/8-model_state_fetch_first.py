#!/usr/bin/python3

"""
This script fetches the first state from the database and prints its id and
name.

Usage:
    ./8-model_state_fetch_first.py <username> <password> <database>

Arguments:
    username (str): The username to connect to the MySQL database.
    password (str): The password to connect to the MySQL database.
    database (str): The name of the database to connect to.

"""


if __name__ == '__main__':

    import sys
    from sqlalchemy import create_engine
    from sqlalchemy.orm import Session
    from model_state import Base, State

    user, password, db = sys.argv[1:]
    conn_url = f"mysql+mysqldb://{user}:{password}@127.0.0.1:{3306}/{db}"

    engine = create_engine(conn_url, pool_pre_ping=True)
    Base.metadata.create_all(engine)
    session = Session(engine)
    result_set = session.query(State).order_by(State.id).limit(1)
    if result_set.count() == 0:
        print('Nothing')
    else:
        for state in result_set:
            print("{}: {}".format(state.id, state.name))
    session.close()
