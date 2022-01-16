import time

from homework3.task2 import make_calculate


def test_make_calculate():
    """ Cheking both result and execution time """
    start = time.time()
    assert make_calculate() == 1024259
    finish = time.time()
    assert int(finish-start) < 60
