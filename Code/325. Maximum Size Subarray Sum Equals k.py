class Solution:
    def maxSubArrayLen(self, nums: List[int], k: int) -> int:
        d = collections.defaultdict(int)
        prefix = 0
        d[0] = 0
        res = 0
        for i, number in enumerate(nums):
            prefix += number
            if prefix - k in d:
                res = max(res, i + 1 - d[prefix - k])
            if prefix not in d:
                d[prefix] = i + 1
        return res