class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        res = []
        intervals.sort()
        for i in range(len(intervals)):
            if i == 0:
                res.append(intervals[i])
                continue
            prev = res[-1]
            cur = intervals[i]
            if prev[0] == cur[0]:
                prev[1] = max(prev[1], cur[1])
            elif prev[1] >= cur[1]:
                continue
            else:
                res.append(cur)
        return len(res)