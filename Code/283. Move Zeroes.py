class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        left, right = 0, 0
        while right < len(nums):
            while right < len(nums) and nums[right] == 0:
                right += 1
            if right < len(nums):
                nums[left] = nums[right]
                left += 1
                right += 1
        for i in range(left, len(nums)):
            nums[i] = 0