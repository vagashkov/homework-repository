"""
Classic task, a kind of walnut for you
Given four lists A, B, C, D of integer values,
    compute how many tuples (i, j, k, l) there are such that
    A[i] + B[j] + C[k] + D[l] is zero.
We guarantee, that all A, B, C, D have same length of N where 0 ? N ? 1000.
"""
from itertools import product
from typing import List


def check_sum_of_four(
                                      a: List[int],
                                      b: List[int],
                                      c: List[int],
                                      d: List[int]) -> int:
    """ function computes how many element
    combination of four lists have sum of zero """
    # trying to explore all the posible combinations
    # among four lists using itertools.product
    # function
    counter = 0
    for list_elements in product(a, b, c, d):
        # checking if sum of elements is equal to 0
        if sum(list_elements) == 0:
            # and increment counter if necessary
            counter = counter + 1
    return counter
