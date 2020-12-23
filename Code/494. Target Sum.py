class Solution:
    # dfs with memorization
    def findTargetSumWays(self, nums: List[int], S: int) -> int:
        def dfs(nums, length, start, target, record):
            if start == length - 1:
                if target == 0 and target == nums[start]:
                    record[(start, target)] = 2
                    return 2
                elif target == nums[start] or target == -nums[start]:
                    record[(start, target)] = 1
                    return 1
                else:
                    record[(start, target)] = 0
                    return 0
            if (start, target) in record:
                return record[(start, target)]
            left = dfs(nums, length, start + 1, target - nums[start], record)
            right = dfs(nums, length, start + 1, target + nums[start], record)
            record[(start, target)] = left + right
            return left + right
        
        length = len(nums)
        record = {}
        return dfs(nums, length, 0, S, record)