# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        q: list[TreeNode] = [root]
        while q:
            print([node.val for node in q])
            first_val_on_this_level: int = q[0].val
            n = len(q)
            for _ in range(n):
                node: TreeNode = q.pop(0)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
        return first_val_on_this_level
