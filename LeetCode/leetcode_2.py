# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        num_l1 = 0
        num_l2 = 0
        power = 1
        while l1 != None:
            num_l1 += l1.val * power
            l1 = l1.next
            power *= 10
        power = 1
        while l2 != None:
            num_l2 += l2.val * power
            l2 = l2.next
            power *= 10
        
        power = 1
        sum_l1l2 = num_l1 + num_l2
        l3 = ListNode(sum_l1l2 % 10)
        sum_l1l2 //= 10
        temp = l3
        while sum_l1l2 != 0:
            temp.next = ListNode(sum_l1l2 % 10)
            sum_l1l2 //= 10
            temp = temp.next

        return l3