#!/usr/bin/python3

""" 12-pascal_triangle module """


def pascal_triangle(n):
    """returns a list of lists of integers representing the Pascal’s triangle
    Args:
        n (int): size of the triangle
    Return: The triangle
    """
    if n <= 0:
        return []
    elif n == 1:
        return [[1]]
    elif n == 2:
        return [[1], [1, 1]]

    triangle = [[1], [1, 1]]  # first two rows of triangle list
    idx = 1
    
    # loop n - 1 times to get triangle size 
    while len(triangle) < n:
        i = 0
        temp_list = [1]  # creates a new row to add computed elements
        # Add rows and columns up to the size of n
        while i < len(triangle[idx]) - 1:
            temp_list.append(triangle[idx][i] + triangle[idx][i+1])
            i += 1
        temp_list.append(1)
        triangle.append(temp_list)
        idx += 1

    return triangle
