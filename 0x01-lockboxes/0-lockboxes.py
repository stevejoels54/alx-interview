#!/usr/bin/python3
"""Lockboxes problem solution in python"""


def canUnlockAll(boxes):
    """Checks if all the boxes can be opened"""
    new_keys = [0]
    unlocked_boxes = {0}

    while new_keys:
        current_box = new_keys.pop()
        for key in boxes[current_box]:
            if key not in unlocked_boxes and key < len(boxes):
                unlocked_boxes.add(key)
                new_keys.append(key)

    return len(unlocked_boxes) == len(boxes)
