def containsDuplicate(nums: list[int]) -> bool:
    numset = set(nums)
    if len(numset) < len(nums):
        return True
    else:
        return False
