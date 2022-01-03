import string

from homework2.task5 import custom_range


def test_custom_range_1arg():
    """Testing with 1 positional argument"""
    assert custom_range(
                        string.ascii_lowercase,
                        'g') == ['a', 'b', 'c', 'd', 'e', 'f']


def test_custom_range_2args():
    """Testing with 2 positional arguments"""
    assert custom_range(
                        string.ascii_lowercase,
                        'g', 'p') == ['g', 'h', 'i', 'j',
                                      'k', 'l', 'm', 'n', 'o']


def test_custom_range_3args():
    """Testing with 3 positional arguments"""
    assert custom_range(
                        string.ascii_lowercase,
                        'p', 'g', -2) == ['p', 'n', 'l', 'j', 'h']
