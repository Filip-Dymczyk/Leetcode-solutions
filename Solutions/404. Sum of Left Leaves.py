from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        def rec_sum_left_leaves(node: Optional[TreeNode], source: str) -> int:
            if not node:
                return 0
            if not node.left and not node.right:
                if source == "left":
                    return node.val
                return 0
            return rec_sum_left_leaves(node.left, "left") + rec_sum_left_leaves(node.right, "right")
        return rec_sum_left_leaves(root, "root")
