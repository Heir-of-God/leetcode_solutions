class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        zeros: int = 0
        ones: int = 0

        for char in s:
            if char == "1":
                ones += 1
            else:
                zeros += 1

        return (ones - 1) * "1" + zeros * "0" + "1"
