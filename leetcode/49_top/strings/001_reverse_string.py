def reverseString(s: List[str]) -> None:
    if len(s) <= 1:
        pass
    i = 0
    while i < len(s) // 2:
        s[i], s[- i - 1] = s[- i - 1], s[i]
        i += 1
