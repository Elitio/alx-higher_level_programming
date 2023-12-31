#!/usr/bin/python3

"""
Write a function that returns a new dictionary with all values multiplied by 2

Prototype: def multiply_by_2(a_dictionary):
You can assume that all values are only integers
Returns a new dictionary
You are not allowed to import any module
"""


def multiply_by_2(a_dictionary):
    new_dict = a_dictionary.copy()
    for key, value in new_dict.items():
        new_dict[key] = value * 2
    return (new_dict)
