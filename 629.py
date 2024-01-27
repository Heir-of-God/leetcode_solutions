class Solution:
    def kInversePairs(self, n: int, k: int) -> int:
        mod: int = 10**9 + 7
        dp: list[int] = [1] + [0] * k
        prefix_sum: list[int] = [0] * (k + 2)

        for cur_number in range(1, n + 1):
            for cur_number_of_pairs in range(1, k + 1):
                dp[cur_number_of_pairs] = (
                    prefix_sum[cur_number_of_pairs + 1] - prefix_sum[max(0, cur_number_of_pairs - cur_number - 1)]
                ) % mod
            for index in range(1, k + 2):
                prefix_sum[index] = (prefix_sum[index - 1] + dp[index - 1]) % mod

        return dp[k]
