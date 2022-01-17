from homework11.task1 import SimplifiedEnum


def test_colors_enum():
    """ test for colors enumeration-like object """
    class ColorsEnum(metaclass=SimplifiedEnum):
        __keys = ("RED", "BLUE", "ORANGE", "BLACK")
    assert ColorsEnum.RED == "RED"


def test_sizes_enum():
    """ test for sizes enumeration-like object """
    class SizesEnum(metaclass=SimplifiedEnum):
        __keys = ("XL", "L", "M", "S", "XS")
    assert SizesEnum.XL == "XL"
