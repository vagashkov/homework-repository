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
    # getting the iterator object from iterable
    some_iterator = iter(some_iterable)
    # getting all the values from iterator
    source_list = [x for x in some_iterator]
    res_list = []
    # right bound-based range
    if len(args) == 1:
        return source_list[:source_list.index(args[0])]
    # left and right bound-based range
    elif len(args) == 2:
        return source_list[source_list.index(args[0]):
                           source_list.index(args[1])]
    # left and right bound-based range with custom step
    elif len(args) == 3:
        return source_list[source_list.index(args[0]):
                           source_list.index(args[1]):args[2]]
    else:
        pass
    return res_list
