import heapq


class Solution:
    def furthestBuilding(self, h: list[int], b: int, l: int) -> int:
        p: list[int] = []

        i = 0
        for i in range(len(h) - 1):
            diff: int = h[i + 1] - h[i]

            if diff <= 0:
                continue

            b -= diff
            heapq.heappush(p, -diff)

            if b < 0:
                b += -heapq.heappop(p)
                l -= 1

            if l < 0:
                return i
        return len(h) - 1
