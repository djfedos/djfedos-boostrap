class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


node00 = ListNode(1)
node01 = ListNode(2)
node02 = ListNode(4)

node00.next = node01
node01.next = node02


node10 = ListNode(1)
node11 = ListNode(3)
node12 = ListNode(4)

node10.next = node11
node11.next = node12


def mergeTwoLists(list1, list2):
    if list1 is None and list2 is None:
        return None
    if list1 is None:
        return list2
    if list2 is None:
        return list1
    cur1 = min(list1, list2, key=lambda x: x.val)
    head = cur1
    if cur1 == list1:
        cur2 = list2
    else:
        cur2 = list1
    while cur1.next is not None:
        cur_buffer = max(cur2, cur1.next, key=lambda x: x.val)
        if cur_buffer == cur1.next:
            cur1.next = cur2
        cur2 = cur_buffer
        cur1 = cur1.next
    if cur1.next is None:
        cur1.next = cur2
    return head

if __name__ == '__main__':
    print(mergeTwoLists(node00, node10))
