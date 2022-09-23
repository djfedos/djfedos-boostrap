class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

node04 = TreeNode(7)
node03 = TreeNode(3)
node02 = TreeNode(6, node03, node04)
node01 = TreeNode(4)
node00 = TreeNode(5, node01, node02)


def isValidBST(root: TreeNode) -> bool:

    def valid(node, left, rigth):
        if node >= rigth or node <= left:
            return False




if __name__ == '__main__':
    print(isValidBST(node00))
