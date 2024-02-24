# first written solution, not effective
# class Solution:
#     def findAllPeople(self, n: int, meetings: list[list[int]], firstPerson: int) -> list[int]:
#         meetings.sort(key=lambda x: x[2])
#         know_secret: set[int] = {0, firstPerson}

#         while meetings:
#             cur_time: int = meetings[0][2]
#             cur_meetings: list[list[int]] = []

#             while meetings and meetings[0][2] == cur_time:
#                 cur_meetings.append(meetings.pop(0))
#             added = True

#             while added:
#                 added = False
#                 for meeting in cur_meetings:
#                     if meeting[0] in know_secret:
#                         if not meeting[1] in know_secret:
#                             know_secret.add(meeting[1])
#                             added = True
#                     elif meeting[1] in know_secret:
#                         if not meeting[0] in know_secret:
#                             know_secret.add(meeting[0])
#                             added = True

#         return list(know_secret)


# the same solution, but optimized a bit
# class Solution:
#     def findAllPeople(self, n: int, meetings: list[list[int]], firstPerson: int) -> list[int]:
#         meetings.sort(key=lambda x: x[2])
#         know_secret: set[int] = {0, firstPerson}

#         while meetings:
#             cur_time: int = meetings[0][2]
#             cur_meetings: list[list[int]] = []

#             while meetings and meetings[0][2] == cur_time:
#                 cur_meetings.append(meetings.pop(0))
#             added = True

#             while added:
#                 added = False
#                 next_lst: list[list[int]] = []

#                 for meeting in cur_meetings:
#                     added_there = False
#                     if meeting[0] in know_secret:
#                         if not meeting[1] in know_secret:
#                             know_secret.add(meeting[1])
#                             added = True
#                             added_there = True
#                     elif meeting[1] in know_secret:
#                         if not meeting[0] in know_secret:
#                             know_secret.add(meeting[0])
#                             added = True
#                             added_there = True
#                     if not added_there:
#                         next_lst.append(meeting)
#                 cur_meetings = next_lst

#         return list(know_secret)


# Fast solution with graph
from collections import defaultdict
from itertools import groupby


class Solution:
    def findAllPeople(self, n: int, meetings: list[list[int]], firstPerson: int) -> list[int]:
        know_secret: set[int] = {0, firstPerson}
        for _, grp in groupby(sorted(meetings, key=lambda x: x[2]), key=lambda x: x[2]):
            stack = set()
            graph = defaultdict(list)
            for x, y, _ in grp:
                graph[x].append(y)
                graph[y].append(x)
                if x in know_secret:
                    stack.add(x)
                if y in know_secret:
                    stack.add(y)

            stack = list(stack)
            while stack:
                x = stack.pop()
                for y in graph[x]:
                    if y not in know_secret:
                        know_secret.add(y)
                        stack.append(y)
        return know_secret
