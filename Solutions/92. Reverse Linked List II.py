from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        reverse_start = None
        reverse_tail = None
        prev_reverse = None
        after_reverse = None
        node = head
        count = 1
        while node:
            if count == left - 1:
                prev_reverse = node
            elif count == left:
                reverse_start = ListNode(node.val)
                reverse_tail = reverse_start
            elif reverse_start and count <= right:
                temp = ListNode(node.val)
                temp.next = reverse_start
                reverse_start = temp
            if count == right:
                after_reverse = node.next
                break
            node = node.next
            count += 1
        if prev_reverse:
            prev_reverse.next = reverse_start
        else:
            head = reverse_start
        reverse_tail.next = after_reverse
        return head
