class Solution:
    def largestPerimeter(self, nums: list[int]) -> int:
        nums.sort(reverse=True)

        for i in range(len(nums)):
            lwr: int = sum(nums[i + 1 :])
            if nums[i] < lwr:
                return nums[i] + lwr
        return -1
