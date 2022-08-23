# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        check = []
        while head is not None:
            check.append(head.val)
            head = head.next
        left = 0
        right = len(check) - 1
        while left < right:
            if check[left] == check[right]:
                left += 1
                right -= 1
            else:
                return False
        return True
                