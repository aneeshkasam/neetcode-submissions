# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        
        if not head or not head.next:
            return False
        left = head
        right = head.next


        while left != right and right != None and right.next != None:
            left = left.next
            right = right.next.next
        if left == right:
            index = True
        else:
            index =  False
        return index
