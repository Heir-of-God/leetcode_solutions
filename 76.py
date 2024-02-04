from collections import Counter


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        s_count, t_count = Counter(), Counter(t)
        l, r = 0, 0
        res = ""
        min_l = float("inf")

        while r != len(s):
            s_count[s[r]] += 1
            r += 1
            if s_count & t_count != t_count:
                continue

            while l < r and s_count & t_count == t_count:
                s_count[s[l]] -= 1
                l += 1
            if r - l + 2 < min_l:
                min_l = r - l + 2
                res = s[l - 1 : r]

        return res
