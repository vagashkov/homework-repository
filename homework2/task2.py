"""
Given an array of size n, find the most common and the least common elements.
The most common element is the element that appears more than n // 2 times.
The least common element is the element that appears fewer than other.
You may assume that the array is non-empty and the most common element
always exist in the array.
Example 1:
Input: [3,2,3]
Output: 3, 2
Example 2:
Input: [2,2,1,1,1,2,2]
Output: 2, 1
"""
from typing import List, Tuple


def major_and_minor_elem(inp: List) -> Tuple[int, int]:
    # setting up initial values
    most_elem = None
    least_elem = None
    most_count = 0
    least_count = len(inp)

    # calculating number of occasions for all unique elements
    for item in set(inp):
        # getting number of occasions for current item
        item_count = inp.count(item)
        # new leader detected
        if item_count > most_count:
            most_elem = item
            most_count = item_count
        # new "looser"
        if item_count < least_count:
            least_elem = item
            least_count = item_count
    return(most_elem, least_elem)
