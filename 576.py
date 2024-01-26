class Solution:
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        dp: list[list[int]] = [[0 for _ in range(n)] for _ in range(m)]
        dp[startRow][startColumn] = 1
        res: int = 0
        mod: int = 10**9 + 7

        for _ in range(1, maxMove + 1, 1):
            temp = [[0 for _ in range(n)] for _ in range(m)]

            for i in range(m):
                for j in range(n):
                    if i in [0, m - 1] or j in [0, n - 1]:
                        if i == m - 1:
                            res = res + dp[i][j]
                        if j == n - 1:
                            res = res + dp[i][j]
                        if i == 0:
                            res = res + dp[i][j]
                        if j == 0:
                            res = res + dp[i][j]

                    temp[i][j] = ((dp[i - 1][j] if i > 0 else 0) + (dp[i + 1][j] if i < m - 1 else 0)) + (
                        (dp[i][j - 1] if j > 0 else 0) + (dp[i][j + 1] if j < n - 1 else 0)
                    )
            dp = temp

        return res % mod
