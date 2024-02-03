class Solution:
    def maxSumAfterPartitioning(self, arr: list[int], k: int) -> int:
        dp: list[int] = [0 for _ in range(len(arr))]
        for i in range(k):
            dp[i] = max(arr[: i + 1]) * (i + 1)

        for ind in range(k, len(dp), 1):
            mx = 0
            for arr_ind_dif in range(k):
                cur_group: int = max(arr[ind - arr_ind_dif : ind + 1]) * (arr_ind_dif + 1)
                mx: int = max(mx, cur_group + dp[ind - arr_ind_dif - 1])
            dp[ind] = mx

        return dp[-1]
