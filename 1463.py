class Solution:
    def cherryPickup(self, grid: list[list[int]]) -> int:
        rows: int = (len(grid),)
        cols: int = len(grid[0])
        dp: list[list[list[int]]] = [
            [[0 for _ in range(cols + 2)] for _ in range(cols + 2)] for _ in range(rows + 1)
        ]
        # dp - describes states of robots, dp[i] - current row and dp[i][j] position of robot 1 and for every its position
        # there dp[i][j][k] for posiotion for second robot. Robots are moving in the same time and every move on the same row

        def get_next_max(row: int, col_r1: int, col_r2: int) -> int:
            res: int = 0
            for next_col_r1 in (col_r1 - 1, col_r1, col_r1 + 1):
                for next_col_r2 in (col_r2 - 1, col_r2, col_r2 + 1):
                    res = max(res, dp[row + 1][next_col_r1 + 1][next_col_r2 + 1])

            return res

        for row in reversed(range(rows)):
            for col_r1 in range(min(cols, row + 2)):
                for col_r2 in range(max(0, cols - row - 1), cols):

                    reward: int = grid[row][col_r1] + grid[row][col_r2]
                    if col_r1 == col_r2:
                        reward /= 2

                    dp[row][col_r1 + 1][col_r2 + 1] = reward + get_next_max(row, col_r1, col_r2)

        return dp[0][1][cols]
