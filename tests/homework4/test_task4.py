import doctest
import os


def test_fizzbuzz():
    """ launch doctest for the file specified """
    doctest.testfile(os.getcwd() + "/homework4/task4.py",
                     module_relative=False)
