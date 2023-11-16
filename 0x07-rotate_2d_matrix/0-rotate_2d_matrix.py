#!/usr/bin/python3
"""
Rotate a 2D matrix 90° clockwise
"""

def rotate_2d_matrix(matrix):
    """
    Rotates a 2D matrix 90° clockwise.

    Args:
    - matrix (list of lists): The input 2D matrix to be rotated.

    Returns:
    - None
    """

    # Initialize pointers for the outermost layer of the matrix
    left, right = 0, len(matrix) - 1

    # Continue rotating layers until left pointer surpasses right pointer
    while left < right:
        # Iterate through elements in the current layer
        for i in range(right - left):
            # Define indices for the four corners of the current layer
            top, bottom = left, right

            # Save the top left value
            topLeft = matrix[top][left + i]

            # Move bottom left to top left
            matrix[top][left + i] = matrix[bottom - i][left]

            # Move bottom right to bottom left
            matrix[bottom - i][left] = matrix[bottom][right - i]

            # Move top right to bottom right
            matrix[bottom][right - i] = matrix[top + i][right]

            # Move top left to top right
            matrix[top + i][right] = topLeft

        # Adjust pointers to move to the next layer
        right -= 1
        left += 1

# Example usage:
# matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# rotate_2d_matrix(matrix)
# print(matrix)

