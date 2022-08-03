# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        dummy = ListNode(0, head)
        pointer_left = dummy
        pointer_right = head
        for i in range(0, n):
            pointer_right = pointer_right.next

        while pointer_right:
            pointer_right = pointer_right.next
            pointer_left = pointer_left.next

        pointer_left.next = pointer_left.next.next
        return dummy.next

    def _print_list(self, head: Optional[ListNode]):
        pointer = head
        while pointer:
            print(pointer.val)
            pointer = pointer.next