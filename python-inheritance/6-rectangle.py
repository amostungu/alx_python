#!/usr/bin/python3
"""Defines a base geometry class BaseGeometry."""

class baseGeo(type):
    """The custom metaclass"""
    def __dir__(cls):
        """Overrides dir() method for the metaclass"""
        return [attribute for attribute in super().__dir__() if attribute != '__init_subclass__']

class BaseGeometry:
    """Reprsent base geometry."""

    def area(self):
        """Not yet implemented."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validate a parameter as an integer.

        Args:
            name (str): The name of the parameter.
            value (int): The parameter to validate.
        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is <= 0.
        """
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be positive integer".format(name))

    def __dir__(cls):
        """Overrides dir() method for the metaclass"""
        return [attribute for attribute in super().__dir__() if attribute != '__init_subclass__']
class Rectangle(BaseGeometry, metaclass = baseGeo):
    """class rectangle inheriting from BaseGeometry"""

    def __init__(self, width, height):
        """initializing width and height of rectangle"""
         self.__width = super().integer_validator("width", width)
         self.__height = super().integer_validator("height", height)
