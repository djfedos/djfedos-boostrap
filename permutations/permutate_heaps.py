# Heap's algorithm from this article: https://www.baeldung.com/cs/array-generate-all-permutations
# also the Wikipedia article was very useful: https://en.wikipedia.org/wiki/Heap%27s_algorithm


from json import dumps
import os


def swap(lts_in, i, j):
    lts_in[i], lts_in[j] = lts_in[j], lts_in[i] 


def permutate(perm):

    if isinstance(perm, int):
        perm = str(perm)
    perm = list(perm)


    l = len(perm)
    c = [0 for i in range(l)]  # this list stores the state of the algorithm

    print(perm)

    # here I add an output to the file, mostly for the tests
    # if there is a leftover output file from previous runs, we delete it now
    if os.path.isfile('./perm_out.json'):
        os.remove('./perm_out.json')

    with open('./perm_out.json', 'a') as perm_out:
        perm_out.write('[')
        perm_out.write(dumps(perm))
        perm_out.write(', ')
    
    i = 0
    while i < l:
        if c[i] < i:
            if (i % 2) == 0:  # on the even step we swap i-th element with first
                swap(perm, 0, i)
            else:
                swap(perm, c[i], i)  # on the odd step we swap i-th element with the one numbered in c list
            print(perm)

            # here I add an output to file for a test
            with open('./perm_out.json', 'a') as perm_out:
                perm_out.write(dumps(perm))
                perm_out.write(', ')
            
            c[i] += 1
            i = 0
        else:
            c[i] = 0
            i += 1


    # to wrap an output into the JSON parsable list, we do some hacks here
    with open('./perm_out.json', 'rb+') as perm_out:
        perm_out.seek(-2, os.SEEK_END)
        perm_out.truncate()

    with open('./perm_out.json', 'a') as perm_out:
        perm_out.write(']')    

# that's how we can pass a source charlist into our program: 
    
    # python permutate_heaps "[l, i, s, t]"
    # python permutate_heaps "list"
    # python permutate_heaps list

    # python permutate_heaps "[1, 2, 3, 4]"
    # python permutate_heaps "1234"
    # python permutate_heaps 1234

# python permutate_heaps [l, i, s, t] or python permutate_heaps [1, 2, 3, 4] will not do
# because spaces separate the arguments in the command line

if __name__== '__main__':
    import fire
    fire.Fire(permutate)
