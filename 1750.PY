class Solution:
    def minimumLength(self, s: str) -> int:
        n: int = len(s)
        l_pointer: int = 0
        r_pointer: int = n - 1
        cur_char: str = s[0]

        while l_pointer < r_pointer and s[l_pointer] == s[r_pointer]:
            while l_pointer <= r_pointer and s[l_pointer] == cur_char:
                l_pointer += 1
            while r_pointer >= l_pointer and s[r_pointer] == cur_char:
                r_pointer -= 1
            if l_pointer < n:
                cur_char = s[l_pointer]

        if r_pointer < l_pointer:
            return 0
        else:
            return r_pointer - l_pointer + 1


# the same but lighter code
# class Solution:
#     def minimumLength(self, s: str) -> int:
#         left, right = 0, len(s) - 1

#         while left < right and s[left] == s[right]:
#             char = s[left]
#             while left <= right and s[left] == char:
#                 left += 1
#             while right >= left and s[right] == char:
#                 right -= 1

#         return right - left + 1
