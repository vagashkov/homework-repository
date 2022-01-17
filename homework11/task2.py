"""
You are given the following code:
class Order:
    morning_discount = 0.25
    def __init__(self, price):
        self.price = price
    def final_price(self):
        return self.price - self.price * self.morning_discount
Make it possible to use different discount programs.
Hint: use strategy behavioural OOP pattern.
https://refactoring.guru/design-patterns/strategy
Example of the result call:
def morning_discount(order):
    ...
def elder_discount(order):
    ...
order_1 = Order(100, morning_discount)
assert order_1.final_price() == 75
order_2 = Order(100, elder_discount)
assert order_2.final_price() == 10
"""
from typing import Callable


def morning_discount(order) -> float:
    """ calculate discount for mornings """
    discount_rate = 0.25
    return 1-discount_rate


def elder_discount(order) -> float:
    """ calculate discount for long-timers """
    discount_rate = 0.9
    return 1-discount_rate


def student_discount(order) -> float:
    """ calculate discount for students """
    discount_rate = 0.3
    return 1-discount_rate


class Order:
    """ class to calculate discounts """
    def __init__(self, price, calc_discount_func: Callable[[], float] = None):
        """ store price and discount calculate function
        (if any) """
        self.price = price
        # if we have discount function object -
        # store it in attribute
        if calc_discount_func:
            self.calc_discount = calc_discount_func

    def final_price(self) -> float:
        """ calculate discount for current order """
        if self.calc_discount:
            return self.price*self.calc_discount(self)
        # no discount - pay full price
        else:
            return self.price
