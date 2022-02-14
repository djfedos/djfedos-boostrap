#  working with files according to this video tutorial: https://youtu.be/Uh2ebFW8OYM

import json
from os import remove
from os.path import getsize

def permutate(charlist):

    # that's how we can simply input an integer number instead of list or even string, for convenience
    if isinstance(charlist, int):
        charlist = str(charlist)
    
    with open('heads_and_tails.txt', 'w') as heads_and_tails:
        heads_and_tails.write(f'[]; {charlist}')

    # TODO:
    # the idea of the memory efficient version is to write heads_and_tails to the file
    # and to read them from the file as needed
    # and to put out anagrams (no tail, head only) one by one, using print() and/or to the file as well
    # by the way it would be nice to eliminate deep recursion due to maximum recursion depth in Python


    def branching():
        with open('heads_and_tails.txt', 'r') as heads_and_tails:
            for line in heads_and_tails:
                head_and_tail = line.split('; ')
                head_str, tail_str = head_and_tail
                if head_str == '[]':
                   head = []
                else:
                    head = head_str.strip('[]').split(', ')
                tail = tail_str.strip('[]').split(', ')

                if not tail:
                    with open('anagrams.txt', 'a') as anagrams:
                        anagrams.write(f"{head}\n")
                else:
                    for char_pos in range(len(tail)):
                        new_head = head.copy()
                        new_head.append(tail[char_pos])
                        new_tail = tail[:char_pos] + tail[char_pos + 1:]
                        with open('new_heads_and_tails.txt', 'a') as new_heads_and_tails:
                            new_heads_and_tails.write(f"{new_head}; {new_tail}\n")
                
        with open('new_heads_and_tails.txt', 'r') as new_heads_and_tails:
            with open('heads_and_tails.txt', 'w') as heads_and_tails:
                heads_and_tails.truncate(0)
                for line in new_heads_and_tails:
                    heads_and_tails.write(line)
        
        remove('new_heads_and_tails.txt')

        if getsize('heads_and_tails.txt'):
            branching()


    branching()

    for num, anagram in enumerate(anagrams, 1):
        print(num, anagram)


permutate([1, 2, 3, 4])

# that's how we pass a source charlist into our program: python perm-brute-tree.py "[e, x, a, m, p, l, e]"
# if __name__== '__main__':
#     import fire
#     fire.Fire(permutate)