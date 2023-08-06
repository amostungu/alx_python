#!/usr/bin/python3
"""Defines a base geometry class BaseGeometry."""


BaseGeometry = __import__('5-base_geometry.py').BaseGeometry
"""importing"""

class Rectangle(BaseGeometry):
    """Rectangle inheritance"""

    def __init__(self, width, height):
        """initialization"""

        self.__width = super().integer_validator("width", width)
        self.__height = super().integer_validator("height", height)

    def integer_validator(self, name, value):
        """integrator validator"""
        if not isinstance(value, int) or value <= 0:
            raise ValueError(f"{name} must be a positive integer.")
