class Solution:
    def findTheLongestSubstring(self, s: str) -> int:
        vowels = {'a': 1, 'e': 2, 'i': 4, 'o': 8, 'u': 16}
        index_dict = {0: -1}
        n = 0
        result = 0
        for i, ch in enumerate(s):
            if ch in vowels:
                n ^= vowels[ch]
            if n not in index_dict:
                index_dict[n] = i
            else:
                result = max(result, i - index_dict[n])
        return result