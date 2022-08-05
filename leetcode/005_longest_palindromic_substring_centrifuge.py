def longestPalindrome(s: str):
    l = len(s)
    if l == 0:
        return ''
    palindrome = s[0]
    for pos in range(l):
        odd = palindrome_center(s, pos - 1, pos + 1)
        even = palindrome_center(s, pos, pos + 1)
        palindrome = max(palindrome, odd, even, key=len)
    return palindrome

def palindrome_center(st, left, right):
    palindrome_found = False
    while left >= 0 and right < len(st) and st[left] == st[right]:
        left -= 1
        right += 1
        palindrome_found = True
    if palindrome_found:
        return st[left+1:right]
    else:
        return ''

# works fine, faster than 92% of leetcode solutions of this problem



if __name__ == '__main__':
    print(longestPalindrome("babad"))
    print(longestPalindrome('cbbd'))
    print(longestPalindrome('abb'))
    print(longestPalindrome('gohangasalamiimalasagnahog'))
    print(longestPalindrome("jcwwnkwiajicysmdueefqjnrokunucidhgkswbgjkkrujkxkxeanrpjvpliomxztalhmvcldnqmkslkprhgtwlnsnygbzdvtdbsdzsdjggzgmhogknpfhtgjmclrkgfqdbiagwrqqcnagosnqrnpapxfrtrhzlyhszdtgkqggmewqmwugrbufiwfvtjhczqgcwpcyjioeacggiwyinpkyxrpxhglrtojgjmmswxnvirfsrbhmpqgjyyagjqfwkqkjkumywvgfutmiwihwnnhbfxcijaoiyxbdnrckexqfhsmmxflaneccyaoqoxfbaylcvvpfafsikebzcdufvhluldguwsmrtjaljpcjestranfrvgvytozxpcvnwquhnsxlmzkehwopgxvifajmrlwqiqylgxibnypxwpkggxevyfoxywfsfpjbzfxxysgxgwxrzkwdqlkrpajlltzqfqshdokibakkhydizsgwbygqulljqmtxkwepitsukwjlrrmsjptwabtlqytprkkuxtqdmptctkfabxsohrfrqvrbjfbppfkpthosveoppiywkkuoasefviegormlqkqlbhnhblkmglxcbszblfipsyumcrjrkrnzplkveznbtdbtlcptgswhiqsjugqrvujkzuwvoxbjremyxqqzxkgerhgtidsefyemtmstsznvgohexdgetqbhrxaomzsamapxhjibfvtbquhowyrwyxthpwvmfyyqsyibemnfbwkddtyoijzwfxhossylygxmnznpegtgvlrsreepkrcdgbujkghrgtsxwlvxrgrqxnvgqkppbkrxjupjfjcsfzepdemaulfetn"))