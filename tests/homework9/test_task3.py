import os

import pytest

from homework9.task3 import universal_file_counter

test_data = [
    ((os.getcwd()+"/homework9/", "txt", None), 13),
    ((os.getcwd()+"/homework9/", "txt", str.split), 15)
]


@pytest.mark.parametrize("params, result", test_data)
def test_universal_file_counter(params, result):
    """ testing tokenizer for different tokens"""
    assert universal_file_counter(*params) == result
