"""
We have a file that works as key-value storage,
each line is represented as key and value
separated by = symbol, example:

name=kek
last_name=top
song_name=shadilay
power=9001

Values can be strings or integer numbers.
If a value can be treated both as a number and a string,
it is treated as number.

Write a wrapper class for this key value storage
that works like this:

storage = KeyValueStorage('path_to_file.txt')
that has its keys and values accessible
as collection items and as attributes.
Example:
storage['name'] # will be string 'kek'
storage.song_name # will be 'shadilay'
storage.power # will be integer 9001

In case of attribute clash existing
built-in attributes take precedence.
In case when value cannot be assigned
to an attribute (for example when there's
a line 1=something) ValueError should be raised.
File size is expected to be small,
you are permitted to read it entirely into memory.
"""

import os
import re


class KeyValueStorage(dict):
    """ storage wrapper key-value formatted files"""
    def __init__(self, file_path):
        # pattern for valid attribute names
        attr_name_pattern = r'[a-zA-Z_][a-zA-Z0-9_]*'
        # trying to open file
        with open(os.getcwd() + file_path, "r", encoding='utf-8-sig') as fi:
            # and walking it line by line
            for line in fi:
                key, value = line.split("=")
                # key name should be valid string
                if not re.fullmatch(attr_name_pattern, key.strip()):
                    raise ValueError
                # checking value type (int vs str)
                value = value.strip()
                value = int(value) if value.isdigit() else value
                # checking for built-in attrs name conflict
                self[key] = value

    def __getattr__(self, attr):
        """ 'translate' attribute-based access into key-based """
        return self[attr]
