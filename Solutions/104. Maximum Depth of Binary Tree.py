from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        def in_max_depth(node: Optional[TreeNode]) -> int:
            if not node:
                return 0
            max_left = 1 + in_max_depth(node.left)
            max_right = 1 + in_max_depth(node.right)
            return max(max_left, max_right)
        return in_max_depth(root)
