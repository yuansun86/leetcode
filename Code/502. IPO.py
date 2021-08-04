class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        projects = []
        heap = []
        for p, c in zip(profits, capital):
            projects.append((c, p))
        projects.sort(reverse = True)
        curCapital = w
        while projects or heap:
            if k == 0:
                break
            while projects and projects[-1][0] <= curCapital:
                c, p = projects.pop()
                heapq.heappush(heap, -p)
            if heap:
                curGain = -heapq.heappop(heap)
                curCapital += curGain
                k -= 1
            else:
                break
        return curCapital