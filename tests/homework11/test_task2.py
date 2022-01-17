import pytest

from homework11.task2 import (Order, elder_discount, morning_discount,
                              student_discount)

test_data = [
    (morning_discount, 75),
    (elder_discount, 10),
    (student_discount, 70)]


@pytest.mark.parametrize("discount_type, expected_value", test_data)
def test_discounts(discount_type, expected_value):
    """ check three different discount types one by one"""
    order = Order(100, discount_type)
    assert round(order.final_price()) == expected_value
