from typing import Sequence


def check_fibonacci(data: Sequence[int]) -> bool:
    for item in data:
        if not isinstance(item, int):
            return False
        if item < 0:
            return False
    if len(data) < 3:
        return False
    while len(data) > 2:
        a, b, c = data[0], data[1], data[2]
        if a + b != c:
            return False
        else:
            data = data[1:]
    return True
