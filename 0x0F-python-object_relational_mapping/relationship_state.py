#!/usr/bin/python3

"""
relationship_state.py

Module for defining the State class using SQLAlchemy for a relational database.

Classes:
    State: Represents a state entity with a one-to-many relationship to City
    entities.

Example:
    To create a State instance and establish a relationship with City:

     from sqlalchemy import create_engine
     from sqlalchemy.orm import sessionmaker
     from relationship_state import State, Base

     engine = create_engine('sqlite:///:memory:')
     Base.metadata.create_all(engine)

     Session = sessionmaker(bind=engine)
     session = Session()

     new_state = State(name='California')
     session.add(new_state)
     session.commit()

     new_city = City(name='Los Angeles', state=new_state)
     session.add(new_city)
     session.commit()

     print(new_state.cities)
    [<City(name='Los Angeles')>]
"""

from sqlalchemy import Column, Integer, String, MetaData
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

metadata = MetaData()
Base = declarative_base(metadata=metadata)


class State(Base):
    """
    State class representing a state entity in the relational database.

    Attributes:
        id (int): Primary key for the state.
        name (str): Name of the state.
        cities (relationship): One-to-many relationship with City entities.

    Example:
        To create a new state:

         new_state = State(name='New York')
         print(new_state.name)
        'New York'
    """

    __tablename__ = 'states'
    id = Column(Integer, unique=True, nullable=False, primary_key=True)
    name = Column(String(128), nullable=False)
    cities = relationship("City", backref="states")
