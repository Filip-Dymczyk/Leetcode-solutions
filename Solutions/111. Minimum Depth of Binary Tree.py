from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        def in_min_depth(node: Optional[TreeNode]) -> int:
            if not node:
                return 0
            min_left = 1 + in_min_depth(node.left)
            min_right = 1 + in_min_depth(node.right)
            if min_left == 1:
                return min_right
            elif min_right == 1:
                return min_left
            return min(min_left, min_right)
        return in_min_depth(root)
