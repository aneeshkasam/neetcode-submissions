# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        current = dummy
        pointer1 = list1
        pointer2 = list2

        while pointer1 != None and pointer2 != None:
            if pointer1.val <= pointer2.val:
                current.next = pointer1
                pointer1 = pointer1.next
            else:
                current.next = pointer2
                pointer2 = pointer2.next
            current = current.next


        if pointer1!= None:
            current.next = pointer1
        if pointer2 != None:
            current.next = pointer2

        
        return dummy.next