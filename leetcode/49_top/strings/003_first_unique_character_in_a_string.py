def firstUniqChar(s: str) -> int:
    unique = {}
    familiar = set()
    for pos in range(len(s)):
        char = s[pos]
        if char not in unique and char not in familiar:
            unique[char] = pos
        elif char in unique:
            unique.pop(char)
            familiar.add(char)
    if unique == {}:
        return -1
    else:
        return list(unique.values())[0]

if __name__ == "__main__":
    print(firstUniqChar("loveleetcode"))
