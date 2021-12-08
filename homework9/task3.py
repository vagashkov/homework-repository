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
import os
from pathlib import Path
from typing import Callable, Optional


def universal_file_counter(
    dir_path: Path,
    file_extension: str,
    tokenizer: Optional[Callable] = None
) -> int:
    """ function to count number of token occasions in
    all the files with specified extension in given directory"""
    counter = 0
    # browsing through the directory (first level only)
    for filename in os.listdir(dir_path):
        file = os.fsdecode(filename)
        # checking if file extension is correct
        if file.lower().endswith("."+file_extension):
            with open(os.path.join(dir_path, file), "r",
                      encoding='utf-8-sig') as fi:
                # no tokenizer given - simply count
                # number of strings
                if not tokenizer:
                    file_count = sum(1 for line in fi)
                    counter += file_count
                else:
                    # we have callable tokenizer - so apply it
                    # to file content and get a number of occasions
                    counter += len(tokenizer.__call__(fi.read()))
    return counter
