#!/usr/bin/python3
"""
This script checks if a list of integers represents a valid UTF-8 encoding.
"""


def validUTF8(data):
    """
    Checks whether the given data is a valid UTF-8 encoding.

    Args:
    data (list): A list of integers representing the data to be validated.

    Returns:
    bool: True if the data is a valid UTF-8 encoding, else returns False.
    """
    # Initialize byte_count to keep track of the expected number of bytes in the current UTF-8 character
    byte_count = 0

    # Iterate through the data list
    for i in data:
        # If byte_count is 0, determine the number of bytes in the current UTF-8 character
        if byte_count == 0:
            if i >> 5 == 0b110 or i >> 5 == 0b1110:
                byte_count = 1
            elif i >> 4 == 0b1110:
                byte_count = 2
            elif i >> 3 == 0b11110:
                byte_count = 3
            elif i >> 7 == 0b1:
                return False
        else:
            # If byte_count is not 0, check if the current integer is following the UTF-8 encoding format
            if i >> 6 != 0b10:
                return False
            byte_count -= 1

    # If all integers have been processed and byte_count is 0, return True, indicating a valid UTF-8 encoding
    return byte_count == 0

