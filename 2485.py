class Solution:
    def pivotInteger(self, n: int) -> int:
        fs = (1 + n) / 2 * n
        cur_s = 0
        cur_n = 0

        while (right_part := fs - cur_s + cur_n) >= cur_s:
            if right_part == cur_s:
                return cur_n
            cur_n += 1
            cur_s += cur_n

        return -1

# Genius
# class Solution(object):
#     def pivotInteger(self, n):
#         x = sqrt(n * (n + 1) / 2)

#         if x % 1 != 0:
#             return -1
#         else:
#             return int(x)
