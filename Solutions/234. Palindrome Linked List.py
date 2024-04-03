from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        traverse = []
        node = head
        while node:
            traverse.append(node.val)
            node = node.next
        return traverse == traverse[::-1]
