#!/usr/bin/python3
"""Defines a base geometry class BaseGeometry."""


BaseGeometry = import('5-base_geometry.py').BaseGeometry
"""importing"""

class Rectangle(BaseGeometry):
    """Rectangle inheritance"""

    def __init__(self, width, height):
        """initialization"""
        self.__width = super().integer_validator("width", width)
        self.__height = super().integer_validator("height", height)
