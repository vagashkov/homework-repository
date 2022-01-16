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
    # making an empty 'item-number of occasions' dict
    item_counts = {}

    # calculating number of occasions for all unique elements
    for item in set(inp):
        item_counts[item] = inp.count(item)
    # now convert sorted dict to list of tuples
    counts = list(sorted(item_counts.items(), key=lambda item: item[1]))
    # and return it's last (most common) and first (least common) elements
    return(counts[-1][0], counts[0][0])
