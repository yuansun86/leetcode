class Solution:
    def minSubArrayLen(self, s: int, nums: List[int]) -> int:
        if not nums:
            return 0
        left, right = 0, 0
        current_sum = nums[left]
        min_length = float('inf')
        while right < len(nums):
            if current_sum >= s:
                min_length = min(min_length, right - left + 1)
                if min_length == 1:
                    return 1
                current_sum -= nums[left]
                left += 1
            else:
                right += 1
                if right == len(nums):
                    break
                current_sum += nums[right]
        return min_length if min_length != float('inf') else 0