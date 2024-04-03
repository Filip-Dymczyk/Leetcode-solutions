from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        if not root:
            return []

        res = []
        stack = []

        def traverse(node: Optional[TreeNode]) -> None:
            if not node.left and not node.right:
                stack.append(str(node.val))
                res.append('->'.join(stack))
                stack.pop()
                return None
            stack.append(str(node.val))
            if node.left:
                traverse(node.left)
            if node.right:
                traverse(node.right)
            stack.pop()
        traverse(root)
        return res
