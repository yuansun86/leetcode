class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, K: int) -> int:
        dp = [[float('inf')] * (K + 1) for _ in range(n)]
        # dp[i][j] indicates the smallest cost from src to i via at most j stops
        graph = [[float('inf')] * n for _ in range(n)]
        for s, t, dist in flights:
            graph[s][t] = dist
            if s == src:
                dp[t][0] = dist
        for i in range(n):
            graph[i][i] = 0
        # for line in graph:
        #     print(line)
        for i in range(K + 1):
            dp[src][i] = 0
        for k in range(1, K + 1):
            for i in range(n):
                for j in range(n):
                    dp[i][k] = min(min(dp[j][k - 1] + graph[j][i], dp[i][k - 1]), dp[i][k])
        # for line in dp:
        #     print(line)
        return dp[dst][K] if dp[dst][K] != float('inf') else -1