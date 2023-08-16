#!/usr/bin/python3

"""
Write a function that returns a key with the biggest integer value.

Prototype: def best_score(a_dictionary):
You can assume that all values are only integers
If no score found, return None
You can assume all students have a different score
You are not allowed to import any module
"""


def best_score(a_dictionary):
    if a_dictionary is None:
        return (None)

    biggest_score = max(a_dictionary.values(), default=None)
    for key, value in a_dictionary.items():
        if value == biggest_score:
            return (key)
