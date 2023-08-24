#!/usr/bin/python3
"""Class definition of a City"""

from sqlalchemy import Column, Integer, String, ForeignKey
"""Importing Column, Integer, String and Foreignkey from sqlalchemy"""
from model_state import Base
"""Importing base from model state"""

class City(Base):
    """City class that inherits from Base"""

    __tablename__ = "cities"
    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
