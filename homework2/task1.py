"""
Given a file containing text. Complete using only default collections:
    1) Find 10 longest words consisting from largest amount of unique symbols
    2) Find rarest symbol for document
    3) Count every punctuation char
    4) Count every non ascii char
    5) Find most common non ascii char for document
"""
import os
import re
import string
from typing import List


def get_longest_diverse_words(file_path: str,
                              encoding="utf-8") -> List[str]:
    """ Find 10 longest words consisting from largest amount
    of unique symbols """
    # we will collect all unique words in list and than sort it by len
    res_list = []
    # trying to open file
    with open(os.getcwd() + file_path, "r", encoding=encoding) as fi:
        # and walking it line by line
        for line in fi:
            # splitting line in words
            for word in line.split():
                word = word.translate(str.maketrans("", "",
                                                    string.punctuation))
                # putting new word into dict (or update existing)
                if word not in res_list:
                    res_list.append(word)
    # sorting words by len in reverse order
    res_list.sort(key=lambda s: len(set(s)), reverse=True)
    # and returning results
    return res_list[:10]


def get_rarest_char(file_path: str, encoding="utf-8") -> str:
    """ Find rarest symbol for document """
    res_dict = {}
    # trying to open file
    with open(os.getcwd() + file_path, "r", encoding=encoding) as fi:
        # and walking it line by line
        for line in fi:
            for char in line:
                # new character
                if char not in res_dict.keys():
                    res_dict[char] = 1
                # already known character
                else:
                    res_dict[char] += 1
    # sort dict (as of since Python 3.7 and later dicts are stored
    # as ordered collections) by item values
    res_dict = dict(sorted(res_dict.items(), key=lambda item: item[1]))
    # and return first key ( = the rarest char)
    return list(res_dict)[0]


def count_punctuation_chars(file_path: str,
                            encoding="utf-8") -> int:
    """ Count every punctuation char """
    punctuation = "!\"#$%&'()*+, -./:;<=>?@[\\]^_`{|}~"
    counter = 0
    # trying to open file
    with open(os.getcwd() + file_path, "r", encoding=encoding) as fi:
        # and walking it line by line
        for line in fi:
            for char in line:
                if char in punctuation:
                    counter += 1
    # and returning results
    return counter


def count_non_ascii_chars(file_path: str,
                          encoding="utf-8") -> int:
    """ Count every non ascii char """
    pattern = r'[\u0080-\uFFFF]'
    counter = 0
    # trying to open file
    with open(os.getcwd() + file_path) as fi:
        # and walking it line by line
        for line in fi:
            counter += len(re.findall(pattern,
                                      bytes(line,
                                            "ascii").decode(encoding)))
    # and returning results
    return counter


def get_most_common_non_ascii_char(file_path: str,
                                   encoding="utf-8") -> str:
    """ Find most common non ascii char for document """
    res_dict = {}
    # trying to open file
    with open(os.getcwd() + file_path) as fi:
        # and walking it line by line
        for line in fi:
            # checking characters one by one
            for char in bytes(line, "ascii").decode(encoding):
                # got non-ascii
                if not char.isascii():
                    # new one
                    if char not in res_dict.keys():
                        res_dict[char] = 1
                    # already known
                    else:
                        res_dict[char] += 1
    # sort dict (as of since Python 3.7 and later dicts are stored
    # as ordered collections) by item values
    res_dict = dict(sorted(res_dict.items(), key=lambda item: item[1]))
    # and return last key ( = the most common char)
    return list(res_dict)[-1]
