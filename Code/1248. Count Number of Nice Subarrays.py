class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        for i in range(len(nums)):
            if nums[i] % 2 == 0:
                nums[i] = 0
            else:
                nums[i] = 1
        count = 0
        total = 0
        hashmap = {}
        hashmap[0] = 1
        for i in range(len(nums)):
            total += nums[i]
            if total - k in hashmap:
                count += hashmap[total - k]
            if total not in hashmap:
                hashmap[total] = 1
            else:
                hashmap[total] += 1
        return count