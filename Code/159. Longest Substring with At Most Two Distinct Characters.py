class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        length = len(s)
        left, right = 0, 0
        max_length = 0
        occ = {}
        while left < length and right < length:
            if s[right] not in occ and len(occ) < 2:
                occ[s[right]] = 1
                max_length = max(max_length, right - left + 1)
                right += 1
            elif s[right] in occ:
                occ[s[right]] += 1
                max_length = max(max_length, right - left + 1)
                right += 1
            else:
                occ[s[left]] -= 1
                if occ[s[left]] == 0:
                    occ.pop(s[left])
                left += 1
        return max_length