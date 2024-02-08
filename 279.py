class Solution:
    def numSquares(self, n: int) -> int:
        ps: list[int] = []
        i = 1
        while i**2 <= n:
            ps.append(i**2)
            i += 1

        dp: list[int] = [float("inf") for _ in range(n + 1)]
        dp[0] = 0

        for perfect_square in ps:
            for ind in range(perfect_square, n + 1, 1):
                dp[ind] = min(dp[ind], dp[ind - perfect_square] + 1)

        return dp[-1]
