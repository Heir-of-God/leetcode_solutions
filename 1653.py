class Solution:
    def minimumDeletions(self, s: str) -> int:
        if_end_a, if_end_b = 0, 0

        for val in s:
            if val == "a":
                if_end_b += 1
            else:
                if_end_b = min(if_end_a, if_end_b)
                if_end_a += 1

        return min(if_end_a, if_end_b)
