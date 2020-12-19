class Solution:
    def numSquares(self, n: int) -> int:
        upper = int(n ** 0.5)
        squares = []
        for i in range(1, upper + 1):
            squares.append(i ** 2)
        dp = [float('inf') for i in range(n + 1)]
        dp[0] = 0
        for i in range(1, n + 1):
            for square in squares:
                if i < square:
                    break
                dp[i] = min(dp[i], 1 + dp[i - square])
        return dp[-1]