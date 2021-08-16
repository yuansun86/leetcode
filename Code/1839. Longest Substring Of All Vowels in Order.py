class Solution:
    def longestBeautifulSubstring(self, word: str) -> int:
        length = len(word)
        i = 0
        j = 0
        res = 0
        index = {'a':0, 'e':1, 'i':2, 'o':3, 'u':4}
        while i < length and j < length:
            if i == j:
                if word[i] != 'a':
                    i += 1
                    j += 1
                else:
                    j += 1
            else:
                if index[word[j]] == index[word[j-1]] or index[word[j]] == index[word[j-1]] + 1:
                    if word[j] == 'u':
                        res = max(res, j - i + 1)
                    j += 1
                else:
                    i = j
        return res