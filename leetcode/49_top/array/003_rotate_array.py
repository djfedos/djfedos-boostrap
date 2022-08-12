def rotate(nums: list[int], k: int):
    for _ in range(k):
        buffer = nums.pop()
        nums.insert(0, buffer)

