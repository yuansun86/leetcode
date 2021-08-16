class Solution:
    def maxSumAfterOperation(self, nums: List[int]) -> int:
        not_used = []
        used = []
        not_used.append(nums[0])
        for i in range(1, len(nums)):
            not_used.append(max(nums[i], not_used[i - 1] + nums[i]))
        used.append(nums[0] ** 2)
        for i in range(1, len(nums)):
            used.append(max(max(nums[i] ** 2 + not_used[i - 1], used[i - 1] + nums[i]), nums[i] ** 2))
        return max(used)