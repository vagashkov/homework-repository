"""
Some of the functions have a bit cumbersome behavior when we deal with
positional and keyword arguments.
Write a function that accept any iterable of unique values and then
it behaves as range function:
import string
assert = custom_range(string.ascii_lowercase, 'g') ==
['a', 'b', 'c', 'd', 'e', 'f']
assert = custom_range(string.ascii_lowercase, 'g', 'p') ==
['g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o']
assert = custom_range(string.ascii_lowercase, 'p', 'g', -2) ==
['p', 'n', 'l', 'j', 'h']
"""


def custom_range(some_iterable, *args):
    # transfming iterable into sequence
    # in order to use slicing
    source_list = list(some_iterable)
    # building initial values for slicing parameters
    start_pos = 0
    end_pos = len(source_list)
    step = 1
    # parsing different args combinations:
    # right bound-based range
    if len(args) == 1:
        end_pos = source_list.index(args[0])
    # left and right bound-based range
    elif len(args) == 2:
        start_pos = source_list.index(args[0])
        end_pos = source_list.index(args[1])
    # left and right bound-based range with custom step
    elif len(args) == 3:
        start_pos = source_list.index(args[0])
        end_pos = source_list.index(args[1])
        step = args[2]
    else:
        pass
    return source_list[start_pos:end_pos:step]
