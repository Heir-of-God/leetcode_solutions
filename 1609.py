class Solution:
    def isEvenOddTree(self, root: Optional[TreeNode]) -> bool:
        q: list[TreeNode] = [root]
        cur_level = 0
        while q:
            prev = q.pop(0)
            if prev.val % 2 == cur_level % 2:
                return False
            n: int = len(q)
            if prev.left:
                q.append(prev.left)
            if prev.right:
                q.append(prev.right)
            prev = prev.val

            for _ in range(n):
                node: TreeNode = q.pop(0)
                if cur_level % 2 == 0:
                    if node.val % 2 == 0 or node.val <= prev:
                        return False
                else:
                    if node.val % 2 == 1 or node.val >= prev:
                        return False
                prev = node.val
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            cur_level += 1

        return True
