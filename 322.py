from math import isinf


class Solution:
    def coinChange(self, coins: list[int], amount: int) -> int:
        dp: list[int] = [float("inf") for _ in range(amount + 1)]
        dp[0] = 0

        for coin in coins:
            for ind in range(coin, amount + 1, 1):
                dp[ind] = min(dp[ind], dp[ind - coin] + 1)

        return dp[-1] if not isinf(dp[-1]) else -1
