"""
Write a function that merges integer from sorted files
and returns an iterator
file1.txt:
1
3
5
file2.txt:
2
4
6
>>> list(merge_sorted_files(["file1.txt", "file2.txt"]))
[1, 2, 3, 4, 5, 6]
"""
import os
from pathlib import Path
from typing import Iterator, List, Union


def value_generator(file_name):
    """ generator function reads file line-by-line
    and returns line content as int value (if it contains any)"""
    with open(os.getcwd()+"//"+file_name, "r",
              encoding='utf-8-sig') as file:
        for line in file:
            # checking if it is really an int
            if line.strip().isdigit():
                yield int(line.strip())


def merge_sorted_files(file_list: List[Union[Path, str]]) -> Iterator:
    """ parsing through the files, constructing list and sorting it """
    all_numbers = []
    # building number list from all files
    # we can use nested list comprehension
    # but for loop maybe more readable
    for filename in file_list:
        file_numbers = [num for num in value_generator(filename)]
        all_numbers += file_numbers
    # sorting result and returning iterator object
    return iter(sorted(all_numbers))
