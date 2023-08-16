#!/usr/bin/python3

"""
Write a function that replaces all occurrences of an element by another in a new list.

Prototype: def search_replace(my_list, search, replace):
my_list is the initial list
search is the element to replace in the list
replace is the new element
You are not allowed to import any module
"""


def search_replace(my_list, search, replace):
    new_list = my_list.copy()
    for item in range(len(new_list)):
        if new_list[item] == search:
            new_list[item] = search
    return (new_list)
