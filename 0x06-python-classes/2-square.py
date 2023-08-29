#!/usr/bin/python3

"""
A class Square that defines a square by: private instance attribute: size"""


class Square:

    """defining the square and initializing size
    to 0 """

    def __init__(self, size=0):
        """ raiseing a TypeError if size is not an integer"""

        if not isinstance(size, int):
            raise TypeError("size must be integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = int(size)