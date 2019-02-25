"""
Given a binary tree, return all root-to-leaf paths.

Note: A leaf is a node with no children.

Example:

Input:

   1
 /   \
2     3
 \
  5

Output: ["1->2->5", "1->3"]

Explanation: All root-to-leaf paths are: 1->2->5, 1->3
"""
class TreeNode:
    def __init__(self, x, left=None, right=None):
        self.val = x
        self.left = left
        self.right = right


def binary_tree_paths(root):
    """Runtime: 40 ms, faster than 98.52% of Python3 online submissions for Binary Tree Paths.
"""
    if root == None:
        return []
    string = ""
    arr = []
    return foo(root, string, arr)

def foo(root, string, arr):

    if root.left == None and root.right == None:
        s = string + str(root.val)
        arr.append(s)

    if root.left != None:
        foo(root.left, string + str(root.val) + "->", arr)
    if root.right != None:
        foo(root.right, string + str(root.val) + "->", arr)

    return arr


root = TreeNode(1, TreeNode(2, None, TreeNode(5)), TreeNode(3))
result = binary_tree_paths(root)
print(result)