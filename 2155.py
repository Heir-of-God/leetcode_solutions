class Solution:
    def maxScoreIndices(self, nums: list[int]) -> list[int]:
        ones_in_arr: int = nums.count(1)
        res: list[int] = []
        mx = 0
        left_0, left_1 = 0, 0
        for ind in range(1, len(nums) + 1):
            if nums[ind - 1] == 0:
                left_0 += 1
            else:
                left_1 += 1
            right_1 = ones_in_arr - left_1
            if right_1 + left_0 > mx:
                res = [ind]
                mx = right_1 + left_0
            elif right_1 + left_0 == mx:
                res.append(ind)
        if ones_in_arr > mx:
            return [0]
        else:
            if ones_in_arr == mx:
                res.append(0)
            return res
