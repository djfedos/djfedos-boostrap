def lengthOfLongestSubstring(s: str) -> int:
    familiar = {}
    count = 0
    substring_length = 0
    longest = 0
    if len(s) == 0:
        return 0
    for pos, char in enumerate(s):
        if char not in familiar:
            familiar[char] = pos
            count += 1
        else:
            substring_length = count
            prev = familiar[char]
            count = pos - prev
            familiar.clear()
            for index in range(prev, pos + 1):
                familiar[s[index]] = index
        if substring_length > longest:
            longest = substring_length
    if longest > count:
        return longest
    else:
        return count


if __name__ == '__main__':
    print(lengthOfLongestSubstring("bbbbbalsmx"))
    print(lengthOfLongestSubstring("abcabcbb"))
    print(lengthOfLongestSubstring("babbbb1a_bb"))
    print(lengthOfLongestSubstring("pwwkew"))
    print(lengthOfLongestSubstring("dvdf"))
