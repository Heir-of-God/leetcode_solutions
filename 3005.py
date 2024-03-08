from collections import Counter


class Solution:
    def maxFrequencyElements(self, nums: list[int]) -> int:
        counter = Counter(nums)
        mx: int = 0
        res: int = 0
        for value in counter.values():
            if value > mx:
                res = 0
                mx = value
            if value == mx:
                res += mx

        return res
