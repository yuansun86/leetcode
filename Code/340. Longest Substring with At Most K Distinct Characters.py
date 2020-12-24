class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        if not s or not k:
            return 0
        
        occ = {}
        left, right = 0, 0
        max_length = 0
        length = len(s)
        while left < length and right < length:
            ch = s[right]
            if ch in occ:
                occ[ch] += 1
                max_length = max(max_length, right - left + 1)
                right += 1
            elif ch not in occ and len(occ) < k:
                occ[ch] = 1
                max_length = max(max_length, right - left + 1)
                right += 1
            else:
                occ[s[left]] -= 1
                if occ[s[left]] == 0:
                    occ.pop(s[left])
                left += 1
        return max_length