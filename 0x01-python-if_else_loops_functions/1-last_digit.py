#!/usr/bin/python3
import random

number = random.randint(-10, 10)

if number > 0:
    state = "positive"
elif number == 0:
    state = "zero"
else:
    state = "negative"

print(f"{number} is {state}")
