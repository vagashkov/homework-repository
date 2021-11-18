from io import StringIO

from _pytest.monkeypatch import MonkeyPatch

from homework3.task1 import timed_lru_cache

monkeypatch = MonkeyPatch()
# preparing some inputs
test_inputs = StringIO('12\n')
monkeypatch.setattr('sys.stdin', test_inputs)


def test_timed_lru_cache(monkeypatch):
    def f():
        print("f called")
        return input('? ')

    # building cached function
    cached = timed_lru_cache(f, 2)
    assert cached() == '12'
