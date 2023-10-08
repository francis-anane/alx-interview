#!/usr/bin/python3
"""Lockboxes interview prep function"""


def canUnlockAll(boxes):
    num_boxes = len(boxes)
    visited = [False] * num_boxes  # Initialize a list to track visited boxes
    visited[0] = True  # The first box is initially visited and unlocked
    stack = [0]  # Start with the first box in the stack

    while stack:
        current_box = stack.pop()
        for key in boxes[current_box]:
            if 0 <= key < num_boxes and not visited[key]:
                visited[key] = True  # Mark the box as visited
                stack.append(key)  # Add the newly unlocked box to the stack

    # Check if all boxes have been visited and unlocked
    return all(visited)
