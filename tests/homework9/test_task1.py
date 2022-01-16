import pytest

from homework9.task1 import merge_sorted_files

test_data = [
    (["homework9//file1.txt", "homework9//file2.txt", "homework9//file3.txt"],
        [1, 2, 3, 4, 5, 6, 7, 66, 77, 88, 99])
]


@pytest.mark.parametrize("files_list, expected", test_data)
def test_merge_sorted_files(files_list, expected):
    assert list(merge_sorted_files(files_list)) == expected
