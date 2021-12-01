"""
Given a dictionary (tree), that can contains multiple nested structures.
Write a function, that takes element and finds the number of occurrences
of this element in the tree.
Tree can only contains basic structures like:
    str, list, tuple, dict, set, int, bool
"""
from typing import Any


def find_occurrences(tree: dict, element: Any) -> int:
    element_counter = 0
    for key, value in tree.items():
        # looking for element ocurrences is dict itself
        # direct comparison
        if value == element:
            print(key)
            element_counter += 1
        # element is.. an element of value (int in set f.e.)
        elif element in value:
            print(key)
            element_counter += 1
        # now let's look in nested structures
        elif isinstance(value, dict):
            element_counter += find_occurrences(value, element)
        elif isinstance(value, list):
            for item in value:
                if isinstance(item, dict):
                    element_counter += find_occurrences(item, element)
    return element_counter
