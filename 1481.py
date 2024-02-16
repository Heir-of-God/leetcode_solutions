from heapq import heapify, heappop
from collections import Counter


class Solution:
    def findLeastNumOfUniqueInts(self, arr: list[int], k: int) -> int:
        hp: list = list(Counter(arr).values())
        heapify(hp)
        while k > 0:
            k -= heappop(hp)
        return len(hp) + (k < 0)
