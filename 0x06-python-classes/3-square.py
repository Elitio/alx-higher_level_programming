#!/usr/bin/python3
"""
Write a class Square that defines a square by: (based on 2-square.py)

Private instance attribute: size
"""


class Square:
    """ A class that defines a square by its size
    """
    def __init__(self, size=0):
        """Instantiation with optional size=0"""
        if type(size) != int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """"Square area and returns the area"""
        return self.__size ** 2
