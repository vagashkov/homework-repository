import pytest

from homework1.task1 import check_power_of_2


def test_negative_number():
    """Testing that actual powers of -15 gives False"""
    assert not check_power_of_2(-15)


def test_zero_number():
    """Testing that actual powers of zero gives False"""
    assert not check_power_of_2(0)


def test_single_number():
    """Testing that actual powers of 1 gives True"""
    assert check_power_of_2(1)


def test_odd_number():
    """Testing that odd numbers give False"""
    assert not check_power_of_2(33)


def test_even_number():
    """Testing that even non-powers of 2 give False"""
    assert not check_power_of_2(42)


def test_positive_case():
    """Testing that actual powers of S2 give True"""
    assert check_power_of_2(65536)
