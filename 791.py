# class Solution:
#     def customSortString(self, order: str, s: str) -> str:
#         order += "qwertyuiopasdfghjklzxcvbnm"
#         return "".join(sorted(s, key=lambda x: order.index(x)))


from collections import Counter


class Solution:
    def customSortString(self, order: str, s: str) -> str:
        freq = Counter(s)
        res: str = ""
        for char in order:
            if char in freq:
                res += char * freq[char]

        for char in freq:
            if char not in res:
                res += char * freq[char]

        return res
