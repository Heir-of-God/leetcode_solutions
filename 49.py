class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        res: list[list[str]] = []  # to store groups of words
        groups: dict[str, int] = {}  # key - group sorted string of chars, val - ind in res

        for word in strs:
            k: str = "".join(sorted(word))
            if not k in groups:
                groups[k] = len(res)
                res.append([])
            res[groups[k]].append(word)

        return res
