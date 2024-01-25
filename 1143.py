class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        dp: list[list[int]] = [
            [0 for _ in range(len(text2))] for _ in range(len(text1))
        ]  # rows - text1, cols - text2;     dp[i][j] - max length in text1[:i+1] and text2[:j+1]

        for col in range(len(text2)):
            dp[0][col] = int(text1[0] == text2[col] or dp[0][max(0, col - 1)])
        for row in range(len(text1)):
            dp[row][0] = int(text1[row] == text2[0] or dp[max(0, row - 1)][0])

        for i in range(1, len(text1)):
            for j in range(1, len(text2)):
                if text1[i] == text2[j]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

        return dp[-1][-1]
