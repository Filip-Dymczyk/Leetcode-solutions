from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        if not head or not head.next:
            return head

        node = head.next
        prev_node = head

        res = None

        while node:
            if not res:
                res = ListNode(node.val)
                res.next = ListNode(prev_node.val)
            else:
                new_res = ListNode(node.val)
                new_res.next = res
                res = new_res
            node = node.next
            prev_node = prev_node.next
        return res
