def hasCycle(head) -> bool:
    if head is None or head.next is None:
        return False
    familiar = set()
    cur = head
    while cur is not None:
        if cur.next in familiar:
            return True
        familiar.add(cur)
        cur = cur.next
    return False
