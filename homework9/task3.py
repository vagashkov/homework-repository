"""
Write a function that takes directory path,
a file extension and an optional tokenizer.
It will count lines in all files with that extension
if  there are no tokenizer.
If a the tokenizer is not none, it will count tokens.
For dir with two files from hw1.py:
>>> universal_file_counter(test_dir, "txt")
6
>>> universal_file_counter(test_dir, "txt", str.split)
6
"""
from pathlib import Path
from typing import Callable, Optional


def single_file_counter(file_path: Path,
                        tokenizer: Optional[Callable] = None) -> int:
    """ function counts lines in spicified file if
    tokenizer is None, otherwise counts tokens """
    with open(file_path, "r",
              encoding='utf-8-sig') as fi:
        # no tokenizer given - simply count
        # number of strings
        if not tokenizer:
            return sum(1 for line in fi)
        else:
            # we have callable tokenizer - so apply it
            # to file content and get a number of occasions
            return len(tokenizer.__call__(fi.read()))


def universal_file_counter(
        dir_path: Path,
        file_extension: str,
        tokenizer: Optional[Callable] = None) -> int:
    """ function to count number of token occasions in
    all the files with specified extension in given directory"""
    counter = 0
    # browsing through the directory
    path = Path(dir_path)
    for element in path.glob("**/*." + file_extension):
        counter += single_file_counter(element, tokenizer)
    return counter
