from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        head = None
        if list1 and list2:
            head = list1
            next1 = list1
            next2 = list2
            if list1.val > list2.val:
                head = list2
                next2 = next2.next
            else:
                next1 = next1.next
            curr_node = head
            while next1 or next2:
                if next1 and next2:
                    if next1.val > next2.val:
                        curr_node.next = next2
                        next2 = next2.next
                    else:
                        curr_node.next = next1
                        next1 = next1.next
                elif next1:
                    curr_node.next = next1
                    next1 = next1.next
                elif next2:
                    curr_node.next = next2
                    next2 = next2.next
                curr_node = curr_node.next
        elif list1:
            head = list1
        elif list2:
            head = list2
        return head
