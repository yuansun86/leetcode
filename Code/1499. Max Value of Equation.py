class Solution:
    def findMaxValueOfEquation(self, points: List[List[int]], k: int) -> int:
        pq = []
        res = float('-inf')
        for j in range(len(points)):
            while len(pq) != 0 and points[j][0] - pq[0][1] > k:
                heapq.heappop(pq)
            if len(pq) != 0:
                res = max(res, -pq[0][0] + points[j][0] + points[j][1])
            heapq.heappush(pq, (points[j][0] - points[j][1], points[j][0]))
        return res
                