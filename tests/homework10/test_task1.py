import os
from os.path import exists

from homework10.task1 import build_data

# files list to check
files_list = [
        "price_winners.txt",
        "pe_winners.txt",
        "growth_winners.txt",
        "bargain_winners.txt"
]


def test_build_data():
    """ function initiates data gathering and analyzing
    process and checks for existance all the result files """
    build_data()
    for result in files_list:
        assert exists(os.getcwd() + r"/homework10/" + result)
