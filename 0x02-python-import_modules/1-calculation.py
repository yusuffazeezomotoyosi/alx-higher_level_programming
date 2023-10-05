#!/usr/bin/python3
#no 1

if __name__ == "__main__":
    """Print the sum, difference, multiple and quotient of 10 and 5."""
    from calculator_1 import add, sub, div, mul

    # Define the values 'a' and 'b'
    a = 10
    b = 5

    # Perform mathematical operations and print results
    sum_result = add(a, b)
    print("{} + {} = {}".format(a, b, sum_result))
    
    difference_result = sub(a, b)
    print("{} - {} = {}".format(a, b, difference_result))
    
    product_result = mul(a, b)
    print("{} * {} = {}".format(a, b, product_result))
    
    quotient_result = div(a, b)
    print("{} / {} = {}".format(a, b, quotient_result))
