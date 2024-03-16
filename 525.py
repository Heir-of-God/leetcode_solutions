class Solution:
    def findMaxLength(self, nums: list[int]) -> int:
        res = 0
        already_seen = {}
        cur_sum = 0

        for ind, num in enumerate(nums):
            cur_sum += 1 if num == 1 else -1
            if cur_sum == 0:
                res = ind + 1
            elif cur_sum not in already_seen:
                already_seen[cur_sum] = ind
            else:
                res = max(res, ind - already_seen[cur_sum])

        return res
