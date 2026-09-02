# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if head == None or head.next == None:
            return
        p1 = head
        p2 = head.next

        while p2 != None and p2.next != None:
            p1 = p1.next
            p2 = p2.next.next
        
        #now p1 is the middle point 
        p2 = p1.next
        p1.next = None
        p1 = head

        #p1 is first half and p2 is second half now
        dupPointer = p2.next
        p2.next = None
        while dupPointer != None:
            temp = dupPointer.next
            dupPointer.next = p2
            p2 = dupPointer
            dupPointer = temp

        #now that the list is reversed we need to do reordering
        while p1 != None and p2 != None:
            temp1 = p1.next
            temp2 = p2.next
            p1.next = p2
            p2.next = temp1
            p1 = temp1
            p2 = temp2
        

        return 



