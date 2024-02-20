class Solution:
    def missingNumber(self, nums: list[int]) -> int:
        for n in range(max(nums) + 2):
            if not n in nums:
                return n


# Genius way by using Gauss sum https://dev.to/alisabaj/the-gauss-sum-and-solving-for-the-missing-number-996#:~:text=In%20this%20problem%2C%20we%20can,%2F%202%20%2C%20which%20is%206.
# class Solution:
#     def missingNumber(self, nums: list[int]) -> int:
#         n: int = len(nums)
#         return (n * (n + 1)) // 2 - sum(nums)
