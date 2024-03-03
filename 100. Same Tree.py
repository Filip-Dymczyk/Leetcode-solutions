from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:

        def check_identity(node_p: Optional[TreeNode], node_q: Optional[TreeNode]) -> bool:
            if not node_p and not node_q:
                return True
            elif node_p and node_q:
                return (node_p.val == node_q.val) and check_identity(node_p.left, node_q.left) and check_identity(node_p.right, node_q.right)
            return False
        return check_identity(p, q)
