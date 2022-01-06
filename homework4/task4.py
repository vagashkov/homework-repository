"""
Write a function that takes a number N as an input
and returns N FizzBuzz numbers*
Write a doctest for that function.
Definition of done:
 - function is created
 - function is properly formatted
 - function has doctests
 - doctests are run with pytest command
You will learn:
 - the most common test task for developers
 - how to write doctests
 - how to run doctests
assert fizzbuzz(5) == ["1", "2", "fizz", "4", "buzz"]
* https://en.wikipedia.org/wiki/Fizz_buzz
** Энциклопедия профессора Фортрана page 14, 15,
"Робот Фортран, чисть картошку!"
"""
from typing import List


def fizzbuzz(n: int) -> List[str]:
    """ Takes a number N as an input and returns N FizzBuzz numbers
    >>> fizzbuzz(10)
    ['1', '2', 'fizz', '4', 'buzz', 'fizz', '7', '8', 'fizz', 'buzz']
    """
    result_list = []
    for count in range(1, n+1):
        # got a number that can be divided by 3 and 5!
        if not count % 15:
            result_list.append("fizzbuzz")
        # by 3 only
        elif not count % 3:
            result_list.append("fizz")
        # by 5
        elif not count % 5:
            result_list.append("buzz")
        # neither by 3, nor by 5
        else:
            result_list.append(str(count))
    return result_list
