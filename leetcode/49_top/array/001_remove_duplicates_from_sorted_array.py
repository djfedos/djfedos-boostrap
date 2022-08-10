# dirty and slow, but it passes

def removeDuplicates(nums: list[int]) -> int:
    l = len(nums)
    if l == 1:
        return 1
    pos = 0
    while pos < len(nums) - 1:
        if nums[pos] == nums[pos + 1]:
            nums.pop(pos)
            l -= 1
            if pos == l - 1:
                break
        else:
            pos += 1

    if len(nums) == 1:
        return 1

    if nums[-1] != nums[-2]:
        pos += 1

    print(nums)
    return pos

if __name__ == '__main__':
    print(removeDuplicates([1]))
    print(removeDuplicates([1,1]))
    print(removeDuplicates([1, 2]))
    print(removeDuplicates([0,0,1,1,1,2,2,3,3,4]))
    print(removeDuplicates([1, 1, 2]))
