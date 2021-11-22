"""
This task is optional.
Write a generator that takes a number N as an input
and returns a generator that yields N FizzBuzz numbers*
Don't use any ifs, you can find an approach
for the implementation in this video**.
Definition of done:
 - function is created
 - function is properly formatted
 - function has tests
>>> list(fizzbuzz(5))
["1", "2", "fizz", "4", "buzz"]
* https://en.wikipedia.org/wiki/Fizz_buzz
** https://www.youtube.com/watch?v=NSzsYWckGd4
"""
# making 'pattern lists' for triples and fives
triple_list = ['', '', "fizz"]
five_list = ['', '', '', '', 'buzz']


def fizzbuzz(n: int):
    # biulding triples list from 1 to parameter value
    triples = triple_list*(n // 3) + triple_list[:n % 3]
    # and fives list from 1 to parameter value
    pentas = five_list*(n // 5) + five_list[:n % 5]
    # zipping two lists using simple map function:
    # res[i] = triples[i] + fives[i]
    # (string concatenation works as well for fizzbuzz numbers)
    return map(lambda x: x[0] + x[1], zip(triples, pentas))
