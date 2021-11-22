from homework4.task5 import fizzbuzz


def test_fizzbuzz():
    """ Testing rather short sequence of 31 numbers"""
    assert list(fizzbuzz(31)) == [
        '', '', 'fizz', '', 'buzz',
        'fizz', '', '', 'fizz', 'buzz',
        '', 'fizz', '', '', 'fizzbuzz',
        '', '', 'fizz', '', 'buzz',
        'fizz', '', '', 'fizz',
        'buzz', '', 'fizz', '', '', 'fizzbuzz', ''
        ]
