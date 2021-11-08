from typing import List


def check_sum_of_four(
                                      a: List[int],
                                      b: List[int],
                                      c: List[int],
                                      d: List[int]) -> int:
    # trying to explore all the
    # posible combinations
    # among four lists
    counter = 0
    for item_a in a:
        for item_b in b:
            for item_c in c:
                for item_d in d:
                    # got the zero sum combo
                    if item_a + item_b + item_c + item_d == 0:
                        counter = counter + 1
    return counter
