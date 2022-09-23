class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


node04 = TreeNode(7)
node03 = TreeNode(15)
node01 = TreeNode(9)
node02 = TreeNode(20, node03, node04)
node00 = TreeNode(3, node01, node02)

node11 = TreeNode(2)
node10 = TreeNode(1, node11)


def maxDepth(root: TreeNode) -> int:
    if root is None:
        return 0

    path = [root]
    familiar = set()
    familiar.add(None)
    cur = root
    max_depth = 0

    while path:
        if cur is None or (cur.left in familiar and cur.right in familiar):
            cur = path.pop()
        if cur.left not in familiar:
            path.append(cur)
            cur = cur.left
            familiar.add(cur)
        elif cur.right not in familiar:
            path.append(cur)
            cur = cur.right
            familiar.add(cur)

        if len(path) > max_depth:
            max_depth = len(path)

    return max_depth


if __name__ == '__main__':
    print(maxDepth(node00))
