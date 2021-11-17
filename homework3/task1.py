"""
In previous homework task 4, you wrote a cache function that remembers
other function output value. Modify it to be a parametrized decorator,
so that the following code:
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
from functools import lru_cache
from typing import Callable


def f():
    return input('? ')


def timed_cache(func: Callable, times: int) -> Callable:
    def cached(func: Callable) -> Callable:
        # enabling caching for called function
        @lru_cache(maxsize=times)
        def wrapper(*args, **kwargs):
            # returning initial function object
            return func(*args, **kwargs)
        return wrapper
    cached_func = cached(func)
    # here we need to use times somehow
    return cached_func


cache_func = timed_cache(f, 2)
print(cache_func())
print(cache_func())
print(cache_func())
print(cache_func())
print(cache_func())
