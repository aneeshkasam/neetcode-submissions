# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution: 
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if p is None and q is None:
            return True 
        elif p is not None and q is None:
            return False
        elif p is None and q is not None:
            return False
        else:
            if p.val != q.val:
                return False
            if self.isSameTree(p.left, q.left) == False:
                return False
            if self.isSameTree(p.right, q.right) == False:
                return False
        return True  
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if root is None and subRoot is None:
            return True
        elif root is None or subRoot is None: 
            return False
        else:
            if root.val == subRoot.val:
                if self.isSameTree(root, subRoot) == True:
                    return True
                else:
                    if self.isSubtree(root.left, subRoot) == False and self.isSubtree(root.right, subRoot) == False:
                        return False

            else:
                if self.isSubtree(root.left, subRoot) == False and self.isSubtree(root.right, subRoot) == False:
                    return False


        return True