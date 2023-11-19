#!/usr/bin/python3

"""
This module defines the City class, which is mapped to the 'cities' table in
a database.

Attributes:
    id (int): The primary key of the 'cities' table.
    name (str): The name of the city.
    state_id (int): The foreign key referencing the 'id' column of the
    'states' table.

Classes:
    City: A class representing a city with attributes id, name, and state_id.

"""


from sqlalchemy import Column, Integer, String, ForeignKey

from model_state import Base


class City(Base):
    """
    Represents a city.

    Attributes:
        id (int): The primary key of the 'cities' table.
        name (str): The name of the city.
        state_id (int): The foreign key referencing the 'id' column of the
        'states' table.
    """
    __tablename__ = 'cities'

    id = Column(Integer(), primary_key=True, unique=True,
                nullable=False, autoincrement=True)
    name = Column(String(128), nullable=False)
    state_id = Column(ForeignKey('states.id'), nullable=False)
