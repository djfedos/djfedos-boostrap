def convert(s: str, numRows: int) -> str:
    rows = {}
    for i in range(1, numRows+1):
        rows[i] = []
    current_row = 0
    forward = True
    pos = 0
    if numRows == 1:
        return s
    # while True here dramatically increases the speed
    # originally I've written while pos < len(s) here, but with breaks that I need here anyway this condition became redundant
    while True:
        if forward:
            current_row += 1
            rows[current_row].append(s[pos])
            if current_row == numRows:
                forward = False
            pos += 1
            if pos == len(s):
                break
        if not forward:
            current_row -= 1
            rows[current_row].append(s[pos])
            if current_row == 1:
                forward = True
            pos += 1
            if pos == len(s):
                break
    result = [''.join(rows[i]) for i in range(1, numRows+1)]
    return ''.join(result)


if __name__ == '__main__':
    print(convert('PAYPALISHIRING', 3))
    assert len(convert('PAYPALISHIRING', 3)) == len('PAYPALISHIRING')
    assert convert('PAYPALISHIRING', 3) == "PAHNAPLSIIGYIR"
    print(convert("PAYPALISHIRING", 4))
    assert len(convert("PAYPALISHIRING", 4)) == len('PAYPALISHIRING')
    assert convert("PAYPALISHIRING", 4) == 'PINALSIGYAHRPI'
    print(convert('A', 1))
    print(convert('AB', 1))



