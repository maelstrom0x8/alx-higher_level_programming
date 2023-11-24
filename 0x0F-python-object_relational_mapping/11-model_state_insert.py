#!/usr/bin/python3

"""
This script inserts a new state into the database.

Usage:
    ./model_state_insert.py <username> <password> <database> <state_name>

Arguments:
    username (str): The username to connect to the MySQL database.
    password (str): The password to connect to the MySQL database.
    database (str): The name of the database to connect to.
    state_name (str): The name of the state to insert into the database.

"""

if __name__ == '__main__':
    import sys
    from sqlalchemy import create_engine
    from sqlalchemy.orm import Session
    from model_state import Base, State

    user, password, db, name = sys.argv[1:]
    conn_url = f"mysql+mysqldb://{user}:{password}@localhost:{3306}/{db}"

    engine = create_engine(conn_url, pool_pre_ping=True)
    Base.metadata.create_all(engine)
    session = Session(engine)

    state = State(name=name)
    session.add(state)
    session.commit()
    print(state.id)
    session.close()
