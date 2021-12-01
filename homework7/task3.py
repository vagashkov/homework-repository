"""
Given a Tic-Tac-Toe 3x3 board (can be unfinished).
Write a function that checks if the are some winners.
If there is "x" winner, function should return "x wins!"
If there is "o" winner, function should return "o wins!"
If there is a draw, function should return "draw!"
If board is unfinished, function should return "unfinished!"

Example:
    [[-, -, o],
     [-, x, o],
     [x, o, x]]
    Return value should be "unfinished"

    [[-, -, o],
     [-, o, o],
     [x, x, x]]

     Return value should be "x wins!"

"""
from typing import List


def tic_tac_toe_checker(board: List[List]) -> str:
    # checking rows - if it contains winner (all the same characters)
    # it's set length will be 1
    for row in board:
        if len(set(row)) == 1:
            return set(row).pop() + " wins!"

    # checking columns
    for i in range(len(board[0])):
        column = [row[i] for row in board]
        if len(set(column)) == 1:
            return column[0] + " wins!"

    # checking downrising diagonal
    diagonal = [board[i][i] for i in range(len(board[0]))]
    if len(set(diagonal)) == 1:
        return diagonal[0] + " wins!"

    # checking uprising diagonal
    diagonal = []
    for i in range(len(board[0])):
        diagonal.append(board[i][len(board[0])-1-i])
    if len(set(diagonal)) == 1:
        return diagonal[0] + " wins!"

    # so if we are here - no one wins or the game is still in progress?
    matrix = set()
    for row in board:
        matrix.update(row)
    if '-' in set(matrix):
        return "unfinished!"

    return "draw!"
