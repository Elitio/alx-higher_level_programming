#!/usr/bin/python3

"""
A function that adds 2 tuples
"""


def add_tuple(tuple_a=(), tuple_b=()):
    a_val = len(tuple_a)
    b_val = len(tuple_b)

    if a_val == 0:
        a_tup1 = 0
        a_tup2 = 0
    elif a_val == 1:
        a_tup1 = tuple_a[0]
        a_tup2 = 0
    else:
        a_tup1 = tuple_a[0]
        a_tup2 = tuple_a[1]
    if b_val == 0:
        b_tup1 = 0
        b_tup2 = 0
    elif b_val == 1:
        b_tup1 = tuple_b[0]
        b_tup2 = 0
    else:
        b_tup1 = tuple_b[0]
        b_tup2 = tuple_b[1]
    new_tuple = ((a_tup1 + b_tup1), (a_tup2 + b_tup2))
    return (new_tuple)
