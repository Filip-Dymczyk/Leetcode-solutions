from typing import Optional



class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        next1 = l1
        next2 = l2
        head = ListNode()
        res = head
        extra = 0
        while next1 or next2 or extra:
            v1 = next1.val if next1 else 0
            v2 = next2.val if next2 else 0
            carry, curr = divmod(v1 + v2 + extra, 10)
            res.next = ListNode(val=curr)
            res = res.next
            next1 = next1.next if next1 else None
            next2 = next2.next if next2 else None
            extra = carry

        return head.next
