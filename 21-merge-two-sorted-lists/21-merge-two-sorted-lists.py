class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        current = dummy = ListNode()
        while list1 and list2:
            if list1.val < list2.val:
                current.next = list1
                list1 = list1.next
                current = current.next
            else:
                current.next = list2
                list2 = list2.next
                current = current.next

        if list1 is None and list2:
            current.next = list2
            list2 = list2.next
            current = current.next

        if list2 is None and list1:
            current.next = list1
            list1 = list1.next
            current = current.next

        return dummy.next
        