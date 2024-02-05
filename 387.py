class Solution:
    def firstUniqChar(self, s: str) -> int:
        seen: set[str] = set()
        q: list[str] = []

        for char in s:
            if char in seen:
                if char in q:
                    q.remove(char)
                continue
            q.append(char)
            seen.add(char)

        return s.index(q[0]) if q else -1


# second solution. As effective
# class Solution:
#     def firstUniqChar(self, s: str) -> int:
#         for el in {i:0 for i in s}:
#             if s.count(el) == 1:
#                 return s.index(el)
#         return -1
