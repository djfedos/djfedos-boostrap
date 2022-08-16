def strStr(haystack: str, needle: str) -> int:
    if len(needle) > len(haystack):
        return -1
    if len(needle) == 0:
        return 0
    found = False
    for pos in range(len(haystack)):
        if len(haystack) - pos >= len(needle):
            if haystack[pos] == needle[0]:
                found = True
                for needle_pos in range(len(needle)):
                    if needle[needle_pos] != haystack[pos + needle_pos]:
                        found = False
            if found:
                return pos
    return -1

if __name__ == '__main__':
    print(strStr("mississippi", "issipi"))
