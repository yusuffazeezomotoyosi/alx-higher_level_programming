#!/usr/bin/python3
# 6-print_comb3.py
# Loop through tens digits (0 to 8)
for tens_digit in range(9):
    # Loop through units digits (tens_digit + 1 to 9)
    for units_digit in range(tens_digit + 1, 10):
        print(f"{tens_digit}{units_digit}", end=", ")

# Print the last combination with a newline
print("89")
