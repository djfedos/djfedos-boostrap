#%%

class TrieNode:
    def __init__(self):
        self.children = {}
        self.isWordEnd = False


class Trie:
    def __init__(self):
        self.root = TrieNode()


    def insert(self, word: str):
        cur = self.root
        for char in word:
            if char not in cur.children:
                cur.children[char] = TrieNode()
            cur = cur.children[char]
        cur.isWordEnd = True


    def search(self, word: str):
        cur = self.root

        for char in word:
            if char not in cur.children:
                return False
            cur = cur.children[char]
        if cur.isWordEnd:
            return True
        else:
            return False


    def starts_with(self, word: str):
        cur = self.root

        for char in word:
            if char not in cur.children:
                return False
            cur = cur.children[char]
        return True


    # def word_list_out(self):
    #     cur = self.root
    #     word_list = []
    #     word = ""
    #     forknodes = {}
    #     if cur.isWordEnd:
    #         word_list.append(word)
    #     if len(cur.children) == 1:
    #         cur = cur.children[0]
    #         word.append(cur)
    #     elif len(cur.children) == 0:
    #         word = ""
    #         cur = self.root
    #     else:
    #         if cur not in forknodes:
    #             forknodes[cur] = iter(cur.children)


examlpe_trie = Trie()

examlpe_trie.insert('marsaba')

print(examlpe_trie.starts_with('ma'))

print(examlpe_trie.starts_with('sw'))

print(examlpe_trie.search('marsaba'))

print(examlpe_trie.starts_with('marsaba'))

#%%
