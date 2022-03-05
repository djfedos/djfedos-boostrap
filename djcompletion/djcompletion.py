def load_tokens(db_path):
    """ 
    O(n*k), n is number of tokens, k is number of chars in a token 
    """
    dictrie = {}
    with open(db_path, 'r') as tokens:
        for line in tokens:
            if line.endswith('\n'):
                line = line[0:-1]
            cur = dictrie
            for char in line:
                if char not in cur:
                    cur[char] = {}
                cur = cur[char]
            cur[None] = None
        return dictrie


def get_completions(my_db, prefix, limit=-1):
    """ 
    O(#prefix)
    """
    completions = []
    part_tree = {}  # here we store everything that goes after the prefix in our dictrie token db
    cur = my_db  # this is ou cursor
    for char in prefix:
        if char not in cur:
            return completions
        else:
            part_tree = cur[char]
        cur = cur[char]
    tails = branching(part_tree)
    for tail in tails:
        completions.append(prefix + tail)
    if limit == -1 or len(completions) < limit:
        return completions
    else:
        return completions[0:limit]
   
# in tails list we collect all the branches of the part_tree

def branching(part_tree, tail='', tails=[]):
    tail_grows = False
    if part_tree:
        for node in part_tree:
            if tail_grows:
                tail = tail[0:-1]
                tail_grows = False
            if node:
                tail += node
                tail_grows = True
            branching(part_tree[node], tail)
    else:
        tails.append(tail)
    return tails


def djcompletion_cli(my_db, prefix, limit=-1):
    my_db = load_tokens(my_db)
    return get_completions(my_db, prefix, limit)



if __name__== '__main__':
    import fire
    fire.Fire(djcompletion_cli)