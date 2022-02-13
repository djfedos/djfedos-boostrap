# here I solve permutations from scratch to understand completely what I'm doing


def permutate(charlist):
    
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

    for num, anagram in enumerate(anagrams, 1):
        print(num, anagram)


# that's how we pass a source charlist into our program: python perm-brute-tree.py "[e, x, a, m, p, l, e]"
if __name__== '__main__':
    import fire
    fire.Fire(permutate)