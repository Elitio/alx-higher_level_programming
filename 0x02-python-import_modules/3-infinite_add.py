#!/usr/bin/python3
"""
A program thats displays the sum of all argv[]
"""
if __name == "__main__":
    from sys import argv
    sum = 0
    for i in argv:
        if i != argv[0]:
            sum += int(i)
    print("{}".format(sum))
