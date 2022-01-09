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


def process_string(input_str: str):
    """ function emulates backspace processing
    using stack-like behavior"""
    result = []
    for symbol in input_str:
        # 'backspace' found
        if symbol == "#":
            # popping last item from 'stack'
            # if it isn't already empty
            if len(result) > 1:
                result.pop(-1)
        # 'letter' found - append it to 'stack'
        else:
            result.append(symbol)
    # return result as string
    return "".join(result)


def backspace_compare(first: str, second: str):
    """ compare processed strings """
    return process_string(first) == process_string(second)
