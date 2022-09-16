# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        tmp = head
        res = head
        cnt = 0
        while tmp.next != None:
            cnt += 1
            tmp = tmp.next
            
        tmp = cnt
        reshead = res
            
        if cnt == 0:
            return None
        
        if cnt == n:
            if res.next.next:
                res.next = res.next.next
            else:
                res.next = None
            return res
        if cnt+1 == n:
            return res.next
        
        print(cnt)
            
        for i in range(cnt-n):
            res = res.next
        
        try:
            res.next = res.next.next
        except AttributeError:
            res.next = None
        
        return reshead