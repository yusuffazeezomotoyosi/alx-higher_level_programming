#!/usr/bin/python3

def remove_char_at(input_str, n):
    str_copy = ""

    if n < 0 or n >= len(input_str):
        str_copy = input_str
        return str_copy

    for i in range(n):
        str_copy += input_str[i]

    for i in range(n + 1, len(input_str)):
        str_copy += input_str[i]

    return str_copy
