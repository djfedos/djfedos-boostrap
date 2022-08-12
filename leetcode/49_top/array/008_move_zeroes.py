def moveZeroes(nums: list[int]) -> None:
    pos = 0
    count = 1
    while count < len(nums):
        if nums[pos] == 0:
            nums.pop(pos)
            nums.append(0)
        else:
            pos += 1
        count += 1
