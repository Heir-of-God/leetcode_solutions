class Solution:
    def countSubstrings(self, s: str) -> int:
        n: int = len(s)
        res: int = 0

        def count_palindromes(left: int, right: int) -> int:
            count = 0
            while left >= 0 and right < n and s[left] == s[right]:
                left -= 1
                right += 1
                count += 1
            return count

        for middle_index in range(n):
            res += count_palindromes(middle_index, middle_index + 1)
            res += count_palindromes(middle_index, middle_index)

        return res
