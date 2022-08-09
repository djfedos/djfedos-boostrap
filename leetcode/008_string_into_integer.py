def myAtoi(s: str) -> int:
    s = s.strip()
    negative = False
    digits_start = 0
    if s == '':
        return 0
    if not s[0].isdigit():
        if s[0] == '-':
            negative = True
            digits_start = 1
        elif s[0] == '+':
            negative = False
            digits_start = 1
        else:
            return 0
    int_list = []
    num = 0
    pos = digits_start
    while pos < len(s):
        if s[pos].isdigit():
            int_list.append(s[pos])
            pos += 1
        else:
            break
    if int_list == []:
        return 0
    int_str = ''.join(int_list)
    if negative:
        num = -int(int_str)
    else:
        num = int(int_str)
    if num > 2 ** 31 - 1:
        num = 2 ** 31 - 1
    if num < - 2 ** 31:
        num = - 2 ** 31
    return num


if __name__ == '__main__':
    r = myAtoi('     -42')
    print(r)
    assert r == -42
    r = myAtoi('4193 with words')
    print(r)
    assert r == 4193
    r = myAtoi("-91283472332")
    print(r)
    assert r == -2147483648
