# some very strange question, which tips say just brute force
class Solution:
    def countEven(self, num: int) -> int:

        def get_sum(num) -> int:
            s = 0
            while num > 0:
                s += num % 10
                num //= 10
            return s

        res: int = 0
        for num in range(2, num + 1, 1):
            if get_sum(num) % 2 == 0:
                res += 1
        return res


# Also noticed this interesting formula
# class Solution:
#     def countEven(self, num: int) -> int:
#         return (num - sum(map(int, str(num))) % 2) // 2
