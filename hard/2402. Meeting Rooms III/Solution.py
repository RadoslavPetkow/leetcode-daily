from heapq import heappush, heappop, heapify
from typing import List

class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        meetings.sort()
        free = list(range(n))
        heapify(free)

        busy = []
        count = [0] * n

        for start, end in meetings:
            while busy and busy[0][0] <= start:
                end_time, room = heappop(busy)
                heappush(free, room)

            duration = end - start

            if free:
                room = heappop(free)
                heappush(busy, (end, room))
                count[room] += 1
            else:
                end_time, room = heappop(busy)
                new_end = end_time + duration
                heappush(busy, (new_end, room))
                count[room] += 1

        best = 0
        for i in range(1, n):
            if count[i] > count[best]:
                best = i
        return best