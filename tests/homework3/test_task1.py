from homework3.task1 import timed_lru_cache

def test_timed_lru_cache():
    # counter for chached function calls
    f_invoked = 0

    def f(input):
        nonlocal f_invoked
        # increment counter
        f_invoked += 1
        # and perform function code
        return input

    # building cached function
    cached = timed_lru_cache(f, 4)
    # call it 20 times
    for _ in range(20):
        assert cached(12) == 12
    # and check how many times it was invoked
    assert f_invoked == 5
