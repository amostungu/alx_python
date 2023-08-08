#!/usr/bin/python3
"""Implementation of Rectangle class that inherit from Base"""


from models.base import Base
"""importing from Model.base"""

class Rectangle(Base):
    """
    Represents a rectangle.

    Attributes:
        id (int): The identifier of the rectangle.
        width (int): The width of the rectangle.
        height (int): The height of the rectangle.
        x (int): The x-coordinate of the rectangle's position.
        y (int): The y-coordinate of the rectangle's position.
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        """Initializes a new Rectangle instance."""
        super().__init__(id)
        self.__width = width
        self.__height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """
        Get the width of the rectangle.

        Returns:
            int: The width of the rectangle.
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Set the width of the rectangle.

        Args:
            value (int): The desired width value.

        Returns:
            None.
        """
        self.__width = value

    @property
    def height(self):
        """
        Get the height of the rectangle.

        Returns:
            int: The height of the rectangle.
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Set the height of the rectangle.

        Args:
            value (int): The desired height value.

        Returns:
            None.
        """
        self.__height = value
   
    @property
    def x(self):
        """
        Get the x-coordinate of the rectangle's position.

        Returns:
            int: The x-coordinate.
        """
        return self.__x

    @x.setter
    def x(self, value):
        """
        Set the x-coordinate of the rectangle's position.

        Args:
            value (int): The desired x-coordinate value.

        Returns:
            None.
        """
        self.__x = value
 
    @property
    def y(self):
        """
        Get the y-coordinate of the rectangle's position.

        Returns:
            int: The y-coordinate.
        """
        return self.__y

    @y.setter
    def y(self, value):
        """
        Set the y-coordinate of the rectangle's position.

        Args:
            value (int): The desired y-coordinate value.

        Returns:
            None.
        """
        self.__y = value
