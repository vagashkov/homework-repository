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


def pattern(base):
    """ declarative-based approach function
    that returns value according with FizzBuzz sequence
    definition """
    yield str(base + 1)  # number
    yield str(base + 2)  # number
    yield "fizz"  # third position - fizz!
    yield str(base + 4)  # number
    yield "buzz"  # fifth position - buzz!!
    yield "fizz"  # sixth (3*2) position - fizz
    yield str(base + 7)  # number
    yield str(base + 8)  # number
    yield "fizz"  # ninth (3*3) position - fizz
    yield "buzz"  # tenth (5*2) position - buzz
    yield str(base + 11)  # number
    yield "fizz"  # twelth position (3*4) - fizz
    yield str(base + 13)  # number
    yield str(base + 14)  # number
    yield "fizzbuzz"  # fithteenth (3*5) position - fizzbuzz!


def fizzbuzz_generator():
    """ endless fizzbuzz sequence generator """
    counter = 0
    while True:
        # return pattern value
        for element in pattern(counter*15):
            yield element
        counter += 1


def fizzbuzz(n):
    """ getting fizzbuzz generator function object and
    use it to produce limited fizzbuzz sequence"""
    source_generator = fizzbuzz_generator()
    for _ in range(n):
        yield next(source_generator)
