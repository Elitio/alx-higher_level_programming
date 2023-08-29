#!/usr/bin/python3

"""
A class Square that defines a square by: private instance attribute: size"""


class Square:

    """defining the square and initializing size
    to 0 """

    def __init__(self, size=0):

        """ raiseing a TypeError if size is not an integer"""
        if type(size) is not int:
            raise TypeError("size must be integer")
        """ Now raise a ValueError when size is less than 0"""
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
