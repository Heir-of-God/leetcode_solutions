# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        def depth(node) -> int:
            nonlocal result
            if not node:
                return 0

            left: int = depth(node.left)
            right: int = depth(node.right)
            result: int = max(result, left + right)

            return max(left, right) + 1

        result = 0
        depth(root)
        return result
