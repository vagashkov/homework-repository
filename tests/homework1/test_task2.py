import pytest

from homework1.task2 import check_fibonacci

zero_based_seq = [
            0,
            1,
            1,
            2,
            3,
            5,
            8,
            13,
            21,
            34,
            55,
            89,
            144,
            233,
            377,
            610,
            987,
            1597,
            2584,
            4181,
            6765,
        ]

non_zero_based_seq = [
            14472334024676221,
            23416728348467685,
            37889062373143906,
            61305790721611591,
            99194853094755497,
            160500643816367088,
            259695496911122585,
            420196140727489673,
            679891637638612258,
            1100087778366101931,
            1779979416004714189,
            2880067194370816120,
            4660046610375530309,
            7540113804746346429,
            12200160415121876738,
            19740274219868223167,
            31940434634990099905,
            51680708854858323072,
            83621143489848422977,
            135301852344706746049,
            218922995834555169026,
            354224848179261915075,
        ]

test_data = [
    # False: too short sequence
    ([1, 2], False),
    # False: non-integer found in sequence
    ([0, 1, 1, "c", 3, 5], False),
    # False: negative int found in sequence
    ([0, 1, 1, -2, 3, 5], False),
    # True: first Fibonacci sequence sample
    # (zero-based)
    (zero_based_seq, True),
    # True: second Fibonacci sequence sample
    # (non-zero-based)
    (non_zero_based_seq, True)]


@pytest.mark.parametrize("sequence, expected", test_data)
def test_check_fibonacci(sequence, expected):
    """Testing all the prepared sequences"""
    assert check_fibonacci(sequence) == expected
