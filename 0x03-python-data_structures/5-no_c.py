#!/usr/bin/python3

def no_c(my_string):
    removed_char = "c C"
    new_string = ""
    for char in my_string:
        if char not in removed_char:
            new_string += char
    return (new_string)

