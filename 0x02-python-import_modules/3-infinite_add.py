#!/usr/bin/python3
# 3-infinite_add.py
# Brennan D Baraban <375@holbertonschool.com>

if __name__ == "__main__":
    """
    Print the addition of all arguments.
    """
    import sys

    # Use list slicing to exclude the script name from arguments
    arguments = sys.argv[1:]

    # Use a list comprehension to convert and sum the arguments as integers
    total = sum([int(arg) for arg in arguments])

    # Print the result
    print(total)
