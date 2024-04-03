from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head or not head.next:
            return None

        elems = []
        node = head
        while node:
            elems.append(node)
            node = node.next

        node_to_del = elems[-n]

        if n + 1 <= len(elems):
            node_prev_to_del = elems[-(n + 1)]
            node_prev_to_del.next = node_to_del.next
        else:
            head = node_to_del.next

        return head
