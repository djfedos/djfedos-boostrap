def isPalindrome(s: str) -> bool:
    slist = []
    for char in s:
        if char.isalnum():
            if char.isupper():
                slist.append(char.lower())
            else:
                slist.append(char)

    if len(slist) <= 1:
        return True
    for pos in range(len(slist)//2):
        if slist[pos] != slist[-1 -pos]:
            return False
    return True
