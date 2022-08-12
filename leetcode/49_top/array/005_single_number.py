def singleNumber(nums: list[int]) -> int:
    known_nums = set()
    for num in nums:
        if num not in known_nums:
            known_nums.add(num)
        else:
            known_nums.remove(num)
    return known_nums.pop()

if __name__ == '__main__':
    print(singleNumber([2,2,1]))
