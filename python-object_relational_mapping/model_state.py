#!/usr/bin/python3
"""Inherits from SQLAlchemy Base and links to the MySQL table cities."""
"""Defines a City model."""

from sqlalchemy import Column, ForeignKey, Integer, String
"""Importing Column, foreignkey, Integr and String"""
from sqlalchemy.ext.declarative import declarative_base
"""importing declarative base"""

Base = declarative_base()
"""declative base"""


class City(Base):
    """Represents a city for a MySQL database.
    Attributes:
        id (str): The state's id.
        name (sqlalchemy.Integer): The state's name.
    """
    __tablename__ = "states"
    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
