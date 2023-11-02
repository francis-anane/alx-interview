#!/usr/bin/python3
"""N Queens Challenge module"""

import sys


if __name__ == '__main__':
    # Check if the correct number of arguments is provided
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        n = int(sys.argv[1])  # Convert the argument to an integer
    except ValueError:
        print('N must be a number')
        exit(1)

    if n < 4:  # Ensure that N is at least 4
        print('N must be at least 4')
        exit(1)

    solutions = []  # Store the solutions here
    placed_queens = []  # Coordinates format [row, column]
    stop = False  # Indicates when the loop should stop
    r = 0  # Row index
    c = 0  # Column index

    # Iterate through rows
    while r < n:
        goback = False
        # Iterate through columns
        while c < n:
            # Check if the current column is safe
            safe = True
            for cord in placed_queens:
                col = cord[1]
                if (col == c or col + (r - cord[0]) == c or
                        col - (r - cord[0]) == c):
                    safe = False
                    break

            if not safe:  # If the column is not safe, move to the next column
                if c == n - 1:
                    goback = True
                    break
                c += 1
                continue

            # Place queen at the current position
            cords = [r, c]
            placed_queens.append(cords)
            if r == n - 1:  # If it's the last row, save the solution
                solutions.append(placed_queens[:])
                for cord in placed_queens:
                    if cord[1] < n - 1:
                        r = cord[0]
                        c = cord[1]
                for i in range(n - r):
                    placed_queens.pop()
                if r == n - 1 and c == n - 1:
                    placed_queens = []
                    stop = True
                r -= 1
                c += 1
            else:
                c = 0
            break
        if stop:
            break
        # If it's not safe, go back to the previous row and continue
        # from the last safe column + 1
        if goback:
            r -= 1
            while r >= 0:
                c = placed_queens[r][1] + 1
                del placed_queens[r]  # Delete previous queen coordinates
                if c < n:
                    break
                r -= 1
            if r < 0:
                break
            continue
        r += 1

    # Print the solutions
    for idx, val in enumerate(solutions):
        if idx == len(solutions) - 1:
            print(val, end='')
        else:
            print(val)
