#!/usr/bin/python3

"""
relationship_city.py

Module for defining the City class using SQLAlchemy for a relational database.

Classes:
    City: Represents a city entity with a many-to-one relationship to State
    entities.

Example:
    To create a City instance and establish a relationship with a State:

     from sqlalchemy import create_engine
     from sqlalchemy.orm import sessionmaker
     from relationship_state import State, Base
     from relationship_city import City

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

     print(new_city.state)
    <State(name='California')>
"""

from sqlalchemy import Column, Integer, String, ForeignKey
from relationship_state import Base


class City(Base):
    """
    City class representing a city entity in the relational database.

    Attributes:
        id (int): Primary key for the city.
        name (str): Name of the city.
        state_id (int): Foreign key referencing the associated State entity.

    Example:
        To create a new city and associate it with a state:

         new_city = City(name='San Francisco', state=new_state)
         print(new_city.name)
        'San Francisco'
    """

    __tablename__ = 'cities'
    id = Column(Integer, unique=True, nullable=False, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey("states.id"), nullable=False)
