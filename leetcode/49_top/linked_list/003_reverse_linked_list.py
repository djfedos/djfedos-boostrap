def reverseList(head: Optional[ListNode]) -> Optional[ListNode]:
    if head is None:
        return None
    if head.next is None:
        return head
    stacklist = []
    cur = head
    while cur is not None:
        stacklist.append(cur.val)
        cur = cur.next
    new_head = ListNode(stacklist.pop())
    cur = new_head
    for _ in range(len(stacklist) - 1):
        cur.next = ListNode(stacklist.pop())
        cur = cur.next
    cur.next = head
    head.next = None
    return new_head
