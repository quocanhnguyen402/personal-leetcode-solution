# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        current = dummy = ListNode(0)
        plus_one = False
        while l1 or l2:   
            sum = l1.val + l2.val
            if plus_one:
                sum += 1
                plus_one = False
            if sum < 10:
                current.next = ListNode(sum,None)
            else:
                current.next = ListNode(sum%10,None)
                plus_one = True
            current = current.next
            l1 = l1.next
            l2 = l2.next
            if l1 and not l2:
                l2 = ListNode(0)
            if l2 and not l1:
                l1 = ListNode(0)
        if plus_one:
            current.next = ListNode(1)
        return dummy.next
        