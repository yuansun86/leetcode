class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        h = []
        t = []
        res = []
        for i, (start, duration) in enumerate(tasks):
            t.append([start, duration, i])
        t.sort(reverse = True)
        curTime = None
        while t or h:
            if not curTime:
                start, duration, index = t.pop()
                curTime = start + duration
                res.append(index)
            else:
                while t and t[-1][0] <= curTime:
                    start, duration, index = t.pop()
                    heapq.heappush(h, (duration, index))
                if h:
                    duration, index = heapq.heappop(h)
                    curTime += duration
                    res.append(index)
                else:
                    if t:
                        start, duration, index = t.pop()
                        curTime = start + duration
                        res.append(index)
        return res
            