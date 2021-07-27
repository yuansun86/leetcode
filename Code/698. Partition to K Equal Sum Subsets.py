class Solution:
    ans = False
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        total = sum(nums)
        target = total // k
        if target != total / k:
            return False
        for number in nums:
            if number > target:
                return False
        self.helper(nums, k, set(), 0, target, 0)
        return self.ans
    
    def helper(self, nums, k, visited, cur, target, index):
        if k == 1:
            self.ans = True
            return
        
        if cur == target:
            self.helper(nums, k - 1, visited, 0, target, 0)
            return
        
        for i in range(index, len(nums)):
            if i in visited:
                continue
            if nums[i] + cur > target:
                continue
            else:
                visited.add(i)
                self.helper(nums, k, visited, cur + nums[i], target, i + 1)
                visited.remove(i)
        
                