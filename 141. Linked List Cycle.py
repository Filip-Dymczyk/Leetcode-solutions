from typing import Optional


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    # Floyd’s Cycle-Finding Algorithm:
    def hasCycle(self, head: Optional[ListNode]) -> bool:

        # Initializing 2 pointers - fast and slow ones:
        fast_p = head
        slow_p = head

        while fast_p and fast_p.next:
            # Moving fast_p by 2 steps:
            fast_p = fast_p.next.next

            # Moving slow_p by 1 step:
            slow_p = slow_p.next

            # If pointers ever meet (fast caught up to slow) - we have a cycle:
            if fast_p == slow_p:
                return True

        # If we leave the loop we don't have a cycle:
        return False
