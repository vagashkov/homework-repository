import pytest

from homework8.task1 import KeyValueStorage

# preparing test data and expected results
test_data = [
    ('name', 'kek'),
    ('last_name', 'top'),
    ('power', 9001),
    ('song', 'shadilay')]


@pytest.mark.parametrize("key, value", test_data)
def test_attr_access(key, value):
    """Testing attribute-based access """
    storage = KeyValueStorage("/homework8/task1.txt")
    assert getattr(storage, key) == value


@pytest.mark.parametrize("key, value", test_data)
def test_dict_access(key, value):
    """Testing dict key-based access """
    storage = KeyValueStorage("/homework8/task1.txt")
    assert storage[key] == value


def test_builtin_attr_and_key():
    """Testing for built-ins access
    (for example, __class__) as an attribute
    and as a key """
    storage = KeyValueStorage("/homework8/task1b.txt")
    assert isinstance(storage, storage.__class__)
    assert storage["__class__"] == "addict"


def test_new_attr():
    """ setting new attr value"""
    storage = KeyValueStorage("/homework8/task1.txt")
    new_key = "new_key"
    new_value = "new value"
    storage.new_key = new_value
    # reopen storage
    storage = KeyValueStorage("/homework8/task1.txt")
    assert storage[new_key] == "new value"


def test_change_attr():
    """ setting existing attr value"""
    storage = KeyValueStorage("/homework8/task1.txt")
    new_key = "new_key"
    new_value = "really new value"
    storage.new_key = new_value
    # reopen storage
    storage = KeyValueStorage("/homework8/task1.txt")
    assert storage[new_key] == "really new value"


def test_del_attr():
    """ deleting existing attr value"""
    storage = KeyValueStorage("/homework8/task1.txt")
    delattr(storage, "new_key")
    # reopen storage
    storage = KeyValueStorage("/homework8/task1.txt")
    assert "new_key" not in storage
