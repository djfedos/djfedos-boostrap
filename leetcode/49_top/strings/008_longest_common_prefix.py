def longestCommonPrefix(strs: list[str]) -> str:
    shortest = min(strs, key=len)
    common_prefix = []
    common_letter = True
    for pos in range(len(shortest)):
        for i in range(1, len(strs)):
            if strs[0][pos] != strs[i][pos]:
                common_letter = False
        if common_letter:
            common_prefix.append(shortest[pos])
    return ''.join(common_prefix)

if __name__ == '__main__':
    print(longestCommonPrefix(["flower", "flow", "flight"]))
