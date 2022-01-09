import pytest

from homework7.task3 import tic_tac_toe_checker

test_data = [
    # row_winner
    ([
        ['-', '-', 'o'],
        ['-', 'o', 'o'],
        ['x', 'x', 'x']],
        "x wins!"),
    # column_winner
    ([
        ['-', '-', 'o'],
        ['-', 'o', 'o'],
        ['x', 'x', 'o']],
        "o wins!"),
    # down_diagonal_winner
    ([
        ['x', '-', 'o'],
        ['-', 'x', 'o'],
        ['o', '-', 'x']],
        "x wins!"),
    # up_diagonal_winner
    ([
        ['-', '-', 'o'],
        ['-', 'o', 'o'],
        ['o', '-', 'x']],
        "o wins!"),
    # draw
    ([
        ['o', 'o', 'x'],
        ['x', 'x', 'o'],
        ['o', 'o', 'x']],
        "draw!"),
    # unfinished
    ([
        ['-', 'o', 'x'],
        ['x', 'x', 'o'],
        ['o', 'o', 'x']],
        "unfinished!"),
    # unfinished II
    ([
        ['-', 'o', 'x'],
        ['x', '-', 'o'],
        ['o', 'o', '-']],
        "unfinished!"),
    # unfinished III
    ([
        ['o', 'o', '-'],
        ['x', '-', 'o'],
        ['-', 'o', 'x']],
        "unfinished!"),
    # unfinished IV
    ([
        ['-', '-', '-'],
        ['x', 'x', 'o'],
        ['o', 'o', 'x']],
        "unfinished!"),
    # unfinished V
    ([
        ['-', 'x', 'o'],
        ['-', 'x', 'o'],
        ['-', 'o', 'x']],
        "unfinished!"),
    # now check logic with bigger field
    # row_winner
    ([
        ['-', '-', 'o', '-', 'o'],
        ['-', 'o', 'o', 'o', 'x'],
        ['x', 'x', 'x', 'x', 'x'],
        ['-', '-', 'o', '-', 'o'],
        ['-', 'o', 'o', 'o', 'x']
    ],
        "x wins!"),
    # column_winner
    ([
        ['-', '-', 'o', '-', 'o'],
        ['-', 'o', 'o', 'o', 'x'],
        ['x', 'x', 'o', 'x', 'x'],
        ['-', '-', 'o', '-', 'o'],
        ['-', 'o', 'o', 'o', 'x']],
        "o wins!"),
    # down_diagonal_winner
    ([
        ['x', '-', 'o', '-', 'o'],
        ['-', 'x', 'o', 'o', 'x'],
        ['x', 'x', 'x', 'o', 'x'],
        ['-', '-', 'o', 'x', 'o'],
        ['-', 'o', 'o', 'o', 'x']],
        "x wins!"),
    # up_diagonal_winner
    ([
        ['-', '-', 'o', '-', 'o'],
        ['-', 'o', 'o', 'o', 'x'],
        ['x', 'x', 'o', 'x', 'x'],
        ['-', 'o', 'o', '-', 'o'],
        ['o', 'o', 'o', 'o', 'x']],
        "o wins!"),
    # draw
    ([
        ['o', 'x', 'o', 'x', 'o'],
        ['o', 'o', 'o', 'o', 'x'],
        ['x', 'x', 'x', 'o', 'x'],
        ['o', 'x', 'o', 'x', 'o'],
        ['o', 'o', 'o', 'o', 'x']],
        "draw!"),
    # unfinished
    ([
        ['-', '-', 'o', '-', 'o'],
        ['-', 'o', 'o', 'o', 'x'],
        ['x', 'x', '-', 'x', 'x'],
        ['-', '-', 'o', '-', 'o'],
        ['-', 'o', 'o', 'o', 'x']],
        "unfinished!"),
    # unfinished II
    ([
        ['-', '-', '-', '-', '-'],
        ['-', 'o', 'o', 'o', 'x'],
        ['x', 'o', 'x', 'x', 'x'],
        ['-', '-', 'o', '-', 'o'],
        ['-', 'o', 'o', 'o', 'x']],
        "unfinished!"),
    # unfinished III
    ([
        ['-', '-', 'o', '-', 'o'],
        ['-', 'o', 'o', 'o', 'x'],
        ['-', 'x', 'x', 'x', 'x'],
        ['-', '-', 'o', '-', 'o'],
        ['-', 'o', 'o', 'o', 'x']],
        "unfinished!"),
    # unfinished IV
    ([
        ['-', '-', 'o', '-', 'o'],
        ['-', '-', 'o', 'o', 'x'],
        ['o', 'x', '-', 'x', 'x'],
        ['-', '-', 'o', '-', 'o'],
        ['-', 'o', 'o', 'o', '-']],
        "unfinished!"),
    # unfinished V
    ([
        ['-', '-', 'o', '-', '-'],
        ['-', 'o', 'o', '-', 'x'],
        ['o', 'x', '-', 'x', 'x'],
        ['-', '-', 'o', '-', 'o'],
        ['-', 'o', 'o', 'o', 'x']],
        "unfinished!"),
    ]


@pytest.mark.parametrize("matrix, expected", test_data)
def test_tic_tac_toe_checker(matrix, expected):
    """ loading parametrized test for all the typical cases"""
    assert(tic_tac_toe_checker(matrix) == expected)
