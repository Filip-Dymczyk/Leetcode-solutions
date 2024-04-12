from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        if not head:
            return head

        less_x = ListNode(-1)
        greater_x = ListNode(-1)
        node_less = less_x
        node_greater = greater_x
        node = head

        while node:
            if node.val < x:
                node_less.next = node
                node_less = node_less.next
            else:
                node_greater.next = node
                node_greater = node_greater.next
            node = node.next
        if node_less.next:
            node_less.next = None
        else:
            node_greater.next = None
        node_less.next = greater_x.next
        return less_x.next
