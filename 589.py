"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""


class Solution:
    def preorder(self, root: "Node") -> list[int]:
        if not root:
            return []
        res: list[int] = []

        def helper(node) -> None:
            res.append(node.val)
            for child in node.children:
                helper(child)

        helper(root)
        return res
