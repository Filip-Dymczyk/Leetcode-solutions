from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def recursive_invert(node: Optional[TreeNode]) -> None:
            if not node:
                return
            node.left, node.right = node.right, node.left
            recursive_invert(node.left)
            recursive_invert(node.right)

        recursive_invert(root)
        return root
