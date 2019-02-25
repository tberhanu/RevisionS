"""
Invert a binary tree.

Example:

Input:

     4
   /   \
  2     7
 / \   / \
1   3 6   9
Output:

     4
   /   \
  7     2
 / \   / \
9   6 3   1
"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def invertTree(root):
    """Runtime: 32 ms, faster than 100.00% of Python3 online submissions for Invert Binary Tree.
"""
    if root == None:
        return None
    tree = TreeNode(root.val)
    dummy = tree
    foo(root, tree)
    return dummy


def foo(root, tree):
    if root == None:
        return
    if root.right:
        tree.left = TreeNode(root.right.val)
        foo(root.right, tree.left)

    if root.left:
        tree.right = TreeNode(root.left.val)
        foo(root.left, tree.right)

