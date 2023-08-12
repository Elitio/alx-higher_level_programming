#!/usr/bin/python3
"""
A program thats displays the sum of all argv[]
"""
if __name == "__main__":
    from sys import argv
    sum = 0
    for i in argv[1:]:
        sum += int(i)
        print("{}".format(sum))
