import random as r
import numpy as np


class Chess: # Boolean class
    def __init__(self, b, r, c, m, n):
        self.board = b
        self.rows = r
        self.cols = c
        self.main_diags = m
        self.neg_diags = n

    def legal(self, i, j, h):
        if self.rows[0][i] == 1:
            return False
        if self.cols[0][j] == 1:
            return False
        if self.main_diags[h][abs(i - j)] == 1:
            return False
        if self.neg_diags[0][i + j] == 1:
            return False
        return True


def initialize(e, n):
    # Starts everything as False (0)
    e.board = np.zeros( (n, n), dtype = int )
    e.rows = np.zeros( (1, n), dtype = int )
    e.cols = np.zeros( (1, n), dtype = int )
    e.main_diags = np.zeros( (2, n), dtype = int )
    e.neg_diags = np.zeros( (1, 2*n + 1), dtype = int )


def place(e, i, j):
    # If (i, j) collides with another queen returns False
    # Otherwise places a queen at (i, j) and returns True
    h = int(j > i)
    if not e.legal(e, i, j, h):
        return False
    e.rows[0][i] += 1
    e.cols[0][j] += 1
    e.main_diags[h][abs(i - j)] += 1
    e.neg_diags[0][i + j] += 1
    e.board[i][j] += 1
    return True


def kill(e, i, j):
    # Removes a queen at (i, j)
    h = int(j > i)
    e.rows[0][i] -= 1
    e.cols[0][j] -= 1
    e.main_diags[h][abs(i - j)] -= 1
    e.neg_diags[0][i + j] -= 1
    e.board[i][j] -= 1


def solve(e, i, k, n):
    # Solves by backtracking
    if i == k: # Skips the row where the random queen was put
        i += 1
    if i >= n:
        return True
    for j in range(n):
        if place(e, i, j):
            if solve(e, i + 1, k, n):
                return True
            kill(e, i, j)
    return False


def queens(n):
    # Main function of solution.py, returns board with a solution
    e = Chess
    initialize(e, n)
    i = r.randint(0, n - 1)
    j = r.randint(0, n - 1)
    place(e, i, j)
    solve(e, 0, i, n)
    return e.board
