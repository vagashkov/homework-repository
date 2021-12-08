import pytest

from homework9.task2 import IndexErrorSupressor, supressor

test_data = [(0, 2), (18, None)]
my_list = [2, 1, 0]


@pytest.mark.parametrize("index, value", test_data)
def test_supressor_as_gen(index, value):
    """ testing suppressor as a generator"""
    with supressor(my_list, index) as element:
        assert element == value


def test_supressor_as_class_positive():
    """ testing supressor as a class with no errors """
    with IndexErrorSupressor():
        assert my_list[0] == 2


def test_supressor_as_class_negative(capsys):
    """ testing supressor as a class with errors intercepted """
    with IndexErrorSupressor():
        my_list[18]
        captured = capsys.readouterr()
        assert captured.out == "IndexError exception intercepted\n"
