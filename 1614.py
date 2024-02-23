class Solution:
    def maxDepth(self, s: str) -> int:
        mx_so_far: int = 0
        cur_opened: int = 0

        for char in s:
            if char == "(":
                cur_opened += 1
                mx_so_far = max(mx_so_far, cur_opened)
            elif char == ")":
                cur_opened -= 1

        return mx_so_far
