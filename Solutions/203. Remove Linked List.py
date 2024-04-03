from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        prev_node = head
        next_node = None

        if prev_node:
            next_node = prev_node.next

        while next_node:
            if prev_node.val == val:
                head = prev_node.next
                prev_node = head

                if prev_node:
                    next_node = prev_node.next
            else:
                if next_node.val == val:
                    next_node = next_node.next
                    prev_node.next = next_node
                else:
                    prev_node = prev_node.next
                    next_node = next_node.next

        return head if head and head.val != val else None
