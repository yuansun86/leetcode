class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def backtracking(first, nums, result):
            if first == len(nums) - 1:
                result.append(nums[::])
                return
            for i in range(first, len(nums)):
                nums[first], nums[i] = nums[i], nums[first]
                backtracking(first + 1, nums, result)
                nums[first], nums[i] = nums[i], nums[first]
        
        result = []
        backtracking(0, nums, result)
        return result