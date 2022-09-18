# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        start = ListNode(0, dummy)
        
        while list1 != None or list2 != None:
            if list1 == None:
                dummy.next = list2
                dummy = dummy.next
                list2 = list2.next
                
            elif list2 == None:
                dummy.next = list1
                dummy = dummy.next
                list1 = list1.next
                
            elif list1.val >= list2.val:
                dummy.next = list2
                dummy = dummy.next
                list2 = list2.next
                
            else:
                dummy.next = list1
                dummy = dummy.next
                list1 = list1.next
        
        return start.next.next