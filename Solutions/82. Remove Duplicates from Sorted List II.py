from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
        f_node = head
        s_node = f_node.next

        while s_node:
            if f_node.val == s_node.val:
                while s_node and s_node.val == f_node.val:
                    s_node = s_node.next
                head = s_node
                f_node = head
                s_node = head.next if head else None
            elif s_node.next and s_node.val == s_node.next.val:
                while s_node.next and s_node.next.val == s_node.val:
                    s_node = s_node.next
                f_node.next = s_node.next
                s_node = f_node.next
            else:
                f_node = f_node.next
                s_node = s_node.next
        return head
