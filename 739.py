# from collections import defaultdict


# class Solution:
#     def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
#         seen: defaultdict[int, int] = defaultdict(default_factory=0)
#         for ind in range(-1, -len(temperatures) - 1, -1):
#             cur: int = temperatures[ind]
#             seen[cur] = ind
#             i: int = 0
#             for warmer in range(cur + 1, 101, 1):
#                 i = min(i, seen.get(warmer, 0))


#             if i:
#                 temperatures[ind] = i - ind
#             else:
#                 temperatures[ind] = 0
#         return temperatures
## bad first solution
class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        res: list[int] = [0 for _ in range(len(temperatures))]
        stack: list[int] = []

        for ind, value in enumerate(temperatures):
            while stack and temperatures[stack[-1]] < value:
                index: int = stack.pop()
                res[index] = ind - index
            stack.append(ind)

        return res
