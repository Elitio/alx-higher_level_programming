#!/usr/bin/python3

"""
A function that returns a tuple with the length
of a string and its first character
"""


def multiple_returns(sentence):
    if len(sentence) == 0:
        str_len = len(sentence)
        f_char = None
    else:
        str_len = len(sentence)
        f_char = sentence[0]
    return (str_len, f_char)
