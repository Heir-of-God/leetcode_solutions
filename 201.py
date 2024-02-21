# O(n) but doesn't work - TLE
# class Solution(object):
#     def rangeBitwiseAnd(self, left, right) -> int:
#         res: int = 1
#         for num in range(left, right + 1, 1):
#             res &= num
#         return res


# O(logN) - does work
class Solution(object):
    def rangeBitwiseAnd(self, left, right) -> int:
        number_of_shifted_bits: int = 0
        while left != right:  # we are trying to find common prefix in binary representation
            left >>= 1
            right >>= 1
            number_of_shifted_bits += 1
        return left << number_of_shifted_bits
