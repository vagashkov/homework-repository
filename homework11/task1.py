"""
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
    """ class to produce classes """
    def __new__(meta_cls, cls_name, cls_bases, dict):
        # first check if dict has an item with keys list
        # ("_" + cls_name + "__keys")
        keys_list = "_" + cls_name + "__keys"
        if keys_list in dict:
            # now we need to build temp dict with values from __keys
            keys_values = {key: key for key in dict[keys_list]}
            # update initial attributes list with values
            dict.update(keys_values)
        # and finally build new class with updated attributes list
        return super(SimplifiedEnum,
                     meta_cls).__new__(meta_cls, cls_name, cls_bases, dict)
