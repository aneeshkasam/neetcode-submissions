# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:   
    def sortList(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        dummy = ListNode()
        sortedList = dummy

        while list1 is not None and list2 is not None:
            if list1.val <= list2.val:
                sortedList.next = list1
                list1 = list1.next
            else:
                sortedList.next = list2
                list2 = list2.next
            sortedList = sortedList.next

        if list1 != None:
            sortedList.next = list1
                    
        if list2 != None:
            sortedList.next = list2

        return dummy.next




    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        interval = 1
        dummy = ListNode()
        FullList = dummy
        if len(lists) == 0:
            return None
        if len(lists) == 1:
            return lists[0]

        while interval < len(lists):
            i = 0
            while i + interval < len(lists):
                lists[i] = self.sortList(lists[i], lists[i + interval])
                FullList = lists[i]
                i += 2 * interval
            interval *= 2
        
        
        return FullList


