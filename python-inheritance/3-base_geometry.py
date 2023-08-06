#!/usr/bin/python3
"""Defines an empty class BaseGeometry."""
class baseGeo(type):
    """The type class"""
    def __dir__(cls):
        """inharitance from type class"""
        return [attribute for attribute in super().__dir__() if attribute != '__init_subclass__']

class BaseGeometry:
    """basegeometry class"""
    def __dir__(cls):
        """class inheritance from type"""
        return [attribute for attribute in super().__dir__() if attribute !='__init_subclass__']
    pass
