#!/usr/bin/python3
# 7-islower.py
def islower(c):
    # Check if the Unicode code point is within the range of lowercase letters
    if 97 <= c <= 122:
        return True
    else:
        return False
