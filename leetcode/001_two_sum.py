def twoSum(nums: list[int], target: int) -> list[int]:
    l = len(nums)
    for i in range(l-1):
        for j in range(i+1, l):
            if nums[i] + nums[j] == target:
                return [i,j]
    return None


if __name__ == "__main__":
    # print(twoSum([2,7,11,15], 9))
    # print(twoSum([4, 1, 3], 7))
    # print(twoSum([3, 2, 4], 6))
    print(twoSum([3, 3], 6))

