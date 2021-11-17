import hashlib
import random
import struct
import time
from multiprocessing import Pool


def slow_calculate(value):
    """Some weird voodoo magic calculations"""
    time.sleep(random.randint(1, 3))
    data = hashlib.md5(str(value).encode()).digest()
    return sum(struct.unpack('<' + 'B' * len(data), data))


def make_calculate():
    # start 25 worker processes
    with Pool(processes=25) as pool:
        result_list = pool.map(slow_calculate, range(500))
    return sum(result_list)


if __name__ == '__main__':
    # start 25 worker processes
    with Pool(processes=25) as pool:
        result_list = pool.map(slow_calculate, range(500))
    print(sum(result_list))
