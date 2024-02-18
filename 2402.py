from heapq import heapify, heappush, heappop


class Solution:
    def mostBooked(self, n: int, meetings: list[list[int]]) -> int:
        meetings.sort()
        free_rooms: list[int] = [i for i in range(n)]
        occupied_rooms: list[tuple[int, int]] = []  # tuple(end_time of meeting, room_number)
        counter: list[int] = [0 for _ in range(n)]

        for start_time, end_time in meetings:
            while occupied_rooms and start_time >= occupied_rooms[0][0]:
                _, room_num = heappop(occupied_rooms)
                heappush(free_rooms, room_num)

            if not free_rooms:
                end, room_num = heappop(occupied_rooms)
                heappush(free_rooms, room_num)
                start_time, end_time = end, end + (end_time - start_time)

            room_number: int = heappop(free_rooms)
            counter[room_number] += 1
            heappush(occupied_rooms, (end_time, room_number))

        return counter.index(max(counter))
