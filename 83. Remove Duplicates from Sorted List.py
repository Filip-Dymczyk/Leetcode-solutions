from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return
        prev = head
        curr = prev.next
        while curr:
            if prev.val == curr.val:
                prev.next = curr.next
                curr = prev.next
            else:
                prev = curr
                curr = curr.next

        return head
