def twoSum(nums, target: int):
    numdict = {}

    for pos in range(len(nums)):
        if nums[pos] not in numdict:
            numdict[nums[pos]] = set([pos])
        else:
            numdict[nums[pos]].add(pos)

    for num in nums:
        if target - num in numdict:
            if target - num == num:
                if len(numdict[num]) > 1:
                    result = []
                    for _ in range(2):
                        result.append(numdict[num].pop())
                    return result
            else:
                return [numdict[num].pop(), numdict[target - num].pop()]
    return -1

# works faster than ~70% of leetcode submissions, but consumes 17,5 Mbytes of memory

if __name__ == '__main__':
    print(twoSum([2,7,11,15], 9))
    assert twoSum([2,7,11,15], 9) == [0, 1]
    print(twoSum([3,2,4], 6))
    assert twoSum([3,2,4], 6) == [1, 2]
    print(twoSum([3,3], 6))
    assert twoSum([3,3], 6) == [0, 1]


