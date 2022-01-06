import os
import tempfile

import pytest

from homework4.task1 import read_magic_number


def test_read_magic_number_pos():
    """Existing file with normal content"""
    fp = tempfile.NamedTemporaryFile(mode='w+t', delete=False)
    fp.write('2')
    fp.close()
    result = read_magic_number(fp.name)
    if os.path.exists(fp.name):
        os.remove(fp.name)
    assert result


def test_read_magic_number_neg():
    """Existing file with out-of-bounds content"""
    fp = tempfile.NamedTemporaryFile(mode='w+t', delete=False)
    fp.write('-1')
    fp.close()
    result = read_magic_number(fp.name)
    if os.path.exists(fp.name):
        os.remove(fp.name)
    assert not result


def test_read_magic_number_not_number():
    """Existing file with abnormal content"""
    fp = tempfile.NamedTemporaryFile(mode='w+t', delete=False)
    fp.write('ddd')
    fp.close()
    with pytest.raises(ValueError):
        read_magic_number(fp.name)
        if os.path.exists(fp.name):
            os.remove(fp.name)


def test_read_magic_number_nofile():
    """Non-existing file"""
    with pytest.raises(ValueError):
        read_magic_number('1233')
