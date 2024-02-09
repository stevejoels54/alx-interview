#!/usr/bin/python3
"""N Queens"""
import sys


def isSafe(board, row, col, n):
    """Check if a queen can be placed on board[row][col]"""
    for i in range(col):
        if board[row][i]:
            return False
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j]:
            return False
    for i, j in zip(range(row, n, 1), range(col, -1, -1)):
        if board[i][j]:
            return False
    return True


def solveNqUtil(board, col, n):
    """Use backtracking to solve the N Queen problem"""
    if col == n:
        pos = []
        for i in range(n):
            for j in range(n):
                if board[i][j] == 1:
                    pos.append([i, j])
        print(pos)
        return True
    res = False
    for i in range(n):
        if isSafe(board, i, col, n):
            board[i][col] = 1
            res = solveNqUtil(board, col + 1, n) or res
            board[i][col] = 0
    return res


def nqueens(n):
    """Solve the N Queen problem"""
    if n < 4:
        print("N must be at least 4")
        sys.exit(1)
    board = [[0 for i in range(n)] for j in range(n)]
    solveNqUtil(board, 0, n)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    if not sys.argv[1].isdigit():
        print("N must be a number")
        sys.exit(1)
    n = int(sys.argv[1])
    nqueens(n)
