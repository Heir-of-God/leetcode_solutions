from collections import defaultdict


class Solution:
    def findJudge(self, n: int, trust: list[list[int]]) -> int:
        who_trust = set()  # set to store persons who trust somebody therefore not judges
        trust_counting = defaultdict(int)  # key - person, value - number of people trusting this person

        for pair in trust:
            who: int = pair[0]
            whom: int = pair[1]

            trust_counting[whom] += 1
            if not who in who_trust:
                who_trust.add(who)

        for person in range(1, n + 1, 1):
            if person not in who_trust and trust_counting[person] == n - 1:
                return person
        return -1
