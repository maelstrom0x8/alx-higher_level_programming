#!/usr/bin/python3

"""
This script fetches all states containing the letter 'a' from the database
and prints their id and name.

Usage:
    ./9-model_state_filter.py <username> <password> <database>

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
    conn_url = f"mysql+mysqldb://{user}:{password}@localhost:{3306}/{db}"

    engine = create_engine(conn_url, pool_pre_ping=True)
    Base.metadata.create_all(engine)
    session = Session(engine)
    result_set = session.query(State).filter(
        State.name.like("%a%")).order_by(State.id).all()
    if len(result_set) == 0:
        print('Nothing')
    else:
        for state in result_set:
            print("{}: {}".format(state.id, state.name))
    session.close()
