# here I solve permutations from scratch to understand completely what I'm doing


def permutate(charlist):
    
    # that's how we can simply input an integer number instead of list or string, for convenience
    if isinstance(charlist, int):
        charlist = str(charlist)
    
    anagrams = []
    heads_and_tails = [[[], charlist]]

    
    def branching(heads_and_tails = heads_and_tails):
        for head_and_tail in heads_and_tails:
            head, tail = head_and_tail
            if not tail:
                anagrams.append(head)
            else:
                for char_pos in range(len(tail)):
                    new_head = head.copy()
                    new_head.append(tail[char_pos])
                    new_tail = tail[:char_pos] + tail[char_pos + 1:]
                    heads_and_tails.append([new_head, new_tail])
            heads_and_tails.remove(head_and_tail)
            if heads_and_tails:
                branching()


    branching()

    # uncomment two following lines to print anagrams and their counter
    # for num, anagram in enumerate(anagrams, 1):
    #     print(num, anagram)

    return anagrams


# that's how we can pass a source charlist into our program: 
    
    # python perm-brute-tree.py "[l, i, s, t]"
    # python perm-brute-tree.py "list"
    # python perm-brute-tree.py list

    # python perm-brute-tree.py "[1, 2, 3, 4]"
    # python perm-brute-tree.py "1234"
    # python perm-brute-tree.py 1234

# python perm-brute-tree.py [l, i, s, t] or # python perm-brute-tree.py [1, 2, 3, 4] will not do

# list of 6 or more characters will crash the program due to exceeding the maximum recursion depth

# how to put the text above into --help message?
# and how to customize Usage message?

if __name__== '__main__':
    import fire
    fire.Fire(permutate)