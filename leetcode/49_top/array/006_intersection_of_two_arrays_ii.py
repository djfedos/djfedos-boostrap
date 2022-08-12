def intersect(nums1: list[int], nums2: list[int]) -> list[int]:
    if len(nums2) > len(nums1):
        short_nums = nums1
        long_nums = nums2
    else:
        short_nums = nums2
        long_nums = nums1

    long_nums_dict = {}
    for num in long_nums:
        if num not in long_nums_dict:
            long_nums_dict[num] = 1
        else:
            long_nums_dict[num] += 1

    intersection = []
    for num in short_nums:
        if num in long_nums_dict:
            intersection.append(num)
            if long_nums_dict[num] == 1:
                long_nums_dict.pop(num)
            else:
                long_nums_dict[num] -= 1

    return intersection

if __name__ == '__main__':
    print(intersect([1,2,2,1], [2,2]))
    print(intersect([4,9,5], [9,4,9,8,4]))

