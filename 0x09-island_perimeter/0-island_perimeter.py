#!/usr/bin/python3
"""Island Perimeter"""

def island_perimeter(grid):
    """Returns the perimeter of the island described in grid."""
    counter = 0
    grid_max = len(grid) - 1  # Index of the last list in the grid
    lst_max = len(grid[0]) - 1  # Index of the last square in the list

    for lst_idx, lst in enumerate(grid):
        for land_idx, land in enumerate(lst):
            if land == 1:
                # Left and right
                if land_idx == 0:
                    # Left side
                    counter += 1

                    # Right side
                    if lst[land_idx + 1] == 0:
                        counter += 1
                elif land_idx == lst_max:
                    # Left side
                    if lst[land_idx - 1] == 0:
                        counter += 1

                    # Right side
                    counter += 1
                else:
                    # Left side
                    if lst[land_idx - 1] == 0:
                        counter += 1

                    # Right side
                    if lst[land_idx + 1] == 0:
                        counter += 1

                # Top and down
                if lst_idx == 0:
                    # Top side
                    counter += 1

                    # Bottom side
                    if grid[lst_idx + 1][land_idx] == 0:
                        counter += 1
                elif lst_idx == grid_max:
                    # Top side
                    if grid[lst_idx - 1][land_idx] == 0:
                        counter += 1

                    # Bottom side
                    counter += 1
                else:
                    # Top side
                    if grid[lst_idx - 1][land_idx] == 0:
                        counter += 1

                    # Bottom side
                    if grid[lst_idx + 1][land_idx] == 0:
                        counter += 1

    return counter

