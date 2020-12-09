class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        dp = [1 for _ in range(target + 1)]
        for i in range(1, target + 1):
            count = 0
            for value in nums:
                if i - value >= 0:
                    count += dp[i - value]
            dp[i] = count
        return dp[-1]