"""
In previous homework task 4, you wrote a cache function
that remembers other function output value.
Modify it to be a parametrized decorator, so that the following code:

@cache(times=3)
def some_function():
    pass

Would give out cached value up to times number only. Example:

@cache(times=2)
def f():
    # careful with input() in python2, use raw_input() instead
    return input('? ')

>>> f()
? 1
'1'
>>> f()     # will remember previous value
'1'
>>> f()     # but use it up to two times only
'1'
>>> f()
? 2
'2'

"""

from functools import lru_cache, wraps
from typing import Callable


def timed_lru_cache(func: Callable, maxsize: int):
    """Extension of functools lru_cache with a function starts counter
    Parameters:
    func (Callable): function to be cached
    maxsize (int): maximum size of cached calls
    """
    def wrapper_cache(f):
        # getting cached version of given function
        cached_func = lru_cache()(f)
        # putting function calls counter initial value
        # and maximum starts before 'reload'
        # directly into function object
        cached_func.counter = 0
        cached_func.maxsize = maxsize

        # adding 'reload' logic
        # cached func will clear its cache
        # after every maxsize starts
        @wraps(cached_func)
        def wrapped_f(*args, **kwargs):
            if cached_func.counter >= cached_func.maxsize:
                # reload point detected
                cached_func.cache_clear()
                cached_func.counter = 0
            cached_func.counter += 1
            return cached_func(*args, **kwargs)
        return wrapped_f
    # returning cached and maxsize-based function object
    return wrapper_cache(func)
