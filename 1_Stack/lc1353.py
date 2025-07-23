import heapq
from typing import List

class Solution:
    def maxEvents(self, events: List[List[int]]) -> int:
        n = len(events)
        max_day = max(event[1] for event in events)
        events.sort()
        mh = [] # min-heap to track end days of events
        ans, j = 0, 0

        for i in range(1, max_day + 1):
            while j < n and events[j][0] <= i:
                heapq.heappush(mh, events[j][1])
                j+=1

            while mh and mh[0] < i:
                heapq.heappop(mh)

            if mh:
                heapq.heappop(mh)
                ans += 1

        return ans
        