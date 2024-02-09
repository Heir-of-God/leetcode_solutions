class Solution:
    def largestDivisibleSubset(self, nums: list[int]) -> list[int]:
        nums.sort()
        n: int = len(nums)
        dp: list[int] = [1 for _ in range(n)]
        max_size: int = 1
        max_ind: int = 0

        for cur_ind in range(1, n):
            for j in range(cur_ind):
                if nums[cur_ind] % nums[j] == 0:
                    dp[cur_ind] = max(dp[cur_ind], dp[j] + 1)
                    if dp[cur_ind] > max_size:
                        max_size = dp[cur_ind]
                        max_ind = cur_ind

        result: list[int] = []
        num: int = nums[max_ind]
        for cur_ind in range(max_ind, -1, -1):
            if num % nums[cur_ind] == 0 and dp[cur_ind] == max_size:
                result.append(nums[cur_ind])
                num = nums[cur_ind]
                max_size -= 1

        return result
