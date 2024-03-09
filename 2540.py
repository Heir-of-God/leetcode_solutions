class Solution:
    def getCommon(self, nums1: list[int], nums2: list[int]) -> int:
        p1 = 0
        p2 = 0

        n1, n2 = len(nums1), len(nums2)
        while p1 < n1 and p2 < n2:
            if nums1[p1] < nums2[p2]:
                p1 += 1
            elif nums1[p1] > nums2[p2]:
                p2 += 1
            else:
                return nums1[p1]

        return -1
