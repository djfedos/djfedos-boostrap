def reverse(x: int) -> int:
    if x == 0:
        return 0
    while x % 10 == 0:
        x //= 10
    s = str(x)
    if x < 0:
        o = -int(s[:0:-1])
    else:
        o = int(s[::-1])
    if o <= -2 ** 31 or o >= 2 ** 31 - 1:
        return 0
    else:
        return o


