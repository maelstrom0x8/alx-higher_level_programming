#!/usr/bin/python3

"""
101-relationship_states_cities_list.py

Script to demonstrate the use of SQLAlchemy for defining and querying
relationships
between State and City entities in a relational database.

Usage:
    python 101-relationship_states_cities_list.py <db_user> <db_password>
    <db_name>

Example:
    To list states and their associated cities:

    $ python 101-relationship_states_cities_list.py db_user db_password
    my_database
"""

import sys
from relationship_state import Base, State
from relationship_city import City
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import relationship


if __name__ == "__main__":
    user, password, db = sys.argv[1:]
    conn_url = f"mysql+mysqldb://{user}:{password}@localhost:{3306}/{db}"

    engine = create_engine(conn_url, pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    for row in session.query(State).order_by(State.id):
        print(row.id, row.name, sep=": ")
        for city in row.cities:
            print("    ", end="")
            print(city.id, city.name, sep=": ")
