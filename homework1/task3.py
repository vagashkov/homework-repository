"""
Write down the function, which reads input line-by-line,
and find maximum and minimum values.
Function should return a tuple with the max and min values.
For example for [1, 2, 3, 4, 5], function should return [1, 5]
We guarantee, that file exists and contains line-delimited integers.
To read file line-by-line you can use this snippet:
with open("some_file.txt") as fi:
    for line in fi:
        ...
"""
import os
from typing import Tuple


def find_maximum_and_minimum(file_name: str) -> Tuple[int, int]:
    # setting min and max initial values
    min = 0
    max = 0

    # trying to open file
    with open(os.getcwd() + file_name, "r") as fi:
        # and walking it line by line
        for line in fi:
            # new minimum found
            if int(line) < min:
                min = int(line)
            # new maximum found
            if int(line) > max:
                max = int(line)
    # closing the file
    fi.close()
    # and returning results
    return (max, min)
