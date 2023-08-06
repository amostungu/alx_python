#!/usr/bin/python3
"""Defines a class Rectangle that inherits from BaseGeometry."""


class baseGeo(type):
    """The custom metaclass"""
    def __dir__(cls):
        """Overrides dir() method for the metaclass"""
        return [attribute for attribute in super().__dir__() if attribute != '__init_subclass__']

class BaseGeometry:
    """BaseGeometry class"""
    def area(self):
        raise Exception("area() is not implemented")


class Rectangle(BaseGeometry):
    """Rectangle inheritance"""
    def __init__(self, width, height):
        self.__width = 0
        self.__height = 0
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def integer_validator(self, name, value):
        if not isinstance(value, int) or value <= 0:
            raise ValueError(f"{name} must be a positive integer.")
    def __dir__(cls):
        """Overrides dir() method for the metaclass"""
        return [attribute for attribute in super().__dir__() if attribute != 'init_subclass']
