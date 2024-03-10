# class Solution:
#     def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
#         res = []
#         nums2 = set(nums2)

#         for el in nums1:
#             if el not in res and el in nums2:
#                 res.append(el)


#         return res


class Solution:
    def intersection(self, nums1: list[int], nums2: list[int]) -> list[int]:
        return set(nums1).intersection(nums2)
