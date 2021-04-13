import math
class Solution:
    def numOfWays(self, nums: List[int]) -> int:
        return (self.helper(nums) - 1) % (10 ** 9 + 7)
    
    def helper(self, nums):
        if len(nums) <= 2:
            return 1
        
        smaller = []
        larger = []
        pivot = nums[0]
        for i in range(1, len(nums)):
            if nums[i] < pivot:
                smaller.append(nums[i])
            else:
                larger.append(nums[i])
        smaller_res = self.helper(smaller)
        larger_res = self.helper(larger)
        comb_res = math.comb(len(nums) - 1, len(smaller))
        return smaller_res * larger_res * comb_res
        