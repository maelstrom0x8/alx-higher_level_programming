#!/usr/bin/python3

"""
102-relationship_cities_states_list.py

Script to demonstrate the use of SQLAlchemy for defining and querying
relationships
between City and State entities in a relational database.

Usage:
    python 102-relationship_cities_states_list.py <db_user> <db_password>
    <db_name>

Example:
    To list cities and their associated states:

    $ python 102-relationship_cities_states_list.py db_user db_password
    my_database
"""

import sys
from relationship_state import Base, State
from relationship_city import City
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import relationship


if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]))
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    for res in session.query(State).order_by(State.id):
        for c in res.cities:
            print(c.id, c.name, sep=": ", end="")
            print(" -> " + res.name)
