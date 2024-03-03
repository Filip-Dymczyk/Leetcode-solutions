from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []

        def in_inorder_traversal(node: TreeNode) -> None:
            if not node:
                return
            in_inorder_traversal(node.left)
            res.append(node.val)
            in_inorder_traversal(node.right)

        in_inorder_traversal(root)
        return res
