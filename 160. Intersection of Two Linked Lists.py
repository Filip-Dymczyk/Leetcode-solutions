from typing import Optional


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        # Length of lists:
        lenA = 0
        lenB = 0

        # Pointer nodes of both lists:
        nextA = headA
        nextB = headB

        # Getting lengths of lists:
        while nextA or nextB:
            if nextA:
                lenA += 1
                nextA = nextA.next
            if nextB:
                lenB += 1
                nextB = nextB.next

        # Difference of lengths - elems to skip from longer list:
        diff = abs(lenA - lenB)

        # Count of skipped elems:
        i = 0

        intersection = None
        nextA = headA
        nextB = headB

        while nextA and nextB:
            # If we haven't skipped all nodes yet:
            if i < diff:
                # Skip node from appriopriate list:
                if lenA > lenB:
                    nextA = nextA.next
                if lenB > lenA:
                    nextB = nextB.next
                i += 1
            # Else - we skipped all required nodes:
            else:
                # If we have same values and haven't found intersection yet - begin intersection:
                if nextA == nextB and not intersection:
                    intersection = nextA
                # If we get not equal nodes - set intersection to None:
                elif nextA != nextB:
                    intersection = None
                # Iterate along the lists:
                nextA = nextA.next
                nextB = nextB.next
        return intersection
