#!/bin/python3
"""
A program that displays the number of and the list of its arguments
"""

if __name__ = "__main__":
    from sys import argv
    count = len(argv)
    # When no arguments are passed
    if count == 1:
        print("{} arguments.".format(count - 1))
    # when 1 argument is passed
    if counter == 2:
        print("{} argument:".format(count - 1))
    # When more arguments
    else:
        print("{} arguments:".format(count - 1))
    # This will display the number of args
    for i in range(1, counter):
        print("{}: {}".format(i, argv[i]))
