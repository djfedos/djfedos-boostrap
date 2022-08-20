def isPalindrome(head: Optional[ListNode]) -> bool:
    if head.next is None:
        return True
    stacklist = []
    cur = head
    while cur is not None:
        stacklist.append(cur.val)
        cur = cur.next
    palindrome = True
    for pos in range(len(stacklist) // 2):
        if stacklist[pos] != stacklist[-1 - pos]:
            palindrome = False
    return palindrome
