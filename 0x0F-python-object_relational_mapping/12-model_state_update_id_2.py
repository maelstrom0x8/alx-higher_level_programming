#!/usr/bin/python3

"""
This script updates the name of a state with ID 2 in the database.

Usage:
    ./12-model_state_update_id_2.py <username> <password> <database>

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

    _state = session.query(State).where(State.id == 2).first()
    _state.name = 'New Mexico'

    session.commit()
    session.close()
