class Solution:
    def divideArray(self, nums: list[int], k: int) -> list[list[int]]:
        nums.sort()

        for i in range(2, len(nums), 3):
            if nums[i] - nums[i - 2] > k:
                return []

        return [nums[i : i + 3] for i in range(0, len(nums), 3)]
