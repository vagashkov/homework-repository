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
    most = 0
    least = 0
    data = {}

    # calculating number of occasions for all unique elements
    for item in set(inp):
        data[item] = inp.count(item)
    # now getting the least and most common element
    for key in data.keys():
        if data[key] == sorted(list(data.values()))[0]:
            least = key
        if data[key] == sorted(list(data.values()))[-1]:
            most = key
    return(most, least)
