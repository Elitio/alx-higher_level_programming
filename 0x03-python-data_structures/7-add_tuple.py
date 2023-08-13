#!/usr/bin/python3

"""
A function that adds 2 tuples
"""


def add_tuple(tuple_a=(), tuple_b=()):
    new_list = list(tuple_a) + list(tuple_b)
    new_tuple = tuple(new_list)
    return (int(new_tuple))
