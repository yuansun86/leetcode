class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
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