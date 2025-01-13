#!/usr/bin/python3
"""
This script calculates the factorial of a number provided as a command-line argument.
"""
import sys

def factorial(n):
    """
    Calculate the factorial of a number recursively.

    Parameters:
    n (int): The number to calculate the factorial of.

    Returns:
    int: The factorial of the number.
    """
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

f = factorial(int(sys.argv[1]))
print(f)