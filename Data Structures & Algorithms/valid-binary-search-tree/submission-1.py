# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rangeHelper(self, root: Optional[TreeNode], low: float, high: float) -> bool:
        if root is None:
            return True
        if low >= root.val:
            return False
        if high <= root.val:
            return False
        
        return (self.rangeHelper(root.left, low, root.val) and self.rangeHelper(root.right, root.val, high))
        
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        return self.rangeHelper(root, float('-inf'), float('inf'))