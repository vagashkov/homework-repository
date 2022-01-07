from homework5.task2 import custom_sum


def test_custom_sum_with_print(capsys):
    """ Checking base scenario - with wrapper
    (we can see it by printing to stdout ) """
    assert custom_sum([1, 2, 3], [4, 5]) == [1, 2, 3, 4, 5]
    assert custom_sum.__name__ == "custom_sum"
    func_info = "This function can sum any objects which have __add___"
    assert custom_sum.__doc__ == func_info
    assert capsys.readouterr().out == "[1, 2, 3, 4, 5]\n"


def test_custom_sum_with_no_print(capsys):
    """ Checking original_func scenario - without wrapper
    (and so we get result without printing to stdout ) """
    without_print = custom_sum.__original_func
    assert without_print(1, 2, 3, 4) == 10
    assert capsys.readouterr().out == ""
