#!/usr/bin/python3

def add_tuple(tuple_a=(), tuple_b=()):
    """
    Add two tuples element-wise.

    Args:
        tuple_a (tuple, optional): The first tuple (default is an empty tuple).
        tuple_b (tuple, optional): The second tuple (default is an empty tuple).

    Returns:
        tuple: A new tuple with the element-wise sum of tuple_a and tuple_b.
    """
    tuple_a += (0, 0)
    tuple_b += (0, 0)
    return (tuple_a[0] + tuple_b[0], tuple_a[1] + tuple_b[1])
