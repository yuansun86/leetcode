class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        res = []
        for i in range(len(intervals)):
            if i == 0:
                res.append(intervals[i])
                continue
            prev = res[-1]
            cur = intervals[i]
            if cur[0] >= prev[1]:
                res.append(cur)
                continue
            else:
                if cur[1] >= prev[1]:
                    continue
                else:
                    res.pop()
                    res.append(cur)
        return len(intervals) - len(res)