class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def dfs(nums, current, index, result):
            result.append(current.copy())
            for i in range(index + 1, len(nums)):
                current = current + [nums[i]]
                dfs(nums, current, i, result)
                current.pop()
        
        cur = []
        result = []
        dfs(nums, cur, -1, result)
        return result