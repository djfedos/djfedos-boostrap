def searchInsert(nums: list[int], target: int) -> int:
    left = 0
    right = len(nums) - 1

    if target < nums[0]:
        return 0
    if target > nums[right]:
        return right

    while right > left:
        mid = left + (right - left) // 2
        if mid >= len(nums):
            return right - 1
        if nums[mid] == target:
            return mid
        elif nums[mid] > target:
            right = mid - 1
        else:
            left = mid + 1

    else:
        return mid


tl1 = [1,3,5,6] # 2
tl2 = [1,3] # 2



if __name__ == '__main__':
    print(searchInsert(tl1, 2))