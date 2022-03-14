# According to the video tutorial here: https://youtu.be/oBt53YbR9Kk

# Fibonacci numbers, brute force approach
#%%
def fib_brute(n):
    if n <= 2:
        return 1
    else:
        return fib_brute(n - 1) + fib_brute(n - 2)

# to evaluate complexity it's useful to draw a solution graph, in this case tree
"""
O(2**n) time complexity
O(n) space complexity
"""

fib_brute(9)

# Fibonacci numbers, memoization
#%%
def fib(n, memo={}):
    if n in memo:
        return memo[n]
    if n <= 2:
        memo[n] = 1
    else:
        memo[n] = fib(n-1, memo=memo) + fib(n-2, memo=memo)  # if I don't pass the memo to the recursive calls explicitly, code still works though
    return memo[n]

"""
O(n) time complexity
O(n) space complexity
"""

fib(50)

# Rectangle grid travel: how many ways do you have from top left corner to the bottom right, if you can only step down or right?
# brute force approach
# %%
# w (width) and h (height) are the dimensions of our grid. number of ways to travel depends on them
def grid_travel_brute(w, h):
    if w < 1 or h < 1:  # in this case the grid can not even exist
        return 0
    if w == 1 or h == 1:  # having one row or colomn of a grid you have only one way trough it
        return 1
    return grid_travel_brute(w - 1, h) + grid_travel_brute(w, h - 1)
# stepping right you decrease the width of the rest of the grid to travel by 1
# stepping down you decrease the height of the rest of the grid to travel by 1

"""
O(n**(w+h)) time complexity
O(w+h) space complexity
"""

grid_travel_brute(9, 9)

# the same problem tackled with memoization
# %%
def grid_travel(w, h, memo={}):
    if (w, h) in memo:
        return memo[(w, h)]
    if (h, w) in memo:       # This optimization is possible because the number of ways
        return memo[(h, w)]  # to travel the rectangle grid doesn't change when you rotate it
    if w < 1 or h < 1:       # in this case the grid can not even exist
        return 0
    if w == 1 or h == 1:
        return 1
    memo[(w, h)] = grid_travel(w - 1, h, memo=memo) + grid_travel(w, h - 1, memo=memo)
    return memo[(w, h)]

"""
O(w*hs) time complexity
O(w+h) space complexity
"""

grid_travel(18, 18)

# %%
