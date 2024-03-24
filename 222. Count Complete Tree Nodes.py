from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:

        def recursive_count(node: Optional[TreeNode]) -> int:
            if not node:
                return 0

            l_c = 1 + recursive_count(node.left)
            r_c = 0
            if node.left and node.right:
                r_c += recursive_count(node.right)
            return l_c + r_c

        return recursive_count(root)
