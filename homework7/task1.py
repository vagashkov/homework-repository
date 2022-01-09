"""
Given a dictionary (tree), that can contains multiple nested structures.
Write a function, that takes element and finds the number of occurrences
of this element in the tree.
Tree can only contains basic structures like:
    str, list, tuple, dict, set, int, bool
"""
from collections import abc
from typing import Any


def find_element(scope, element) -> int:
    """ recursive function to find element
    occurencies in any kind of object from listed
    in task definition """
    element_counter = 0
    # non-iterable object(int or bool)
    if not isinstance(scope, abc.Iterable):
        # making simple comparison
        if scope == element:
            element_counter += 1
    # iterable - but simply a string
    elif isinstance(scope, str):
        # making simple comparison too
        if scope == element:
            element_counter += 1
    # iterable object: list, tuple, dict, set
    else:
        # object is not dict - browse through its items
        if not isinstance(scope, abc.Mapping):
            for item in scope:
                element_counter += find_element(item, element)
        # mapping object (dict) - browse through values
        else:
            for item in scope.values():
                element_counter += find_element(item, element)
    return element_counter


def find_occurrences(tree: dict, element: Any) -> int:
    """ use resursive function to process tree """
    return find_element(tree, element)
