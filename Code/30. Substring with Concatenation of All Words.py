class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        count = {}
        for word in words:
            count[word] = count.get(word, 0) + 1
        res = []
        length = len(s)
        word_count = len(words)
        word_length = len(words[0])
        for i in range(length - word_count * word_length + 1):
            seen = {}
            found = True
            for j in range(word_count):
                substring = s[i + j * (word_length):i + (j + 1) * word_length]
                if substring not in count:
                    found = False
                    break
                else:
                    seen[substring] = seen.get(substring, 0) + 1
                    if seen[substring] > count[substring]:
                        found = False
                        break
            if found:
                res.append(i)
        return res
                    