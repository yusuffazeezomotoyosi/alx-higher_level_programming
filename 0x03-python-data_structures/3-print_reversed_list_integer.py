#!/usr/bin/python3

def print_reversed_list_integer(my_list):
    """
    Print integers from a list in reverse order.

    Args:
        my_list (list): The list of integers to be printed in reverse order.
    """
    for i in reversed(my_list):
        print("{:d}".format(i))
