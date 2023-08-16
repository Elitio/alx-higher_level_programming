#!/usr/bin/python3
"""
Write a function that returns a set
of common elements in two sets.

Prototype: def common_elements(set_1, set_2):
You are not allowed to import any module
"""


def common_elements(set_1, set_2):
    new_set = []

    for i in set_1:
        for j in set_2:
            if i == j:
                new_set.append(i)
    return (new_set)
