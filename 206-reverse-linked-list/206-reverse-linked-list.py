class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        previous = None
        while head:
            current = head
            head = current.next
            current.next = previous
            previous = current
        return previous