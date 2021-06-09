class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        d = {}
        for word in words:
            ch = word[0]
            if ch not in d:
                d[ch] = [word]
            else:
                d[ch].append(word)
        
        count = 0
        for ch in s:
            if ch not in d:
                continue
            else:
                prev = d[ch]
                del d[ch]
                for word in prev:
                    if len(word) == 1:
                        count += 1
                    else:
                        if word[1] in d:
                            d[word[1]].append(word[1:])
                        else:
                            d[word[1]] = [word[1:]]
        return count
            