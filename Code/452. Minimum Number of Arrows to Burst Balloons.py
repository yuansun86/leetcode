class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        res = []
        points.sort()
        for i in range(len(points)):
            if i == 0:
                res.append(points[0])
                continue
            prev = res[-1]
            cur = points[i]
            if cur[0] > prev[1]:
                res.append(cur)
            else:
                prev[0] = cur[0]
                prev[1] = min(cur[1], prev[1])
        return len(res)