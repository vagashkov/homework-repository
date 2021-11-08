import os
import sys
from typing import Tuple


def find_maximum_and_minimum(file_name: str) -> Tuple[int, int]:
    min = 0
    max = 0

    with open(os.getcwd() + file_name, "r") as fi:
        for line in fi:
            if int(line) < min:
                min = int(line)
            if int(line) > max:
                max = int(line)
    fi.close()
    return (max, min)
