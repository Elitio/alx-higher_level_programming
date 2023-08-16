#!/usr/bin/python3

"""
A function that returns a set of all elements present in only one set
"""


def only_diff_elements(set_1, set_2):
    all_members = set_1.symmetric_difference(set_2)
    return (all_members)
