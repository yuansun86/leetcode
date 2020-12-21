class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        length = len(nums)
        prefix_sum = [0 for _ in range(length + 1)]
        for i in range(1, length + 1):
            prefix_sum[i] = prefix_sum[i - 1] + nums[i - 1]
        max_count = -1
        target = prefix_sum[-1] - x
        left, right = 0, 1

        while left <= right and right < length + 1:
            current = prefix_sum[right] - prefix_sum[left]
            if current == target:
                max_count = max(max_count, right - left)
                right += 1
            elif current > target:
                left += 1
            else:
                right += 1
            
        if max_count == -1:
            return -1
        return len(nums) - max_count