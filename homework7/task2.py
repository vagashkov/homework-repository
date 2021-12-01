"""
Given two strings. Return if they are equal when both are typed into
empty text editors. # means a backspace character.
Note that after backspacing an empty text, the text will continue empty.
Examples:
    Input: s = "ab#c", t = "ad#c"
    Output: True
    # Both s and t become "ac".
    Input: s = "a##c", t = "#a#c"
    Output: True
    Explanation: Both s and t become "c".
    Input: a = "a#c", t = "b"
    Output: False
    Explanation: s becomes "c" while t becomes "b".
"""


def process_backspaces(input_str: str):
    while "#" in input_str:
        # cleaning backspaces at the beginning
        if input_str[0] == "#":
            input_str = input_str[1:]
        # found # inside string - remove it with symbol to the left
        else:
            bs_index = input_str.index("#")
            input_str = input_str[: bs_index-1] + input_str[bs_index+1:]
    return input_str


def backspace_compare(first: str, second: str):
    return process_backspaces(first) == process_backspaces(second)
