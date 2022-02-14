# this appeared to be a kind of file operation and serialization tutorial
# I'm not happy with it, though I may be will eventually complete it 

# working with files according to this video tutorial: https://youtu.be/Uh2ebFW8OYM
# JSON serialization/deserialization follows this video tutorial: https://youtu.be/9N6a-VLBa2I

import json
from os import remove
from os.path import getsize

def permutate(charlist):

    # that's how we can simply input an integer number instead of list or even string, for convenience
    if isinstance(charlist, int):
        charlist = str(charlist)
    
    with open('heads_and_tails.json', 'w') as heads_and_tails:
        head_and_tail = [[], charlist]
        head_and_tail_json = json.dumps(head_and_tail)
        heads_and_tails.write(head_and_tail_json)


    def branching():
        with open('heads_and_tails.json', 'r') as heads_and_tails:
            for line in heads_and_tails:
                head_and_tail = json.loads(line)
                head, tail = head_and_tail[0]
                
                if not tail:
                    with open('anagrams.json', 'a') as anagrams:
                        anagrams.write(f"{head}\n")
                else:
                    for char_pos in range(len(tail)):
                        new_head = head.copy()
                        new_head.append(tail[char_pos])
                        new_tail = tail[:char_pos] + tail[char_pos + 1:]
                        new_head_and_tail = [new_head, new_tail]
                        new_head_and_tail_json = json.dumps(new_head_and_tail)
                        with open('new_heads_and_tails.json', 'a') as new_heads_and_tails:
                            new_heads_and_tails.write(new_head_and_tail_json)
                
        with open('new_heads_and_tails.json', 'r') as new_heads_and_tails:
            with open('heads_and_tails.json', 'w') as heads_and_tails:
                heads_and_tails.truncate(0)
                for line in new_heads_and_tails:
                    heads_and_tails.write(line)
        
        remove('new_heads_and_tails.json')

        if getsize('heads_and_tails.json'):
            branching()


    branching()

    for num, anagram in enumerate(anagrams, 1):
        print(num, anagram)


permutate([1, 2, 3, 4])

# that's how we pass a source charlist into our program: python perm-brute-tree.py "[e, x, a, m, p, l, e]"
# if __name__== '__main__':
#     import fire
#     fire.Fire(permutate)