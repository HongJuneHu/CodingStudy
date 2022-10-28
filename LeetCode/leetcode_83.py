# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        tmp = head
        try:
            while True:
                if tmp.val == tmp.next.val:
                    tmp.next = tmp.next.next
                else:
                    tmp = tmp.next
        except:
            return head