#!/usr/bin/python3
"""Class definition of a City"""


from sqlalchemy import Column, Integer, String, ForeignKey
"""Importing Column, Integer, String and Foreignkey from sqlalchemy"""

from model_state import Base
"""Importing base from model state"""

class City(Base):
    """City class that inherits from Base"""

    __tablename__ = "cities"
    """Database table"""

    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    """An auto-incrementing primary key for the City table."""

    name = Column(String(128), nullable=False)
    """The name of the city, limited to 128 characters."""

    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)

    """A foreign key referencing the id column of the associated state."""
