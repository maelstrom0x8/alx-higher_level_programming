#!/usr/bin/python3

"""
This script fetches the id of a state from the database based on its name.

Usage:
    ./10-model_state_my_get.py <username> <password> <database> <state_name>

Arguments:
    username (str): The username to connect to the MySQL database.
    password (str): The password to connect to the MySQL database.
    database (str): The name of the database to connect to.
    state_name (str): The name of the state to search for.

"""


if __name__ == '__main__':

    import sys
    from sqlalchemy import create_engine
    from sqlalchemy.orm import Session
    from model_state import Base, State

    user, password, db, state = sys.argv[1:]
    conn_url = f"mysql+mysqldb://{user}:{password}@127.0.0.1:{3306}/{db}"

    engine = create_engine(conn_url, pool_pre_ping=True)
    Base.metadata.create_all(engine)
    session = Session(engine)
    result_set = session.query(State).where(State.name == (state, )).first()
    if result_set is None:
        print('Not Found')
    else:
        print(result_set.id)
    session.close()
