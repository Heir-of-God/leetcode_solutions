class Solution:
    def sortedSquares(self, A: list[int]) -> list[int]:
        result: list[int] = [0] * len(A)
        write_pointer: int = len(A) - 1
        left_pointer: int = 0
        right_pointer: int = len(A) - 1
        left_square: int = A[left_pointer] ** 2
        right_square: int = A[right_pointer] ** 2
        while write_pointer >= 0:
            if left_square > right_square:
                result[write_pointer] = left_square
                left_pointer += 1
                left_square = A[left_pointer] ** 2
            else:
                result[write_pointer] = right_square
                right_pointer -= 1
                right_square = A[right_pointer] ** 2
            write_pointer -= 1
        return result
