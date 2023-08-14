#!/usr/bin/python3

"""
A function that deletes the item at a specific position in a list
"""


def delete_at(my_list=[], idx=0):
    if idx < 0 or idx > len(my_list) - 1:
        return (my_list)
    else:
        new_list = my_list[:idx] + my_list[(idx + 1):]
        my_list = new_list
        return (my_list)
