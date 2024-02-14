class Solution:
    def rearrangeArray(self, nums: list[int]) -> list[int]:
        positive: list[int] = []
        negative: list[int] = []

        for num in nums:
            if num > 0:
                positive.append(num)
            else:
                negative.append(num)

        res: list[int] = []
        for i in range(len(nums) // 2):
            res.append(positive[i])
            res.append(negative[i])

        return res
