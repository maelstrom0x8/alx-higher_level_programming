#!/usr/bin/python3

"""
This module defines the State class, which is mapped to the 'states'
table in a database.

Attributes:
    id (int): The primary key of the 'states' table.
    name (str): The name of the state.

Classes:
    State: A class representing a state with attributes id and name.

"""


from sqlalchemy import String, Column, Integer
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    """
    Represents a state.

    Attributes:
        id (int): The primary key of the 'states' table.
        name (str): The name of the state.

    """
    __tablename__ = "states"

    id = Column(Integer(), primary_key=True,
                autoincrement=True, nullable=False)
    name = Column(String(128), nullable=False, unique=True)

    def __init__(self, name) -> None:
        super().__init__()
        self.name = name
