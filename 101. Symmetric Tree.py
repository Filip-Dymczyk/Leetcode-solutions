from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:

        def check_symmetry(node_left: Optional[TreeNode], node_right: Optional[TreeNode]) -> bool:
            if not node_left and not node_right:
                return True
            elif node_left and node_right:
                return node_left.val == node_right.val and check_symmetry(node_left.left, node_right.right) and \
                    check_symmetry(node_left.right, node_right.left)
            return False
        return check_symmetry(root.left, root.right)
