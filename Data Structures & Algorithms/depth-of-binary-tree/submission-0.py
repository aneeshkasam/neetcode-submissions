# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        finalDepth = 0
        leftDepth = 0
        rightDepth = 0
        if not root:
            return 0
        if root.left is None and root.right is None:
            return 1
        
        #finding the final depth of tree

        if root.left is not None:
            leftDepth = self.maxDepth(root.left)
        if root.right is not None:
            rightDepth = self.maxDepth(root.right)
        finalDepth = 1 + max(leftDepth, rightDepth)
        return finalDepth