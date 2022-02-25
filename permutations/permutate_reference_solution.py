# this permutation program is written together with ydzvulon as a tutorial


def insert_new_char(char_list, new_char):
    list_of_lists = []
    for position in range(len(char_list) + 1):
        char_list_plus = char_list.copy()
        char_list_plus.insert(position, new_char)
        list_of_lists.append(char_list_plus)
    return list_of_lists    

def permutate(list_of_chars):
    anagrams = []
    
    if len(list_of_chars) == 0: 
        anagrams = [list_of_chars]

    else:
        new_char = list_of_chars[0]
        rest = list_of_chars[1:]

        rest_anagrams = permutate(rest)
        for anagram in rest_anagrams:
            new_anagrams = insert_new_char(anagram, new_char)
            anagrams.extend(new_anagrams)



    print(anagrams)
    return anagrams



    '''
    
    [[]] (+) 1
    [[1]] (+) 2
    [[1, 2] [2, 1]] (+) 3
    [[1, 2, 3] [2, 1, 3] [1, 3, 2] [2, 3, 1] [3, 1, 2] [3, 2, 1]]
    
    [1, 2, 3, 4] [1, 2, 4, 3] [1, 4, 2, 3] [4, 1, 2, 3]
    [2, 1, 3] ...
    [1, 3, 2]
    [2, 3, 1]
    [3, 1, 2]
    [3, 2, 1] 
    '''

if __name__== '__main__':
    import fire
    fire.Fire(permutate)
