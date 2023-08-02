#!/usr/bin/python3
"""class baseGeometry"""


class BaseGeometry:
    def area(self):
        raise Exception("area() is not implemented")


class Rectangle(BaseGeometry):
    """rectangle inheritance"""

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

    def area(self):
        return self.__width * self.__height

    def __str__(self):
        return f"[Rectangle] {self.__width}/{self.__height}"


class Square(Rectangle):
    """square inheritance"""

    def __init__(self, size):
        self.__size = 0
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(self.__size, self.__size)

    def __str__(self):
        return f"[Square] {self.__size}/{self.__size}"
