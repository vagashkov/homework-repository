from homework4.task5 import fizzbuzz


def test_fizzbuzz():
    """ Testing rather short sequence of 31 numbers"""
    assert list(fizzbuzz(31)) == [
        '1', '2', 'fizz', '4', 'buzz',
        'fizz', '7', '8', 'fizz', 'buzz',
        '11', 'fizz', '13', '14', 'fizzbuzz',
        '16', '17', 'fizz', '19', 'buzz',
        'fizz', '22', '23', 'fizz',
        'buzz', '26', 'fizz', '28', '29', 'fizzbuzz', '31'
        ]
