#!/usr/bin/python3
if __name__ = "__main__":
    import sys
    count = len(sys.argv) - 1
    # When no arguments are passed
    if count == 0:
        print("{} arguments.".format(count))
    # when 1 argument is passed
    elif counter == 1:
        print("{} argument:".format(count))
    # When more arguments
    else:
        print("{} arguments:".format(count))
    # This will display the number of args
    if count >= 1:
        count = 0
        for arg in sys.argv:
            if != 0:
                print("{}: {}".format(count, arg))
            count += 1
