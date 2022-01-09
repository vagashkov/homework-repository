from homework7.task1 import find_occurrences

# Example tree:
example_tree = {
    "first": ["RED", "BLUE"],
    "second": {
        "simple_key": ["simple", "list", "of", "RED", "valued"],
    },
    "third, fourth and fifth": {
        "abc": "BLUE",
        "jhl": "RED",
        "complex_key": {
            "key1": "value1",
            "key2": "RED",
            "key3": ["a", "lot", "of", "values", {"nested_key": "RED"}],
        }
     },
    "sixth": "RED",
    "seventh": ("RED",),
    "eighth": {"RED", "NOT_RED"},
    "ninth and tenth!": ["RED", ["RED"]]
}


def test_find_occurrences_ext():
    """ parsing an example tree """
    assert find_occurrences(example_tree, "RED") == 10
