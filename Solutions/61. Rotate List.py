from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return head
        linked_list = []

        node = head
        while node:
            linked_list.append(node)
            node = node.next

        k %= len(linked_list)

        if k == 0:
            return head

        new_head = linked_list[-k]
        last_node = linked_list[-(k + 1)]
        last_node.next = None
        linked_list[-1].next = head
        return new_head
