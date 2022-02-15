# Heap's algorithm from this article: https://www.baeldung.com/cs/array-generate-all-permutations
# also the Wikipedia article was very useful: https://en.wikipedia.org/wiki/Heap%27s_algorithm


def swap(lts_in, i, j):
    lts_in[i], lts_in[j] = lts_in[j], lts_in[i] 


def permutate(perm):

    if isinstance(perm, int):
        perm = str(perm)
    perm = list(perm)


    l = len(perm)
    c = [0 for i in range(l)]  # this list stores the state of the algorithm

    print(perm)
    
    i = 0
    while i < l:
        if c[i] < i:
            if (i % 2) == 0:  # on the even step we swap i-th element with first
                swap(perm, 0, i)
            else:
                swap(perm, c[i], i)  # on the odd step we swap i-th element with the one numbered in c list
            print(perm)
            c[i] += 1
            i = 0
        else:
            c[i] = 0
            i += 1


# that's how we can pass a source charlist into our program: 
    
    # python permutate_heaps "[l, i, s, t]"
    # python permutate_heaps "list"
    # python permutate_heaps list

    # python permutate_heaps "[1, 2, 3, 4]"
    # python permutate_heaps "1234"
    # python permutate_heaps 1234

# python permutate_heaps [l, i, s, t] or # python permutate_heaps [1, 2, 3, 4] will not do

if __name__== '__main__':
    import fire
    fire.Fire(permutate)
