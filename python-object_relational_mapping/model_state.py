#!/usr/bin/python3
"""Inherits from SQLAlchemy Base and links to the MySQL table cities."""
"""Defines a City model."""

from sqlalchemy import Column, ForeignKey, Integer, String
"""Importing Column, foreignkey, Integr and String"""
from sqlalchemy.ext.declarative import declarative_base
"""importing declarative base"""

Base = declarative_base()


class City(Base):
    """Represents a city for a MySQL database.
    Attributes:
        id (str): The city's id.
        name (sqlalchemy.Integer): The city's name.
        state_id (sqlalchemy.String): The city's state id.
    """
    __tablename__ = "cities"
    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey("states.id"), nullable=False)
