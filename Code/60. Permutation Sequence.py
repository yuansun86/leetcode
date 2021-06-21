class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        lst = [str(i) for i in range(1, n + 1)]
        return self.helper(lst, k)
    
    def helper(self, nums, k):
        if len(nums) == 1:
            return nums[0]
        if k == 1:
            return ''.join(nums)
        
        n = len(nums)
        i = (k - 1) // math.factorial(n - 1)
        prefix = nums.pop(i)
        return prefix + self.helper(nums, k % math.factorial(n - 1))