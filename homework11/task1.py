﻿"""
Vasya implemented nonoptimal Enum classes.
Remove duplications in variables declarations
using metaclasses.

from enum import Enum
class ColorsEnum(Enum):
    RED = "RED"
    BLUE = "BLUE"
    ORANGE = "ORANGE"
    BLACK = "BLACK"
class SizesEnum(Enum):
    XL = "XL"
    L = "L"
    M = "M"
    S = "S"
    XS = "XS"

Should become:
class ColorsEnum(metaclass=SimplifiedEnum):
    __keys = ("RED", "BLUE", "ORANGE", "BLACK")
class SizesEnum(metaclass=SimplifiedEnum):
    __keys = ("XL", "L", "M", "S", "XS")
assert ColorsEnum.RED == "RED"
assert SizesEnum.XL == "XL"
"""


class SimplifiedEnum(type):
    def __new__(meta_cls, name, bases, dct):
        """ building new class object from scratch """
        return super(SimplifiedEnum,
                     meta_cls).__new__(meta_cls, name, bases, dct)

    def __getattr__(self, attr):
        """ simulate 'enum-like' behavour """
        if attr in self.keys_list:
            return attr
        return None
