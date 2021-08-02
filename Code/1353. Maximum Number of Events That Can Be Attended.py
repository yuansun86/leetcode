class Solution:
    def maxEvents(self, events: List[List[int]]) -> int:
        h = []
        d = collections.defaultdict(list)
        count = 0
        for event in events:
            k = event[0]
            d[k].append(event)
        for day in range(1, 10**5 + 1):
            if day in d:
                for event in d[day]:
                    heapq.heappush(h, event[1])
            while h and h[0] < day:
                heapq.heappop(h)
            if h:
                heapq.heappop(h)
                count += 1
        return count