class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        left = [0] * n
        right = [0] * n
        left_min = prices[0]
        left_profit = 0
        for i in range(n):
            left_min = min(left_min, prices[i])
            left_profit = max(left_profit, prices[i] - left_min)
            left[i] = left_profit
        
        right_max = prices[-1]
        right_profit = 0
        for i in range(n - 1, -1, -1):
            right_max = max(right_max, prices[i])
            right_profit = max(right_profit, right_max - prices[i])
            right[i] = right_profit
        # print(left)
        # print(right)
        res = 0
        for i in range(n):
            res = max(res, left[i] + right[i])
        return res