class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        results = []
        used = set()
        self.dfs(nums, 0, [], used, results)
        return results
    
    def dfs(self, nums, index, path, used, results):
        results.append(path[:])
        for i in range(index, len(nums)):
            if i > index and nums[i] == nums[i - 1] and i - 1 not in used:
                continue
            used.add(i)
            path.append(nums[i])
            self.dfs(nums, i + 1, path, used, results)
            path.pop()
            used.remove(i)