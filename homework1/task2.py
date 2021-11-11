"""
Given a cell with "it's a fib sequence" from slideshow,
    please write function "check_fib", which accepts a Sequence of integers, and
    returns if the given sequence is a Fibonacci sequence
We guarantee, that the given sequence contain >= 0 integers inside.
"""
from typing import Sequence


def check_fibonacci(data: Sequence[int]) -> bool:
    # precheck: Fibonacci sequence can contain
    # only positive integer or zero
    for item in data:
        # we found something that is not integer
        if not isinstance(item, int):
            return False
        # and not positive or zero
        if item < 0:
            return False
    # seq is too short
    if len(data) < 3:
        return False
    # now browse throunh the sequence
    while len(data) > 2:
        # getting it's 'head'
        a, b, c = data[0], data[1], data[2]
        # check the condition
        if a + b != c:
            return False
        # .. and move forward if it was fullfilled
        else:
            data = data[1:]
    # we checked all the sequence and it is fine
    return True
