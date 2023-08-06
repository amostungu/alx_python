#!/usr/bin/python3
"""Defines a base geometry class BaseGeometry."""


BaseGeometry = __import__('5-base_geometry.py').BaseGeometry
"""importing"""

class Rectangle(BaseGeometry):
    """Rectangle inheritance"""

    def __init__(self, width, height):
        """initialization"""
        self.__width = 0
        self.__height = 0
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def integer_validator(self, name, value):
        """integrator validator"""
        if not isinstance(value, int) or value <= 0:
            raise ValueError(f"{name} must be a positive integer.")
