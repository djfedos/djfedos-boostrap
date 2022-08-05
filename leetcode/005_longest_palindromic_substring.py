def longestPalindrome(s: str):
    l = len(s)
    for window_size in range(l, 0, -1):
        for start in range(0, l - window_size + 1):
            string_slice = s[start:start+window_size]
            if is_palindrome(string_slice):
                return string_slice

# worst case scenario O(n^3) time complexity due to nested loops above and another one in is_palindrome
# this code works but too slowly to be accepted on leetcode

def is_palindrome(st):
    l = len(st)
    for pos in range(l//2):
        if st[pos] != st[l - 1 - pos]:
            return False
    return True

if __name__ == '__main__':
    # print(longestPalindrome("babad"))
    # print(longestPalindrome('cbbd'))
    # print(longestPalindrome('abb'))
    # print(is_palindrome('gohangasalamiimalasagnahog'))
    print(longestPalindrome("jcwwnkwiajicysmdueefqjnrokunucidhgkswbgjkkrujkxkxeanrpjvpliomxztalhmvcldnqmkslkprhgtwlnsnygbzdvtdbsdzsdjggzgmhogknpfhtgjmclrkgfqdbiagwrqqcnagosnqrnpapxfrtrhzlyhszdtgkqggmewqmwugrbufiwfvtjhczqgcwpcyjioeacggiwyinpkyxrpxhglrtojgjmmswxnvirfsrbhmpqgjyyagjqfwkqkjkumywvgfutmiwihwnnhbfxcijaoiyxbdnrckexqfhsmmxflaneccyaoqoxfbaylcvvpfafsikebzcdufvhluldguwsmrtjaljpcjestranfrvgvytozxpcvnwquhnsxlmzkehwopgxvifajmrlwqiqylgxibnypxwpkggxevyfoxywfsfpjbzfxxysgxgwxrzkwdqlkrpajlltzqfqshdokibakkhydizsgwbygqulljqmtxkwepitsukwjlrrmsjptwabtlqytprkkuxtqdmptctkfabxsohrfrqvrbjfbppfkpthosveoppiywkkuoasefviegormlqkqlbhnhblkmglxcbszblfipsyumcrjrkrnzplkveznbtdbtlcptgswhiqsjugqrvujkzuwvoxbjremyxqqzxkgerhgtidsefyemtmstsznvgohexdgetqbhrxaomzsamapxhjibfvtbquhowyrwyxthpwvmfyyqsyibemnfbwkddtyoijzwfxhossylygxmnznpegtgvlrsreepkrcdgbujkghrgtsxwlvxrgrqxnvgqkppbkrxjupjfjcsfzepdemaulfetn"))