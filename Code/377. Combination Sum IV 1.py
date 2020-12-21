class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        def helper(target, hashmap):
            if target == 0:
                return 1
            if target in hashmap:
                return hashmap[target]
            result = 0
            for number in nums:
                if number <= target:
                    result += helper(target - number, hashmap)
            hashmap[target] = result
            return result
        
        return helper(target, {})