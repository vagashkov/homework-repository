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
        "unfinished!")]


@pytest.mark.parametrize("matrix, expected", test_data)
def test_tic_tac_toe_checker(matrix, expected):
    """ loading parametrized test for all the typical cases"""
    assert(tic_tac_toe_checker(matrix) == expected)
