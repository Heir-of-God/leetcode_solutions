class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        candidate: int = -1
        votes: int = 0

        for el in nums:
            if votes == 0:
                candidate = el
            if candidate == el:
                votes += 1
            else:
                votes -= 1

        return candidate


# there we're using Boger-Moore Majority Voting algorithm
# https://www.geeksforgeeks.org/boyer-moore-majority-voting-algorithm/
