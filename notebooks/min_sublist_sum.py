numlist = [-6, 1, 3, -4, -2, 2, -3, 5, -7]

def min_sublist_sum(numlist):
    min_sum = numlist[0]
    for i in range(1, len(numlist)):
        