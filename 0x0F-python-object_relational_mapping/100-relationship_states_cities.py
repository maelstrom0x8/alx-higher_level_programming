#!/usr/bin/python3

"""
100-relationship_states_cities.py

Script to demonstrate the use of SQLAlchemy for defining and establishing a
relationship
between State and City entities in a relational database.

Usage:
    python 100-relationship_states_cities.py <db_user> <db_password> <db_name>

Example:
    To create a State and City with a one-to-many relationship:

    $ python 100-relationship_states_cities.py db_user db_password my_database
"""

import sys

from relationship_state import Base, State
from relationship_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == '__main__':

    user, password, db = sys.argv[1:]
    conn_url = f"mysql+mysqldb://{user}:{password}@localhost:{3306}/{db}"

    engine = create_engine(conn_url, pool_pre_ping=True)
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    state = State(name='California')
    city = City(name='San Francisco')
    state.cities.append(city)

    session.add(state)
    session.add(city)
    session.commit()
    session.close()
