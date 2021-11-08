def check_power_of_2(a: int) -> bool:
    if a < 1:
        return False
    while a != 1:
        if a % 2:
            return False
        a = a // 2
    return True
