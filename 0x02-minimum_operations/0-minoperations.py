#!/usr/bin/python3
"""Minimum Operations"""


def minOperations(n):
    """Calculates the fewest number of operations needed
        to result in exactly n H characters in the file"""

    ops = 0  # Number of operations
    clipboard = 1  # Initial clipboard

    while clipboard < n:
        if n % clipboard == 0:
            clipboard += clipboard
            ops += 2
        else:
            clipboard += clipboard
            ops += 1

    return ops
