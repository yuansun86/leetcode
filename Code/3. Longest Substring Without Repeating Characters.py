class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        length = len(s)
        max_length = 0
        i, j = -1, 0
        last_pos = {}
        for j in range(length):
            ch = s[j]
            if ch in last_pos:
                i = max(last_pos[ch], i)
            max_length = max(max_length, j - i)
            last_pos[ch] = j
        return max_length

# class Solution:
    # sliding window
#     def lengthOfLongestSubstring(self, s: str) -> int:
#         max_length = 0
#         occ = set()
#         left, right = 0, 0
#         length = len(s)
#         max_length = 0
#         while left < length and right < length:
#             if s[right] not in occ:
#                 occ.add(s[right])
#                 right += 1
#                 max_length = max(max_length, right - left)
#             else:
#                 occ.remove(s[left])
#                 left += 1
#         return max_length