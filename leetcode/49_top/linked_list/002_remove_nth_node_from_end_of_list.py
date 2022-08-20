def removeNthFromEnd(head: Optional[ListNode], n: int) -> Optional[ListNode]:
    sz = 0
    cur = head
    while cur is not None:
        cur = cur.next
        sz += 1
    pos = sz - n
    if pos == 0:
        return head.next
    else:
        cur = head
        while pos != 1:
            cur = cur.next
            pos -= 1
        if cur.next.next is None:
            cur.next = None
        else:
            cur.next = cur.next.next
        return head

