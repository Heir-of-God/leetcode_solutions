class Solution:
    def minPathSum(self, grid: list[list[int]]) -> int:

        for row_ind in range(len(grid)):
            for col_ind in range(len(grid[0])):
                if row_ind == col_ind == 0:
                    continue
                cur: int = grid[row_ind][col_ind]
                min_top: int | float = grid[row_ind - 1][col_ind] if row_ind != 0 else float("inf")
                min_left: int | float = grid[row_ind][col_ind - 1] if col_ind != 0 else float("inf")

                grid[row_ind][col_ind] = min(min_top, min_left) + cur

        return grid[-1][-1]
