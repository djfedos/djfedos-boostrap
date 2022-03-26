# According to the video tutorial here: https://youtu.be/oBt53YbR9Kk

#%%
# Fibonacci numbers, brute force approach

def fib_brute(n):
    if n <= 2:
        return 1
    else:
        return fib_brute(n - 1) + fib_brute(n - 2)

# to evaluate complexity it's useful to draw a solution graph, in this case tree
"""
O(2^n) time complexity
O(n) space complexity
"""

fib_brute(9)

#%%
# Fibonacci numbers, memoization

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

# %%
# Rectangle grid travel: how many ways do you have from top left corner to the bottom right, if you can only step down or right?
# brute force approach
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
O(n^(w+h)) time complexity
O(w+h) space complexity
"""

grid_travel_brute(9, 9)

# %%
# the same problem tackled with memoization

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
# Can the numbers from the given array sum up to the target sum? This function should check this
# brute force implementation

def can_sum_brute(target, nums):
    if target == 0:
        return True
    if target < 0:
        return False
    for num in nums:
        if can_sum_brute(target-num, nums):
            return True
    return False

"""
O(n^m) time complexity, where n is len(nums), m is target
O(m) space complexity
"""

# can_sum_brute(250, [7, 14])

# %%
# and now with memoization

def can_sum(target, nums, memo={}):
    if target in memo:
        return memo[target]
    if target == 0:
        return True
    if target < 0:
        return False
    for num in nums:
        memo[target-num] = can_sum(target-num, nums, memo=memo)
        if memo[target-num]:    
            return True
    return False

"""
O(n^m) time complexity, where n is len(nums), m is target
O(m) space complexity
"""

print(can_sum(3000, [7, 14]))
print(can_sum(51, [10, 21]))

# %%
# Benchmark to measure function running time
# uncomment to enable

# import time
# from tkinter import N
# for func in can_sum_brute, can_sum:
#     start_time = time.time()
#     func(250, [7, 14])
#     duration = time.time() - start_time
#     print(f'{func.__name__} runs {duration:0.5f} s')

# on my machine can_sum_brute() takes about 6 s to run
# and can_sum() runs in about 0.00002 s with the same input

# %%
# What is the exact set of numbers to yeild the target sum?
# brute force approach

def how_sum_brute(target, nums):
    if target == 0:
        return []
    if target < 0:
        return None
    for num in nums:
        delta = target - num
        path = how_sum_brute(delta, nums)
        if path != None:
            path.append(num)
            return path
    return None

"""
O(n^m*m) time complexity, where n is len(nums), m is target
O(m) space complexity
"""

print(how_sum_brute(21, [14, 7]))
print(how_sum_brute(51, [11, 10])) 

# %%
# the same task tackled with memoization
# this time with a special kickstart function to reset the memo on each non-recursive call

def how_sum_memo(target, nums, memo):
    if target in memo:
        return memo[target]
    if target == 0:
        return []
    if target < 0:
        return None
    for num in nums:
        delta = target - num
        path = how_sum_memo(delta, nums, memo=memo)
        if path != None:
            path.append(num)
            memo[target] = path
            return memo[target]
    memo[target] = None
    return None

"""
O(n*m^2) time complexity
O(m^2) space complexity
"""

# this additional function is needed to kickstart the memoized function
# with the empty memo each time it's been called
# else there is always garbage stuck in the memo
def how_sum(target, nums):
    return how_sum_memo(target, nums, {})


print(how_sum(300, [7, 50, 14]))
print(how_sum(250, [7, 50, 14]))
print(how_sum(100, [7, 14]))
print(how_sum(0, [2, 1]))

# %%
# benchmark for running time of how_sum_brute() and how_sum()
# uncomment to enable

# import time
# for func in how_sum_brute, how_sum:
#     start_time = time.time()
#     print(func(250, [7, 50, 14]))
#     duration = time.time() - start_time
#     print(f'{func.__name__} runs {duration:0.5f} s')

# # how_sum_brute() takes about 14 s
# # how_sum() runs in about 0.00017 s

# %%
# How to choose the shortest possible set of the given numbers to get the target sum?
# This function will answer
# brute force approach

def best_sum_brute(target, nums):
    if target == 0:
        return []
    if target < 0:
        return None

    shortest = None
    
    for num in nums:
        delta = target - num
        path = best_sum_brute(delta, nums)
        if path != None:
            path.append(num)
            if not shortest or len(path) < len(shortest):
                shortest = path
    
    return shortest

"""
O(n^m*m) time complexity, where n is len(nums), m is target
O(m^2) space complexity
"""

print(best_sum_brute(7, [5, 3, 4, 7]))
print(best_sum_brute(8, [2, 3, 5]))
print(best_sum_brute(8, [1, 4, 5]))


# %%

def best_sum_memo(target, nums, memo={}):
    if target in memo:
        return memo[target]
    if target == 0:
        return []
    if target < 0:
        return None

    shortest = None
    
    for num in nums:
        delta = target - num
        path = best_sum_memo(delta, nums, memo=memo)
        if path != None:
            path.append(num)
            if not shortest or len(path) < len(shortest):
                shortest = path
                 
    memo[target] = shortest
    return memo[target]

# In this case memoization doesn't work even when function is called once,
# so an additional kickstarter function also doesn't help

# # this additional function is needed to kickstart the memoized function
# # with the empty memo each time it's been called
# # else there is always garbage stuck in the memo
# def best_sum(target, nums):
#     return best_sum_memo(target, nums, {})

# print(best_sum_memo(100, [1, 2, 5, 25]))
print(best_sum_memo(8, [1, 4, 5]))

# %%
