def lengthOfLongestSubstring(s: str) -> int:
    if len(s) == 0:
        return 0
    map = {}
    start = 0
    max_length = 0
    for pos in range(len(s)):
        char = s[pos]
        if char in map and start <= map[char]:
            start = map[char] + 1
        else:
            max_length = max(max_length, pos - start + 1)
        map[char] = pos
    return max_length

if __name__ == '__main__':
    print(lengthOfLongestSubstring("bbbbbalsmx"))
    print(lengthOfLongestSubstring("abcabcbb"))
    print(lengthOfLongestSubstring("babbbb1a_bb"))
    print(lengthOfLongestSubstring("pwwkew"))
    print(lengthOfLongestSubstring("dvdf"))
