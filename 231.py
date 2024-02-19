class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        for power in range(31):  # n <= 2^31 - 1
            if 2**power == n:
                return True
        return False


# infinity iq solution
# class Solution:
#     def isPowerOfTwo(self, n: int) -> bool:
#         return n > 0 and n & (n - 1) == 0
