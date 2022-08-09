def findMedianSortedArrays(nums1: list[int], nums2: list[int]) -> float:
    len1 = len(nums1)
    len2 = len(nums2)
    total_len = len1 + len2

    left1 = 0
    right1 = len1

    left2 = 0
    right2 = len2

    init_split_1 = right1 // 2
    init_split_2 = right2 // 2

    if total_len % 2 == 0:
        while nums1[init_split_1 - 1] > nums2[init_split_2 + 1] or nums2[init_split_2 - 1] > nums1[init_split_1 + 1]:
            if nums1[init_split_1 - 1] > nums2[init_split_2 + 1]:
                init_split_1 = left1 - (init_split_1 - left1) // 2

            elif



        if nums1[init_split_1 - 1] < nums2[init_split_2 + 1] and nums2[init_split_2 - 1] < nums1[init_split_1 + 1]:
            return (nums1[init_split_1] + nums2[init_split_2])/2
        elif:









if __name__ == '__main__':
    r = findMedianSortedArrays([1,3][2])
    print(r)
    assert r == 2

