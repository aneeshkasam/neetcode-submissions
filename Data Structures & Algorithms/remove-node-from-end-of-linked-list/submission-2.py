# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        #making the fast pointer as fast as n
        if head is None: 
            return head
        if head.next is None and n == 1:
            head = None
            return head
        if head.next.next is None and n == 2:
            head = head.next
            return head
        slow = head
        p1 = head
        p2 = head
        a = n
        #set p2 place
        while a > 0:
            p2 = p2.next
            a -= 1
        
        while p2 is not None:
            slow = p1
            p1 = p1.next
            p2 = p2.next
        
        if p1 is head:
            return head.next
        #p1 is in removing node and slow is one behind p1

        slow.next = p1.next

        return head

        