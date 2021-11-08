def check_power_of_2(a: int) -> bool:
    # negative numbers and zero are non-powers of 2
    if a < 1:
        return False
    # continously divide number by two
    while a != 1:
        # we have remainder so number
        # cannot be power of 2
        if a % 2:
            return False
        # move fowrard
        a = a // 2
    # still no remainder - it is really power of 2
    return True
