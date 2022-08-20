class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


node00 = ListNode(2)
node01 = ListNode(0)
node02 = ListNode(1)
node03 = ListNode(3)

node00.next = node01
node01.next = node02
node02.next = node03


def deleteNode(node):
    node.val = node.next.val
    if node.next.next is None:
        node.next = None
    else:
        node.next = node.next.next

if __name__ == '__main__':
    deleteNode(node00)
