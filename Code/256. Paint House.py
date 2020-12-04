class Solution:
    def minCost(self, costs: List[List[int]]) -> int:
        if not costs:
            return 0
        result = [costs[0][0], costs[0][1], costs[0][2]]
        for i in range(1, len(costs)):
            result[0], result[1], result[2] = min(costs[i][0] + result[1], costs[i][0] + result[2]), \
                                              min(costs[i][1] + result[0], costs[i][1] + result[2]), \
                                              min(costs[i][2] + result[0], costs[i][2] + result[1])

        return min(result)