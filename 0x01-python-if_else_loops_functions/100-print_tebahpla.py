#!/usr/bin/python3

for i in range(ord('z'), ord('a') - 1, -1):
    if i % 2 != 0:
        i -= ord('A') - ord('a')
    print(chr(i), end='')
