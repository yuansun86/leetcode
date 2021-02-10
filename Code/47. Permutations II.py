class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        used = set()
        results = []
        self.dfs(nums, used, [], results)
        return results
    
    def dfs(self, nums, used, path, results):
        if len(path) == len(nums):
            results.append(path[:])
            return
        for i in range(len(nums)):
            if i in used:
                continue
            if i > 0 and nums[i] == nums[i - 1] and i-1 not in used:
                continue
            path.append(nums[i])
            used.add(i)
            self.dfs(nums, used, path, results)
            used.remove(i)
            path.pop()