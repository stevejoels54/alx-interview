#!/usr/bin/python3
"""UTF-8 Validation"""


def validUTF8(data):
    """
    Determines if a given data set represents a valid UTF-8 encoding.

    Args:
        data (list): List of integers representing 1-byte data.

    Returns:
        bool: True if data is a valid UTF-8 encoding, else False.
    """

    remaining_bytes = 0

    for num in data:
        if num & 0x80:
            if remaining_bytes == 0:
                if num & 0xE0 == 0xC0:
                    remaining_bytes = 1
                elif num & 0xF0 == 0xE0:
                    remaining_bytes = 2
                elif num & 0xF8 == 0xF0:
                    remaining_bytes = 3
                else:
                    return False
            else:
                remaining_bytes -= 1
        elif remaining_bytes > 0:
            return False

    return remaining_bytes == 0
