def plusOne(digits: list[int]) -> list[int]:
    pos = len(digits) - 1
    while pos > 0:
        if digits[pos] == 9:
            digits[pos] = 0
            pos -= 1
        else:
            digits[pos] += 1
            return digits
    if digits[0] == 9:
        digits[0] = 0
        digits.insert(0, 1)
    else:
        digits[0] += 1
    return digits

if __name__ == '__main__':
    print(plusOne([9]))
