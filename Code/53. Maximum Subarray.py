class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        res = float('-inf')
        prev = float('-inf')
        for number in nums:
            prev = max(prev + number, number)
            res = max(res, prev)
        return res