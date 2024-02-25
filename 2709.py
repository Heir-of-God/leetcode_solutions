class UnionFind:
    def __init__(self, n: int) -> None:
        self.parent: list[int] = [i for i in range(n)]
        self.size: list[int] = [1 for _ in range(n)]
        self.count: int = n

    def find(self, x: int) -> int:
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y) -> None:
        px, py = self.find(x), self.find(y)
        if px == py:
            return
        if self.size[px] < self.size[py]:
            self.parent[px] = py
            self.size[py] += self.size[px]
        else:
            self.parent[py] = px
            self.size[px] += self.size[py]
        self.count -= 1


class Solution:
    def canTraverseAllPairs(self, nums: list[int]) -> bool:
        uf = UnionFind(len(nums))

        factor_index: dict[int, int] = {}  # factor -> index of value with this factor
        for ind, num in enumerate(nums):
            factor = 2
            while factor**2 <= num:
                if num % factor == 0:
                    if factor in factor_index:
                        uf.union(ind, factor_index[factor])
                    else:
                        factor_index[factor] = ind
                    while num % factor == 0:
                        num //= factor
                factor += 1

            if num > 1:
                if num in factor_index:
                    uf.union(ind, factor_index[num])
                else:
                    factor_index[num] = ind

        return uf.count == 1


# https://youtu.be/jZ-RVp5CVYY?si=LYi9D0hqd-9YvBcn
