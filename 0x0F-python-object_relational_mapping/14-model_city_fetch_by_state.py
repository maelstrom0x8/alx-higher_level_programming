#!/usr/bin/python3

"""
This script fetches all cities with their state names from the database.

Usage:
    ./14-city_fetch_by_state.py <username> <password> <database>

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
    from model_city import City

    user, password, db = sys.argv[1:]
    conn_url = f"mysql+mysqldb://{user}:{password}@127.0.0.1:{3306}/{db}"

    engine = create_engine(conn_url, pool_pre_ping=True)
    Base.metadata.create_all(engine)
    session = Session(engine)

    result_set = session.query(State.name, City.id, City.name).join(
        State, State.id == City.state_id).all()
    [print(f"{e[0]}: ({e[1]}) {e[2]}") for e in result_set]

    session.close()
