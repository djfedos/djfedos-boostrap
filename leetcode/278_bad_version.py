def isBadVersion(i: int):
    if i == 3:
        return True
    else:
        return False


def firstBadVersion(self, n: int) -> int:
    left = 1
    right = n
    first_bad = n

    while right >= left:
        mid = left + (right - left) // 2
        if mid >= n:
            break
        if isBadVersion(mid):
            first_bad = mid
            right = mid - 1
        else:
            left = mid + 1

    return first_bad




if __name__ == '__main__':
    print(search(pile, 7432))