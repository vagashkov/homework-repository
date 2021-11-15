"""
Write a function that takes K lists as arguments and returns all possible
lists of K items where the first element is from the first list,
the second is from the second and so one.
You may assume that that every list contain at least one element
Example:
assert combinations([1, 2], [3, 4]) == [
    [1, 3],
    [1, 4],
    [2, 3],
    [2, 4],
]
"""
from typing import Any, List


def combinations(*args: List[Any]) -> List[List]:
    lists_list = list(args)
    res_list = []
    # getting all the possible combinations
    for list_i in lists_list:
        for list_j in lists_list:
            if not (list_i is list_j):
                for item_i in list_i:
                    for item_j in list_j:
                        if not (item_i is item_j):
                            res_list.append([item_i, item_j])
    return res_list[:int(len(res_list)/2)]
