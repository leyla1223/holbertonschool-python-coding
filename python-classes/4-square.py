#!/usr/bin/python3
"""This module defines a Square class with size, area, and print functionality.
"""


class Square:
    """Defines a square with size validation, area calculation, and printing.
    """

    def __init__(self, size=0):
        """Initialize a Square instance with optional size (default is 0)."""
        self.size = size  # Use setter for validation

    @property
    def size(self):
        """Retrieve the size of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Return the current square area."""
        return self.__size ** 2

    def my_print(self):
        """Print the square using the '#' character.

        If size is 0, prints an empty line.
        """
        if self.__size == 0:
            print("")
            return
        for _ in range(self.__size):
            print("#" * self.__size)
