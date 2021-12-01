from homework7.task1 import find_occurrences

# Example tree:
example_tree = {
    "first": ["RED", "BLUE"],
    "second": {
        "simple_key": ["simple", "list", "of", "RED", "valued"],
    },
    "third": {
        "abc": "BLUE",
        "jhl": "RED",
        "complex_key": {
            "key1": "value1",
            "key2": "RED",
            "key3": ["a", "lot", "of", "values", {"nested_key": "RED"}],
        }
     },
    "fourth": "RED",
    "fifth": ("RED",),
    "sixth": {"RED", "NOT_RED"}
}


def test_find_occurrences_ext():
    """ parsing an example tree (with tuple and set appended)"""
    assert find_occurrences(example_tree, "RED") == 8
