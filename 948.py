class Solution:
    def bagOfTokensScore(self, tokens: list[int], power: int) -> int:
        tokens.sort()
        cur_score: int = 0
        mx_score: int = 0

        while tokens and (tokens[0] <= power or cur_score):
            while tokens and power >= tokens[0]:
                power -= tokens.pop(0)
                cur_score += 1
            mx_score = max(mx_score, cur_score)
            cur_score -= 1
            if tokens:
                power += tokens.pop()

        return mx_score
