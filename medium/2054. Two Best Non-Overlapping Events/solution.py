from typing import List
import heapq

class Solution:
    def maxTwoEvents(self, events: List[List[int]]) -> int:
        events.sort(key=lambda x: x[0])

        heap = []
        best = 0
        ans = 0

        for start, end, value in events:
            while heap and heap[0][0] < start:
                e_end, e_val = heapq.heappop(heap)
                if e_val > best:
                    best = e_val

            if value > ans:
                ans = value
            if best + value > ans:
                ans = best + value

            heapq.heappush(heap, (end, value))

        return ans