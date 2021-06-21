class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        words_length = 0
        words_count = 0
        res = []
        line = []
        i = 0
        while i < len(words):
            word = words[i]
            if words_length + words_count + len(word) <= maxWidth:
                line.append(word)
                words_length += len(word)
                words_count += 1
                i += 1
            else:
                res.append(self.processLine(line, maxWidth, False))
                line = []
                words_length = 0
                words_count = 0
        res.append(self.processLine(line, maxWidth, True))
        return res
        
        
    def processLine(self, line, maxWidth, isLast = False):
        if not isLast:
            words_count = len(line)
            if words_count == 1:
                return line[0] + " " * (maxWidth - len(line[0]))
            num_gaps = words_count - 1
            words_length = sum([len(word) for word in line])
            gaps = [0] * num_gaps
            spaces = maxWidth - words_length
            i = 0
            while spaces > 0:
                gaps[i] += 1
                spaces -= 1
                i = (i + 1) % len(gaps)
            # combine words and gaps
            res = []
            res.append(line[0])
            for i in range(num_gaps):
                res.append(" " * gaps[i])
                res.append(line[i + 1])
            return "".join(res)
        else:
            res = " ".join(line)
            if len(res) < maxWidth:
                res += (" " * (maxWidth - len(res)))
            return res
                