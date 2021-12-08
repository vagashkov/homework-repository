"""
Write a context manager, that suppresses passed exception.
Do it both ways: as a class and as a generator.
>>> with supressor(IndexError):
...    [][2]
"""
from contextlib import AbstractContextManager, contextmanager


@contextmanager
def supressor(sequence, index):
    """ context manager as a generator"""
    try:
        yield sequence[index]
    # supressing only IndexError exceptions
    except IndexError:
        yield None


class IndexErrorSupressor(AbstractContextManager):
    def __exit__(self, exc_type, exc_value, traceback):
        """ __exit__ method checks for exceptions occured
        and processed it, returning True (or it will be escalated
        further) """
        if isinstance(exc_value, IndexError):
            # handlig IndexError here
            print("IndexError exception intercepted")
            return True
