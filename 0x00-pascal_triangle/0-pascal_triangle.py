#!/usr/bin/python3
"""
pascal's triangle
"""


def pascal_triangle(n):
    """
    func: pascal_triangle
        return pascal's triangle
    args:
        <int: n> : number of rows (> 0)
    return:
        <list <of list>>
    """
    if n < 0:
        return ([])
    row = []
    for x in range(n):
        row.append([])
        row[x].append(1)
        if (x > 0):
            for y in range(1, x):
                row[x].append(row[x - 1][y - 1] + row[x - 1][y])
            row[x].append(1)

    return (row)
