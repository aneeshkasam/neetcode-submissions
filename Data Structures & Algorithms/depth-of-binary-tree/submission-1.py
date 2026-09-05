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
        
        #finding the final depth of tree
        leftDepth = self.maxDepth(root.left)
        rightDepth = self.maxDepth(root.right)
        finalDepth = 1 + max(leftDepth, rightDepth)
        return finalDepth