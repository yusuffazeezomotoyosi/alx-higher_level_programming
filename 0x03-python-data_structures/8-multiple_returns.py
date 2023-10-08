#!/usr/bin/python3

def multiple_returns(sentence):
    total = len(sentence)
    char = sentence[0] if total > 0 else None  # Use None (without quotes) for a None value
    new = total, char
    return new  # Remove unnecessary parentheses
