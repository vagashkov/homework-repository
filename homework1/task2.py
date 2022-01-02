"""
Given a cell with "it's a fib sequence" from slideshow,
    please write function "check_fib",
    which accepts a Sequence of integers, and
    returns if the given sequence is a Fibonacci sequence
We guarantee, that the given sequence contain >= 0 integers inside.
"""
from typing import Sequence


def gen_fibonacci(start: int):
    """ function builds Fibonacci sequence
    using parameter as a lower margin """
    i = 0
    j = 1
    while True:
        if i >= start:
            yield i
        i, j = j, i+j


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
    # now browse throgh both sequences -
    # that we are checking and that we just built,
    # comparint it element by element
    for data_member, fib_member in zip(data,
                                       gen_fibonacci(data[0])):
        if data_member != fib_member:
            return False
    # we checked all the sequence and it is fine
    return True
