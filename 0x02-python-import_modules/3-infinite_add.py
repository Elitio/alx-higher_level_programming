#!/usr/bin/python3
"""
A program thats displays the sum of all argv[]
"""
if __name == "__main__":
    import sys
    sum = 0
    for i in sys.argv:
        if i != sys.argv[0]:
            sum += int(i)
    print(sum)
