from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        def pt(node: Optional[TreeNode]) -> None:
            if not node:
                return
            pt(node.left)
            pt(node.right)
            res.append(node.val)
        pt(root)
        return res
